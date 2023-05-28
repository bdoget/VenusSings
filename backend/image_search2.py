from google_images_search import GoogleImagesSearch
import os
from dotenv import load_dotenv

def get_image_results(query, num_results):
    # Set up the Google Images Search API
    load_dotenv()
    api_key = os.getenv("GOOGLE_KEY")
    cv_key = os.getenv("GOOGLE_CX_KEY")


    gis = GoogleImagesSearch(api_key, cv_key)

    # Search for images
    search_params = {
        'q': query,
        'num': num_results,
        'safe': 'high',
        'fileType': 'jpg|png',
        'imgSize': 'large',
    }

    gis.search(search_params=search_params)
    # Get the image URLs from the results
    image_urls = []
    for image in gis.results():
        image_urls.append(image.url)

    return image_urls



def main():

    query = input("Enter your query\n")
    num_results = 10
    image_results = get_image_results(query, num_results)

    # Print the image URLs
    for url in image_results:
        print(url)

if __name__ == "__main__":
    main() 

