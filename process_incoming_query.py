import pandas as pd
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import requests


def create_embbeding(text_list):

    r = requests.post("http://localhost:11434/api/embed",json={
            "model":"bge-m3",
            "input":text_list
        })

    embedding = r.json()['embeddings']
    return embedding


def inference(prompt):
    print("Thinking ......")
    r = requests.post("http://localhost:11434/api/generate",json={
            "model":"llama3.2",
            "prompt":prompt,
            "stream":False

        })
    response = r.json()
    return response

df = joblib.load("embeddings.joblib")

incoming_query = input("Enter the query: -") 
question_embedding = create_embbeding([incoming_query])[0]#here we convert that question into embeddings by passing the question in list beacuse our function takes the argument in list it returns the list of list so for only one list we write we want index 0 values that is single list of embeddings not list of list


similarities = cosine_similarity(np.vstack(df['embedding']),[question_embedding]).flatten()
# print(similarities)
print(similarities)
top_results = 5
max_indx = similarities.argsort()[::-1][0:top_results] # argsort will return the index of the sorted array in ascending order it means our highest matching is at last so we use [::-1] to reverse the order to descending order and we want only top 3 similar chunks so we use [0:3]

new_df = df.loc[max_indx]
print(new_df[["Title","Text"]])

prompt = f'''
i am teachig the python course. Here are videos subtitle chunks containing video title, video number ,start time in seconds , end time in secomnds, the text at that time : 

{new_df[["title","number","start","end","text"]].to_json(orient ="records")}#we use orient = records to convert the dataframe into the list of dictionary

--------------------------------------
"{incoming_query}" 
User asked this question related to the video chunks , you have to answer in human way (dont mention the above format , its just for you ) where and how much content is taught in which video (int which video and at what timestamp) and quide the user to go to that particular video . If user asks unrelated question , tell him that you can only answer questions related to the course only 
'''
with open("prompt.txt","w") as f:
    f.write(prompt)

response = inference(prompt)["response"]
print(response)

with open("response.txt","w") as f:
    f.write(response)
