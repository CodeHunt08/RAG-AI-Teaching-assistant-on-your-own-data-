import requests
import os
import json
import pandas as pd
import joblib

def create_embeddings(text):
    r = requests.post("http://localhost:11434/api/embed",json={
        "model":"bge-m3",
        "input":text
    })

    embeddings = r.json()["embeddings"]
    
    return embeddings


jsons = os.listdir("jsons")
my_dicts = []
print(jsons)
for json_file in jsons:
    with open(f"jsons/{json_file}","r") as f:
        content = json.load(f)


    embeddings = create_embeddings([c["text"] for c in content["chunks"]])

    for i , item in enumerate(content["chunks"]):
        item["chunk_id"] = i
        item["embedding"] = embeddings[i]
        my_dicts.append(item)


df = pd.DataFrame.from_records(my_dicts)
joblib.dump(df, "embeddings.joblib")