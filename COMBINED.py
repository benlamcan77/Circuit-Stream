import chromadb
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(
base_url="https://api.groq.com/openai/v1",
api_key=os.getenv("GITHUB_TOKEN"),
)

db = chromadb.PersistentClient(path="./chroma_db")
memories = db.get_or_create_collection("my_facts")

memories.upsert(
    documents=[
        "LeBron",
        "Jordan",
        "Doncic",
    ],
    ids = ["fact1", "fact2", "fact3"]
)

question = input("What is the question?")
results = memories.query(query_texts=[question], n_results=3)

notes = "\n".join(results["documents"][0])

prompt = f"""
Here are some things I remember:

{notes}

Answer the user's question using the memories above.

Question: {question}
"""

r = client.chat.completions.create(
model="llama-3.3-70b-versatile",
messages=[{"role": "user", "content": prompt}],
)


print(r.choices[0].message.content)
