import os
import subprocess


files = os.listdir("videos")
for file in files:
    title = file.split("｜")[0]
    number = file.split("#")[1].split(" [")[0]
    subprocess.run(["ffmpeg","-i",f"videos/{file}",f"Audios/{number}_{title}.mp3"])
    print(number,title)



