import chromadb
import chromadb.utils.embedding_functions as of
db = chromadb.PersistentClient(path="./chroma_db")
memories = db.get_or_create_collection("my_facts")

memories.upsert(
    documents=[
        "Hamster",
        "Ball",
        "Shoe",
    ],
    ids = ["fact1", "fact2", "fact3"]
)

print("\nstored:", memories.count(),"facts")

question = "heaven"
results = memories.query(query_texts=[question], n_results=3)

print(results["documents"]), results["distances"]
