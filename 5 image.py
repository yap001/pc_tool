import requests
import random
from datetime import datetime, timedelta

# Function to grab random images from Google Images
def grab_random_images(query, num_images):
    # Insert your Google Images API key here
    api_key = "YOUR_API_KEY"
    # Set the search query and number of images to fetch
    search_query = query
    num_images = num_images

    # API request URL
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx=YOUR_CX_CODE&q={search_query}&searchType=image&num={num_images}"

    try:
        response = requests.get(url)
        data = response.json()
        # Parse the response to extract image URLs
        image_urls = [item['link'] for item in data['items']]
        return image_urls
    except requests.exceptions.RequestException as e:
        print("Error: ", e)

# Function to grab images every Sunday and Tuesday
def grab_images_on_schedule():
    # Define the search query and number of images
    search_query = "YOUR_SEARCH_QUERY"
    num_images = 5

    # Get the current date
    current_date = datetime.now().date()

    # Check if it's Sunday or Tuesday
    if current_date.strftime("%A") == "Sunday" or current_date.strftime("%A") == "Tuesday":
        # Grab random images
        image_urls = grab_random_images(search_query, num_images)
        print("Random Images:")
        for url in image_urls:
            print(url)
    else:
        print("Today is not Sunday or Tuesday.")

# Call the function to grab images on schedule
grab_images_on_schedule()
