import requests
from bs4 import BeautifulSoup
import time

# Function to scrape the webpage and extract the titles
def scrape_titles():
    url = "https://www.aljazeera.com/tag/ukraine-russia-crisis/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.find_all(class_="u-clickable-card__link")[:5]  # Get the first 5 titles
    return [title.text for title in titles]

# Function to display the titles and countdown timer
def display_titles(titles):
    print("Scraped Titles:")
    for title in titles:
        print("- " + title)
    print()

# Function to display the countdown timer
def display_timer(seconds):
    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        time_format = f"{minutes:02d}:{sec:02d}"
        print(f"Next scrape in: {time_format}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\n\n")

# Main loop
while True:
    titles = scrape_titles()
    display_titles(titles)
    display_timer(60 * 24)  # 24 hours interval
