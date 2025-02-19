import cocoindex
from dotenv import load_dotenv

def text_to_embedding(text: cocoindex.DataSlice) -> cocoindex.DataSlice:
    """
    Embed the text using a SentenceTransformer model.
    """
    return text.transform(
        cocoindex.transforms.SentenceTransformerEmbed(
            model="sentence-transformers/all-MiniLM-L6-v2"))

@cocoindex.flow_def(name="FilesEmbedding")
def files_embedding_flow(flow_builder: cocoindex.FlowBuilder, data_scope: cocoindex.DataScope):
    """
    Define an example flow that embeds files into a vector database.
    """
    data_scope["documents"] = flow_builder.add_source(cocoindex.sources.LocalFile(path="sourceFiles"))

    doc_embeddings = data_scope.add_collector()

    with data_scope["documents"].entry() as doc:
        doc["chunks"] = doc["content"].transform(
            cocoindex.transforms.SplitRecursively(
                language="markdown", chunk_size=300, chunk_overlap=100))

        with doc["chunks"].entry() as chunk:
            chunk["embedding"] = chunk["text"].call(text_to_embedding)
            doc_embeddings.collect(filename=doc["filename"], location=chunk["location"],
                                   text=chunk["text"], embedding=chunk["embedding"])

    doc_embeddings.export(
        "doc_embeddings",
        cocoindex.storages.Postgres(),
        primary_key_fields=["filename", "location"],
        vector_index=[("embedding", cocoindex.VectorSimilarityMetric.COSINE_SIMILARITY)])

query_handler = cocoindex.query.SimpleSemanticsQueryHandler(
    name="SemanticsSearch",
    fl=files_embedding_flow,
    target_name="doc_embeddings",
    query_transform_flow=text_to_embedding,
    default_similarity_metric=cocoindex.VectorSimilarityMetric.COSINE_SIMILARITY)

@cocoindex.cli_main()
def _run():
    cocoindex.start_server()
    input("Press Enter to stop...")

if __name__ == "__main__":
    load_dotenv()
    _run()
