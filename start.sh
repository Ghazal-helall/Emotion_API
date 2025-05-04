#!/bin/bash

# Download only if not already present
if [ ! -f Roberta_model.zip ]; then
    echo "Downloading model from Hugging Face..."
    wget https://huggingface.co/GhazalHelal/RoBERTa/resolve/main/Roberta_model.zip
fi

# Unzip only if not already extracted
if [ ! -d Roberta_model ]; then
    echo "Unzipping model..."
    unzip Roberta_model.zip
fi

echo "Starting server..."
uvicorn main:app --host 0.0.0.0 --port $PORT
