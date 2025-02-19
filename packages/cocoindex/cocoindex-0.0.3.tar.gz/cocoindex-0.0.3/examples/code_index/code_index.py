import cocoindex
from dotenv import load_dotenv

def code_to_embedding(text: cocoindex.DataSlice) -> cocoindex.DataSlice:
    """
    Embed the text using a SentenceTransformer model.
    """
    return text.transform(
        cocoindex.transforms.SentenceTransformerEmbed(
            model="sentence-transformers/all-MiniLM-L6-v2"))

@cocoindex.flow_def(name="CodeIndexing")
def code_indexing_flow(flow_builder: cocoindex.FlowBuilder, data_scope: cocoindex.DataScope):
    """
    Define an example flow that embeds files into a vector database.
    """
    data_scope["files"] = flow_builder.add_source(cocoindex.sources.LocalFile(path="../../ui/src/lib"))

    code_embeddings = data_scope.add_collector()

    with data_scope["files"].entry() as file:
        file["chunks"] = file["content"].transform(
                    cocoindex.transforms.SplitRecursively(
                        language="javascript", chunk_size=300, chunk_overlap=100))
        with file["chunks"].entry() as chunk:
            chunk["embedding"] = chunk["text"].call(code_to_embedding)
            code_embeddings.collect(filename=file["filename"], location=chunk["location"],
                                    code=chunk["text"], embedding=chunk["embedding"])

    code_embeddings.export(
        "code_embeddings",
        cocoindex.storages.Postgres(),
        primary_key_fields=["filename", "location"],
        vector_index=[("embedding", cocoindex.VectorSimilarityMetric.COSINE_SIMILARITY)])


query_handler = cocoindex.query.SimpleSemanticsQueryHandler(
    name="SemanticsSearch",
    fl=code_indexing_flow,
    target_name="code_embeddings",
    query_transform_flow=code_to_embedding,
    default_similarity_metric=cocoindex.VectorSimilarityMetric.COSINE_SIMILARITY)

@cocoindex.cli_main()
def _run():
    cocoindex.start_server()
    input("Press Enter to stop...")

if __name__ == "__main__":
    load_dotenv()
    _run()
