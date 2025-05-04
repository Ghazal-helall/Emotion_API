#!/bin/bash

echo "Downloading model from Hugging Face..."
wget https://huggingface.co/GhazalHelal/RoBERTa/resolve/main/Roberta_model.zip

echo "Unzipping model..."
unzip Roberta_model.zip

echo "Starting server..."
uvicorn main:app --host 0.0.0.0 --port $PORT
