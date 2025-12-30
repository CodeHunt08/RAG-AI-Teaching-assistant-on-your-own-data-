# RAG Based AI Teaching Assistant

This is a project where I tried to create an AI that learns from my own study videos.
Instead of using internet knowledge, the model answers questions only from the lectures that I uploaded.

I basically turned video lectures into text, created embeddings, and then used similarity search to get the most relevant chunks. Finally the model generates an answer from that data — like a mini personal tutor.

## What this project does

- I put some lecture videos inside the videos/ folder

- Script converts them to mp3

- Then Whisper converts the audio to text

- The text is broken into small chunks

- I generated embeddings using bge-m3 model in Ollama

- When I ask a question, the program finds related chunks using cosine similarity

- The answer is generated based only on those chunks

### So basically:

Video → Audio → Text → Chunks → Embeddings → Ask → Get Answer

## Tech Stack used in this project

- Python

- Whisper for converting audio to text

- Ollama + BGE-M3 model for embeddings

- NumPy / Pandas for handling data

- scikit-learn (cosine similarity) for matching chunks with query

- Joblib to store embeddings

## Current Status & What I plan to add later

This project is not fully completed yet.
Right now it only takes videos → audio → text → embeddings, but I want to improve it more.
Some things that I still want to work on:

- Add support for PDF, Word files, notes and slides

- Convert those files into chunks the same way as video text

- Improve accuracy by trying a better LLM

- Planning to integrate Gemini/OpenAI API for better quality answers

- Maybe build a simple chat UI so anyone can ask questions easily

So this is kind of a base version. The main RAG pipeline is working, but I will improve it step by step.

# How to use this RAG AI Teaching assistant on your own data 
## Step 1 - Collect your videos
Move all your videos files to the videos folderr

## step 2 - Convert to mp3
Convert all the video files to mp3 by running video_to_mp3.py

## step 3 - Covert mp3 to json
Convert all the mp3 files to json by running mp3_to_json.py

## step 4 - Covert the json files to vectors 
Use the file preprocess_json.py to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

## step 5 - Prompt generation and feeding ro LLM

Read the joblib file and load it into the memory . then create a relevant prompt as per the user query and feed it to the LLM


