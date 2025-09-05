import os
import glob
import math
import google.generativeai as genai

# --- 1. Setup Gemini ---
genai.configure(api_key="AIzaSyDUzi1aauluPA859Ef5m73p2zzQ9FWdG1k")
model_name = "gemini-1.5-flash"

# --- 2. Load + chunk docs ---
def chunk_text(text, max_length=500):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

doc_files = glob.glob("/home/harish/Desktop/chatbot/docs/**/*.*", recursive=True)
doc_files = [f for f in doc_files if f.endswith((".md", ".txt", ".html"))]

chunks = []
for f in doc_files:
    with open(f, "r", encoding="utf-8") as file:
        text = file.read()
    for chunk in chunk_text(text):
        embedding = genai.embed_content(
            model="models/text-embedding-004",
            content=chunk
        )
        chunks.append({"text": chunk, "vector": embedding["embedding"]})

print(f"✅ Loaded {len(chunks)} chunks from {len(doc_files)} documents.")

# --- 3. Cosine similarity helper ---
def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(x ** 2 for x in v1))
    mag2 = math.sqrt(sum(x ** 2 for x in v2))
    return dot / (mag1 * mag2)

# --- 4. Ask function for Jupyter ---
chat_model = genai.GenerativeModel(model_name)

def ask_bot(question):
    if not question:
        return "Please enter a question."

    # Embed question
    q_embed = genai.embed_content(
        model="models/text-embedding-004",
        content=question
    )["embedding"]

    # Rank chunks by similarity
    ranked = sorted(
        [(c, cosine_similarity(q_embed, c["vector"])) for c in chunks],
        key=lambda x: -x[1]
    )[:3]

    # Build prompt
    context = "\n---\n".join(c["text"] for c, _ in ranked)
    prompt = f"""
    You are an assistant that answers questions based only on the following document excerpts.
    If the answer isn't clearly in the documents, reply with "I don't know."
    DOCUMENTS:
    {context}
    QUESTION: {question}
    """

    # Ask Gemini
    response = chat_model.generate_content([{"role": "user", "parts": [prompt]}])
    return response.text
