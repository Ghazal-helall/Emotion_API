#!/bin/bash
unzip -o Roberta_model.zip
uvicorn main:app --host 0.0.0.0 --port 10000
