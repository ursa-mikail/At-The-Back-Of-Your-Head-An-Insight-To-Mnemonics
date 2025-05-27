#!pip install duckduckgo-search pillow requests

import random
import requests
from PIL import Image
from duckduckgo_search import DDGS
from io import BytesIO
import os

def search_and_display_image(query, max_results=10):
    print(f"Searching for: {query}")
    with DDGS() as ddgs:
        results = ddgs.images(query, max_results=max_results)
        image_urls = [result['image'] for result in results]

    if not image_urls:
        print("No images found.")
        return

    selected_url = random.choice(image_urls)
    print(f"Selected Image URL: {selected_url}")

    try:
        response = requests.get(selected_url, timeout=10)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))
        image.show()  # This opens with the default image viewer

        # Optional: Save a temporary local file
        local_filename = "temp_image.jpg"
        image.save(local_filename)
        print(f"Image saved to: {os.path.abspath(local_filename)}")

    except Exception as e:
        print(f"Failed to load/display image: {e}")

# Example usage
target_of_search = "dragon ball"
search_and_display_image(target_of_search)

