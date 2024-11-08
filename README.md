

# Amazon Product Scraper
This project scrapes product information from a specific category on Amazon India using Beautiful Soup and Requests. It extracts details such as product name, price, rating, and seller name (if available) and saves them to a CSV file.

## Table of Contents
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Output](#output)
- [Notes](#notes)

## Features
- Extracts product details from Amazon’s Electronics category.
- Saves the following details to `amazon_products.csv`:
  - **Product Name**
  - **Price**
  - **Rating**
  - **Seller Name**

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/amazon-product-scraper.git
   cd amazon-product-scraper
   ```

2. **Install Requirements**
   This project requires Python 3 and the following Python libraries:
   - `requests`
   - `beautifulsoup4`
   - `pandas`

   You can install these using:

   ```bash
   pip install -r requirements.txt
   ```

3. **Update User-Agent (Optional)**
   Amazon’s anti-scraping measures may block repeated requests. To avoid this, update the User-Agent in the script if needed.

## Usage

Run the following command in your terminal to execute the script:
```bash
python scraping.py
```

The script will:
1. Send a request to Amazon’s Electronics page.
2. Parse the HTML to extract product details.
3. Save the extracted data in `amazon_products.csv`.

You’ll see a message in the terminal once the data has been saved.

## Output

After running the script, you should see a CSV file named `amazon_products.csv` in the project directory. This file will contain the following columns:
- `Product Name`
- `Price`
- `Rating`
- `Seller Name`

## Notes
- **Amazon Anti-Scraping**: Amazon has strict scraping policies. Use this script responsibly and avoid frequent requests to prevent being blocked.
- **Data Accuracy**: Some data points may be missing or inaccurate if they’re dynamically loaded. The script currently handles only statically loaded data.

Replace `https://github.com/Ajinkya259/Amazon-Product-Scraper` with your actual GitHub repository URL, and add the video link at the end once uploaded.

