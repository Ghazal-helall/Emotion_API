from fastapi import FastAPI, Request
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware
import os
import requests
import zipfile

app = FastAPI()

# Enable CORS for Flutter frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your domain in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Download and unzip the model from Hugging Face if not present
MODEL_DIR = "Roberta_model"
MODEL_ZIP = "Roberta_model.zip"
HF_MODEL_URL = "https://huggingface.co/GhazalHelal/RoBERTa/resolve/main/Roberta_model.zip"

if not os.path.exists(MODEL_DIR):
    print("Downloading model from Hugging Face...")
    r = requests.get(HF_MODEL_URL)
    with open(MODEL_ZIP, "wb") as f:
        f.write(r.content)

    print("Unzipping model...")
    with zipfile.ZipFile(MODEL_ZIP, "r") as zip_ref:
        zip_ref.extractall(".")

# Load model
classifier = pipeline(
    "text-classification",
    model=MODEL_DIR,
    tokenizer=MODEL_DIR,
    return_all_scores=True
)

label_map = {
    "LABEL_0": "Happy",
    "LABEL_1": "Sad",
    "LABEL_2": "Surprised",
    "LABEL_3": "Angry"
}

@app.post("/predict-emotion")
async def predict(request: Request):
    data = await request.json()
    text = data["text"]
    results = classifier(text)[0]
    top_label = max(results, key=lambda x: x["score"])["label"]
    emotion = label_map.get(top_label, "Unknown")
    return {"emotion": emotion}

# Required entry point for Render
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
