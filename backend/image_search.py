import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

def image_search(query):
    load_dotenv()
    api_key = os.getenv("SERPAPI_KEY")

    params = {
        "q": query,
        "tbm": "isch",
        "api_key": api_key,
        "safe": "active",
        "imgsz": "large"
    }

    search = GoogleSearch(params)
    response = search.get_dict()
    image_links = []
    
    if "images_results" in response:
        for result in response["images_results"]:
            image_url = result["original"]
            image_links.append(image_url)
    else:
        print("No image results found.")
    return image_links

def main():
    api_key = os.getenv("GOOGLE_KEY")
    q = input("Enter your query\n")
    for x in image_search(q):
        print(x)

if __name__ == "__main__":
    main()
