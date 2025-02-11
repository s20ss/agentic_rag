from llama_index.core import SimpleDirectoryReader
from .app_service import AppService
from .file_service import FileService
from config import settings
import redis
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_redis import RedisConfig, RedisVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

class IndexingService():
    @staticmethod
    def index_app(app_id):
        app = AppService.get_app_by_id(id=app_id)
        related_files = FileService.get_app_files(app_id=app_id)
        related_files_location = [related_file.file_location for related_file in related_files]
        reader = SimpleDirectoryReader(input_files=related_files_location)
        documents = reader.load_data()
        ids = []
        updated_documents =[]
        print("DOCUMENTS",documents[0])
        for idx,document in enumerate(documents):
            print((document.to_dict()),)
            updated_documents.append(
                Document(
                    page_content=document.text,
                    metadata=document.metadata,
                )
            )
            ids.append(idx)
            

        redis_url = settings.redis_url
        redis_client = redis.from_url(redis_url)
        

        embeddings = OllamaEmbeddings(model="llama3")
        index_name = app.name+"index_vector"
        config = RedisConfig(
            index_name=index_name,
            redis_url=redis_url,
            
        )

        vector_store = RedisVectorStore(embeddings=embeddings,index_name=index_name, config=config)
        
        vector_store.add_documents(documents=updated_documents,ids=ids)

        query = "Shashank Shekhar Shukla"
        results = vector_store.similarity_search(query, k=2)

        print("Simple Similarity Search Results:")
        for doc in results:
            print(f"Content: {doc.page_content[:100]}...")
            print(f"Metadata: {doc.metadata}")
            print()


        print(dir(vector_store))
        
        

