import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Amazon page to scrape
url = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"

# Headers to mimic a request from a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5"
}

# Send a GET request to the page
response = requests.get(url, headers=headers)

# Check for a successful request
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Initialize list to hold product data
    products = []
    
    # Find all product containers
    product_containers = soup.find_all('div', {'data-component-type': 's-search-result'})
    
    for container in product_containers:
        # Extract product name
        name_tag = container.h2.a
        name = name_tag.text.strip() if name_tag else None

        # Extract price
        price_tag = container.find('span', {'class': 'a-price-whole'})
        price = price_tag.text.strip().replace(',', '') if price_tag else "N/A"

        # Extract rating
        rating_tag = container.find('span', {'class': 'a-icon-alt'})
        rating = rating_tag.text.split()[0] if rating_tag else "N/A"

        # Extract seller name
        seller_tag = container.find('span', {'class': 'a-size-base-plus'})
        seller = seller_tag.text.strip() if seller_tag else "N/A"

        # Add product details to list
        products.append([name, price, rating, seller])
    
    # Save to CSV
    df = pd.DataFrame(products, columns=['Product Name', 'Price', 'Rating', 'Seller Name'])
    df.to_csv('amazon_products.csv', index=False)
    print("Data saved to amazon_products.csv")
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
