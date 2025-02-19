from pydantic import BaseModel, Field, ConfigDict, FilePath

from aa_rag import setting
from aa_rag.gtypes import IndexType
from aa_rag.gtypes.models.base import BaseResponse


class IndexItem(BaseModel):
    knowledge_name: str = Field(default=..., examples=["fairy_tale"])
    index_type: IndexType = Field(
        default=setting.index.type, examples=[setting.index.type]
    )
    embedding_model: str = Field(
        default=setting.embedding.model, examples=[setting.embedding.model]
    )

    model_config = ConfigDict(extra="allow")


class ChunkIndexItem(IndexItem):
    file_path: FilePath = Field(default=..., examples=["./data/fairy_tale.txt"])
    chunk_size: int = Field(
        default=setting.index.chunk_size, examples=[setting.index.chunk_size]
    )
    chunk_overlap: int = Field(
        default=setting.index.overlap_size, examples=[setting.index.overlap_size]
    )
    index_type: IndexType = Field(
        default=setting.index.type, examples=[setting.index.type]
    )

    model_config = ConfigDict(extra="forbid")


class IndexResponse(BaseResponse):
    class Data(BaseModel):
        table_name: str = Field(..., examples=["fairy_tale_chunk_text_embedding_model"])

    message: str = Field(
        default="Indexing completed via ChunkIndex",
        examples=["Indexing completed via ChunkIndex"],
    )
    data: Data = Field(default_factory=Data)
