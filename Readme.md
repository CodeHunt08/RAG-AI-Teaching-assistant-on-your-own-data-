# How to use this RAG AI Teaching assistant on your own data 
## Step 1 - Collect your videos
Move all your videos files to the videos folder

## step 2 - Convert to mp3
Convert all the video files to mp3 by running video_to_mp3.py

## step 3 - Covert mp3 to json
Convert all the mp3 files to json by running mp3_to_json.py

## step 4 - Covert the json files to vectors 
Use the file preprocess_json.py to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

## step 5 - Prompt generation and feeding ro LLM

Read the joblib file and load it into the memory . then create a relevant prompt as per the user query and feed it to the LLM
