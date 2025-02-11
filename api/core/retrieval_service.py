from llama_index.core import SimpleDirectoryReader
from .app_service import AppService
from .file_service import FileService
from config import settings
import redis
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_redis import RedisConfig, RedisVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

class RetrievalService():
    @staticmethod
    def search_app(app_id:int,query:str,top_k:int):
        app = AppService.get_app_by_id(id=app_id)
        redis_url = settings.redis_url
        redis_client = redis.from_url(redis_url)
        embeddings = OllamaEmbeddings(model="llama3")
        index_name = app.name+"index_vector"
        config = RedisConfig(
            index_name=index_name,
            redis_url=redis_url,
            
        )

        vector_store = RedisVectorStore(embeddings=embeddings,index_name=index_name, config=config)

        query = "query"
        results = vector_store.similarity_search(query, k=top_k)

        print("Simple Similarity Search Results:")
        for doc in results:
            print(f"Content: {doc.page_content[:100]}...")
            print(f"Metadata: {doc.metadata}")
        
        return results


        
        
        

