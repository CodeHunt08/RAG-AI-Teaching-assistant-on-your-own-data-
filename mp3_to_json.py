import whisper
import os
import json 

model = whisper.load_model("large-v2")

def convert_to_text(file):
    r = model.transcribe(audio=f"audios/{file}",
                                language="hi",
                                task="translate",
                                word_timestamps=False)
   
    print(r)
    return r

audios = os.listdir("audio")



for file in audios:
    title = file.split(".mp3")[0].split("_")[1]
    number = file.split("_")[0]
    r = model.transcribe(audio=f"audio/{file}",
                                language="hi",
                                task="translate",
                                word_timestamps=False)
    chunks = []
    for segment in r['segments']:
        chunk = {
            "number":number,
            "title":title,
            "start":segment['start'],
            "end":segment['end'],
            "text":segment['text']
        }
        chunks.append(chunk)

    print(number,title)
    with open(f"json/{number}_{title}","w") as f:
        json.dump({"chunks":chunk,"text":r['text']},f)

