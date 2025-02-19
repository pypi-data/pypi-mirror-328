import hashlib
import uuid
from pathlib import Path

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from markitdown import MarkItDown

from aa_rag import setting
from aa_rag.db import LanceDBDataBase
from aa_rag.db.base import BaseVectorDataBase, BaseNoSQLDataBase
from aa_rag.db.milvus_ import MilvusDataBase
from aa_rag.db.mongo_ import MongoDBDataBase
from aa_rag.db.tinydb_ import TinyDBDataBase
from aa_rag.gtypes.enums import VectorDBType, NoSQLDBType


def parse_file(file_path: Path) -> Document:
    """
    Parse a file and return a Document object.

    Args:
        file_path (str): Path to the file to be parsed.

    Returns:
        Document: Document object containing the parsed content and metadata.
    """
    assert file_path.exists(), f"File not found: {file_path}"

    md = MarkItDown()
    content_str = md.convert(str(file_path.absolute())).text_content

    return Document(page_content=content_str, metadata={"source": file_path.name})


def calculate_md5(input_string: str) -> str:
    """
    Calculate the MD5 hash of a string.

    Args:
        input_string (str): need to be calculated.

    Returns:
        str: MD5 hash of the input string.
    """
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode("utf-8"))
    return md5_hash.hexdigest()


def get_embedding_model(
    model_name: str, return_dim: bool = False
) -> Embeddings | tuple[Embeddings, int]:
    """
    Get the embedding model based on the model name.
    Args:
        model_name (str): Model name.
        return_dim (bool): Return the embedding dimension if True.

    Returns:
        Embeddings: Embedding model instance.
        If return_dim is True, also returns the number of dimensions.

    """
    assert setting.openai.api_key, (
        "OpenAI API key is required for using OpenAI embeddings."
    )
    embeddings = OpenAIEmbeddings(
        model=model_name,
        dimensions=1536,
        api_key=setting.openai.api_key,
        base_url=setting.openai.base_url,
    )
    if return_dim:
        return embeddings, embeddings.dimensions or 1536
    else:
        return embeddings


def get_llm(model_name: str) -> BaseChatModel:
    assert setting.openai.api_key, (
        "OpenAI API key is required for using OpenAI embeddings."
    )
    model = ChatOpenAI(
        model=model_name,
        api_key=setting.openai.api_key,
        base_url=setting.openai.base_url,
    )

    return model


def get_vector_db(db_type: VectorDBType) -> BaseVectorDataBase | None:
    match db_type:
        case VectorDBType.LANCE:
            return LanceDBDataBase()
        case VectorDBType.MILVUS:
            return MilvusDataBase()
        case _:
            raise ValueError(f"Invalid db type: {db_type}")


def get_nosql_db(db_type: NoSQLDBType) -> BaseNoSQLDataBase | None:
    match db_type:
        case NoSQLDBType.TINYDB:
            return TinyDBDataBase()
        case NoSQLDBType.MONGODB:
            return MongoDBDataBase()
        case _:
            raise ValueError(f"Invalid db type: {db_type}")


def get_db(
    db_type: NoSQLDBType | VectorDBType,
) -> BaseNoSQLDataBase | BaseVectorDataBase | None:
    if isinstance(db_type, NoSQLDBType):
        return get_nosql_db(db_type)
    elif isinstance(db_type, VectorDBType):
        return get_vector_db(db_type)
    else:
        raise ValueError(f"Invalid db type: {db_type}")


def get_uuid():
    return str(uuid.uuid4()).replace("-", "")
