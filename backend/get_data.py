from get_lyrics import get_lyrics
# from image_search import image_search
from image_search2 import get_image_results
from spotify_id import search_tracks
import random, math
import json, os

def get_data(track_id):
    """
        Attaches images based on lyrics to the lyrics array
    """
    try:
        data = get_lyrics(track_id)
        for interval in data:
            interval['image'] = get_image_results(interval['words'])[0]
            break
        return data
    except Exception as e:
        return "Oops"

def get_data2(track_id,max_images,query="",additional_query=""):
    """
        get lyrics from track_id, get images from lyrics, cache the links into file
    """

    data = None
    try:
        data = get_lyrics(track_id)
    except:
        return "Oops"

    n = len(data)
    if n < max_images:
        for idx,interval in enumerate(data):
            temp = interval['words'] + f" {query} {additional_query}"
            print(temp)
            interval['image'] = get_image_results(temp,1)[0]
            interval['id'] = idx
            # interval['transition'] = True
            break
    elif max_images <= 0:
        for idx,interval in enumerate(data):
            interval['image'] = "https://arctype.com/blog/content/images/2021/04/NULL.jpg"
            interval['id'] = idx
            # interval['transition'] = True
    else:
        remaining_imgs = max_images
        last_image = []
        for idx, interval in enumerate(data):

            chance = random.randint(1, math.ceil((n+1)/max_images))

            if last_image == [] and (chance == 1 or remaining_imgs > 0):
                temp = interval['words'] + f" {query} {additional_query}"
                print(temp)
                last_image = get_image_results(temp,n-idx)
                remaining_imgs -= 1

            interval['image'] = last_image[0]
            interval['id'] = idx
            # interval['transition'] = True
            last_image.pop(0)
        
    return data
    
def cacheQuery(query, data):
    """
    Cache the query and the data into a file
    """
    # Create a file in the "subtitle" folder named "query" and store the data in it
    filename = f"Subtitle/{query}.txt"
    with open(filename, "w") as file:
        json.dump(data, file)

def cleanQuery(query):
    return query.lower().replace(" ", "")

def get_data3(query,max_images=5):
    query = cleanQuery(query)
    # if file exists, return the data
    filename = f"Subtitle/{query}.txt"
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            return json.load(file)
    
    trackID = search_tracks(query)
    data = get_data2(trackID,max_images,query)
    cacheQuery(query, data)
    return data

if __name__ == "__main__":

    # print(get_data("11dFghVXANMlKmJXsNCbNl"))
    # print(len(get_lyrics("11dFghVXANMlKmJXsNCbNl")))

    # cacheQuery("test", get_lyrics("11dFghVXANMlKmJXsNCbNl"))
    get_data3("faded-alan walker",2)
    pass
