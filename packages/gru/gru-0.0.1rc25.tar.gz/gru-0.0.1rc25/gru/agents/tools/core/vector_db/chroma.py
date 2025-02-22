from gru.agents.tools.core.vector_db.base import VectorDBClient
from gru.agents.tools.core.vector_db.models import VectorDBConfig
from typing import List, Dict, Any


class ChromaDBClient(VectorDBClient):
    def connect(self, config: VectorDBConfig) -> None:
        raise NotImplementedError("Method not implemented yet")

    async def similarity_search(self, query: str, top_k: int) -> List[Dict[str, Any]]:
        raise NotImplementedError("Method not implemented yet")

    async def filtered_search(
        self, query: str, filters: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        raise NotImplementedError("Method not implemented yet")

    async def add_to_collection(self, collection_name: str, documents: List[Dict[str, Any]]):
        raise NotImplementedError("Method not implemented yet")

    async def update_collection(self, collection_name: str, document_id: str, update_data: Dict[str, Any]):
        raise NotImplementedError("Method not implemented yet")

    async def create_embedding(self, text: str) -> List[float]:
        raise NotImplementedError("Method not implemented yet")

    async def delete_from_collection(self, collection_name: str, document_id: str):
        raise NotImplementedError("Method not implemented yet")

    async def list_collections(self) -> List[str]:
        raise NotImplementedError("Method not implemented yet")

    async def get_collection_stats(self, collection_name: str) -> Dict[str, Any]:
        raise NotImplementedError("Method not implemented yet")

    async def reset_collection(self, collection_name: str):
        raise NotImplementedError("Method not implemented yet")
