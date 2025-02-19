export const COCOINDEX_PREFIX = "cocoindex.io/";

const attributeFullName = (name: string) => COCOINDEX_PREFIX + name;

export const MIME_TYPE = attributeFullName("mime_type");

export const CHUNK_BASE_TEXT = attributeFullName("chunk_base_text");

export const VECTOR_ORIGIN_TEXT = attributeFullName("vector_origin_text");
