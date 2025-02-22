from gru.agents.tools.core.code_generator.models import RetrievalResult
from gru.agents.tools.core.context_retriever.base import ContextRetriever
from langchain_core.vectorstores import VectorStore, InMemoryVectorStore
from langchain_openai.embeddings import OpenAIEmbeddings
from typing import Optional, List, Dict, Any


class DefaultContextRetriever(ContextRetriever):
    def __init__(
        self,
        vector_store: VectorStore,
        system_prompt: Optional[str] = None,
        user_prompt_template: Optional[str] = None,
    ):
        """
        Initializes the Default Context Retriever with an optional prompt.

        :param vector_store: Vector database store for retrieval.
        :param system_prompt: Optional system-level prompt for LLM-based retrieval.
        :param user_prompt_template: Optional user prompt template for querying context.
        """
        self.embeddings = OpenAIEmbeddings()
        vector_db = vector_store or InMemoryVectorStore(embedding=OpenAIEmbeddings())
        super().__init__(vector_store=vector_db, system_prompt=system_prompt, user_prompt_template=user_prompt_template)

    async def initialize_store(self, tables: List[Dict[str, Any]]):
        # Implementation
        raise NotImplementedError("Method not implemented yet")

    async def get_relevant_datasources(self, query: str, top_k: int) -> List[str]:
        # Implementation
        raise NotImplementedError("Method not implemented yet")

    async def get_relevant_schemas(self, tables: List[str]) -> List[str]:
        # Implementation
        raise NotImplementedError("Method not implemented yet")

    async def get_similar_examples(self, query: str) -> List[str]:
        # Implementation
        raise NotImplementedError("Method not implemented yet")

    async def get_documentation(self, query: str) -> List[str]:
        # Implementation
        raise NotImplementedError("Method not implemented yet")

    async def store_conversation(self, query: str, sql: str):
        # Implementation
        raise NotImplementedError("Method not implemented yet")
    
    async def retrieve_context(self, query: str, top_k: int = 5) -> RetrievalResult:
        """
        Retrieves relevant context for the query by fetching data from the vector database.
        """
        tables = await self.get_relevant_datasources(query, top_k)
        schemas = await self.get_relevant_schemas(tables)
        examples = await self.get_similar_examples(query)
        docs = await self.get_documentation(query)

        return RetrievalResult(
            tables=tables,
            schemas=schemas,
            documentation=docs,
            examples=examples,
            low_cardinality_values=[],
            domain_knowledge=[],
            opt_rules=[],
        )

