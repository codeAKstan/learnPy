import requests
from bs4 import BeautifulSoup
import re
import csv

def scrape_emails(url):
    """
    Scrape emails from a given URL.
    """
    try:
        # Fetch the webpage
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract emails using regex
            emails = set(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', soup.text))
            return emails
        else:
            print(f"Failed to access {url} with status code {response.status_code}")
            return set()
    except Exception as e:
        print(f"An error occurred while accessing {url}: {e}")
        return set()

# List of URLs to scrape (add more URLs as needed)
urls = [
    "https://primecrestfinance.com/",
    "https://axiscapitaltrades.com/",
    "https://www.w3schools.com",
    "my.anitahost.com"
]

# Collect emails from all URLs
all_emails = set()
for url in urls:
    print(f"Scraping {url}...")
    emails = scrape_emails(url)
    all_emails.update(emails)

# Save emails to a CSV file
if all_emails:
    with open("emails.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Email"])  # Write header
        for email in all_emails:
            writer.writerow([email])

    print(f"Emails saved to emails.csv: {len(all_emails)} emails found.")
else:
    print("No emails found.")
