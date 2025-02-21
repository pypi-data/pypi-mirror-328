export const flowSpec: unknown = {
    "name": "FilesEmbedding",
    "source_ops": [
      {
        "name": "documents",
        "kind": "LocalFile",
        "path": "devData/sourceFiles"
      }
    ],
    "reactive_ops": [
      {
        "name": ".foreach.0",
        "action": "ForEach",
        "field_path": [
          "documents"
        ],
        "op_scope": {
          "name": "_documents_0",
          "ops": [
            {
              "name": "markdown",
              "action": "Transform",
              "inputs": [
                {
                  "kind": "Field",
                  "scope": "_documents_0",
                  "field_path": [
                    "content"
                  ]
                }
              ],
              "op": {
                "kind": "ToMarkdown"
              }
            },
            {
              "name": "chunks",
              "action": "Transform",
              "inputs": [
                {
                  "kind": "Field",
                  "scope": "_documents_0",
                  "field_path": [
                    "markdown"
                  ]
                }
              ],
              "op": {
                "kind": "SplitRecursively",
                "chunk_overlap": 100,
                "chunk_size": 300,
                "language": "markdown"
              }
            },
            {
              "name": ".foreach.1",
              "action": "ForEach",
              "field_path": [
                "chunks"
              ],
              "op_scope": {
                "name": "_chunks_1",
                "ops": [
                  {
                    "name": "embedding",
                    "action": "Transform",
                    "inputs": [
                      {
                        "kind": "Field",
                        "scope": "_chunks_1",
                        "field_path": [
                          "text"
                        ]
                      }
                    ],
                    "op": {
                      "kind": "SentenceTransformerEmbed",
                      "model": "sentence-transformers/all-MiniLM-L6-v2"
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    ]
  }