import pafy

pafy.set_api_key("AIzaSyATQgehc_FxWS8mWyWYxk79_-CrUgiXMIQ")

query = input("Query: ")
search_results = pafy.search(query)
if search_results:
    first_video = search_results[0]
    url = first_video.watchv_url
    print("Website URL:", url)
    video = pafy.new(url)
    audio_stream = video.getbestaudio()
    audio_stream.download(filepath="./bin/audio.mp3")
else:
    print("No search results found.")
