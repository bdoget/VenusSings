import pafy

pafy.set_api_key("AIzaSyATQgehc_FxWS8mWyWYxk79_-CrUgiXMIQ")

#query = input("Query: ")
# search_results = "https://www.youtube.com/watch?v=qVSy4O3k3u4"
# if search_results:
#     first_video = search_results[0]
#     url = first_video.watchv_url
#     print("Website URL:", url)
#     video = pafy.new(url)
#     audio_stream = video.getbestaudio()
#     audio_stream.download(filepath="./bin/audio.mp3")
# else:
#     print("No search results found.")

video = pafy.new("https://www.youtube.com/watch?v=qVSy4O3k3u4")
audio_stream = video.getbestaudio()
audio_stream.download(filepath="./bin/audio.mp3")