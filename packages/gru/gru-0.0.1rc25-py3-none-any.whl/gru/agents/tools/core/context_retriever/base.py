from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from langchain_core.vectorstores import VectorStore
from gru.agents.tools.core.code_generator.models import RetrievalResult


class ContextRetriever(ABC):

    def __init__(self, vector_store: VectorStore ,system_prompt: Optional[str] = None, user_prompt_template: Optional[str] = None):
        """
        Base class for Context Retrievers.

        :param system_prompt: Optional system prompt (default: None).
        :param user_prompt_template: Optional user prompt template (default: None).
        """
        self.vector_store = vector_store
        self.system_prompt = system_prompt
        self.user_prompt_template = user_prompt_template
        
    @abstractmethod
    async def initialize_store(self, tables: List[Dict[str, Any]]):
        pass

    @abstractmethod
    async def get_relevant_datasources(self, query: str, top_k: int) -> List[str]:
        pass

    @abstractmethod
    async def get_relevant_schemas(self, tables: List[str]) -> List[str]:
        pass

    @abstractmethod
    async def get_similar_examples(self, query: str) -> List[str]:
        pass

    @abstractmethod
    async def get_documentation(self, query: str) -> List[str]:
        pass

    @abstractmethod
    async def store_conversation(self, query: str, sql: str):
        pass

    @abstractmethod
    async def retrieve_context(self, query: str, top_k: int) -> RetrievalResult:
        pass
