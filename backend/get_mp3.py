from pytube import YouTube
import os
import ffmpy

link = "https://www.youtube.com/watch?v=HuQ0ni6AlrU"

yt = YouTube(link)

downloader = yt.streams.filter(progressive = True, file_extension = "mp4").first()

test = downloader.download(output_path = "./bin", filename = "video.mp4")
ff =ffmpy.FFmpeg(inputs={test: None},outputs={'./bin/audio.mp3': None})
ff.run()