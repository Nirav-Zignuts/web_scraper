import requests
import cloudscraper
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

def get_flipkart_price(product_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    # Construct Flipkart search URL
    search_url = f"https://www.flipkart.com/search?q={product_name}"
    
    response = requests.get(search_url, headers=headers)
    
    # Check if request was successful
    if response.status_code != 200:
        print("Failed to fetch data. Status Code:", response.status_code)
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    product_container = soup.find('a', {'class': 'CGtC98'})
    product_price = soup.find('a', {'class': 'CGtC98'}).find('div', {'class': 'yKfJKb row'}).find('div', {'class': 'Nx9bqj _4b5DiR'}) 
    product_img = soup.find('a', {'class': 'CGtC98'}).find('div', {'class': '_4WELSP'}).find('img', {'class': 'DByuf4'}).get('src')

    print(product_price)
    if product_container:
        details_container = product_container.find('div', {'class': 'yKfJKb row'})
        if details_container:
            product_name_tag = details_container.find('div', {'class': 'Nx9bqj _4b5DiR'})
            specs_list = details_container.find('ul', {'class': 'G4BRas'})

            product_name = product_name_tag.text.strip() if product_name_tag else "Product name not found"
            
            # Fetch all <li> elements inside the <ul>
            specs = [li.text.strip() for li in specs_list.find_all('li')] if specs_list else ["No specifications available"]
            
            return {
                'price':product_price.text,
                "Product Name": product_name,
                "Specifications": specs,
                "URL": search_url,
                "Image_URL": product_img
            }
    
    return {"error": "Product not found on Flipkart"}



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# def get_reliance_price(product_name):
#     # Set up Selenium WebDriver (Headless Chrome)
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")  # Runs in background
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#     # Open the 91Mobiles search page
#     search_url = f"https://www.91mobiles.com/search_page.php?q={product_name.replace(' ', '%20')}&type=all&utm_source=autosuggest"
#     driver.get(search_url)

#     # Wait for JavaScript to load
#     time.sleep(5)  

#     product_data = []

#     try:
#         # Find all product list items
#         product = driver.find_elements(By.CLASS_NAME,"div.content_finder_grid ul.product_listing")
#         print(product)
#         product_items = driver.find_elements(By.CSS_SELECTOR, "ul.product_listing li.finder_snipet_wrap")

#         if not product_items:
#             print("No products found")
#             return {"error": "No products found"}

#         for item in product_items:
#             try:
#                 name_element = item.find_element(By.CSS_SELECTOR, "div.pro_grid_name a.hover_blue_link")
#                 price_element = item.find_element(By.CSS_SELECTOR, "div.pro_grid_price")

#                 product_name = name_element.text.strip()
#                 product_price = price_element.text.strip() if price_element else "Price not found"
#                 product_url = name_element.get_attribute("href")

#                 product_data.append({"name": product_name, "price": product_price, "url": product_url})

#             except Exception as e:
#                 print("Error extracting item:", e)

#     except Exception as e:
#         print("Error:", e)
#         return {"error": "Failed to extract product data"}

#     driver.quit()
#     return product_data

# Example usage
# print(get_reliance_price("iPhone 13"))


def get_reliance_price(product_name):
    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (no browser UI)
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Construct the search URL
    search_url = f"https://www.gadgets360.com/search?searchtext={product_name}"
    
    # search_url = f"https://www.reliancedigital.in/products?q={product_name.replace(' ', '%20')}"
    driver.get(search_url)

    # Wait for the page to load
    time.sleep(2)  # Adjust the sleep time as needed

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Close the WebDriver
    driver.quit()
    print(search_url)
    # print(soup)
    # Find all product containers
    first_product = soup.find('div',{'class' : 'content_block row margin_b30'}).find('div',{'class':'k_prc'}).find('div',{'class':'k_prc_wrp'}).find('ul',{'class':'slider slide1 prc-slider'})
    # product_items = first_product.find_all('li', {'class': 'finder_snipet_wrap'})
    print(first_product)
    pname = first_product.find('div',{'class':'pd-dtl'}).find('a',{'class':'pditem-txt'}).text
    product_img = first_product.find('div',{'class':'pd-img-wrp'}).find('a').find('img').get('src')
    price = first_product.find('div',{'class':'pd-dtl'}).find('span',{'class':'price-txt'}).text
    purlname = first_product.find('div',{'class':'pd-dtl'}).find('a',{'class':'splr-txt'}).text
    purllink = first_product.find('div',{'class':'pd-dtl'}).find('a',{'class':'splr-txt'}).get('href')
    print(pname)
    print(price)
    # print(purl)
    return {
                'price':price,
                "Product Name": pname,
                "URL": search_url,
                "Image_URL": product_img,
                "purlname":purlname,
                "purllink":purllink,
            }
#     if not product_items:
#         print("No products found")
#         return {"error": "No products found"}

#     # Extract product names and prices
#     product_data = []
#     for item in product_items:
#         name_tag = item.find('div', {'class': 'content_info contentheight1'}).find('div',{'class':'pro_grid_name'}).find('a',{'class':'hover_blue_link name gaclick'}).text
#         price_tag = item.find('div', {'class': 'pro_grid_price'})
#         print(name_tag)
#         # product_name = name_tag.text.strip() if name_tag else "Name not found"
#         product_price = price_tag.text.strip() if price_tag else "Price not found"

#         product_data.append({"name": product_name, "price": product_price})

#     print("no data")
#     return {"error": "Product not found on Reliance Digital"}










































# import urllib.parse

# def get_reliance_price(product_name):
#     scraper = cloudscraper.create_scraper()
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#         "Accept-Language": "en-US,en;q=0.9",
#         "Referer": "https://www.google.com/",
#     }
#     search_url = f"https://www.91mobiles.com/search_page.php?q={product_name.replace(' ', '%20')}&type=all&utm_source=autosuggest"
#     response = scraper.get(search_url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     # print(soup)
#     print(search_url)
#     first_product = soup.find('div',{'class' : 'content_finder_grid'}).find('ul',{'class':'product_listing'})
#     product_items = first_product.find_all('li', {'class': 'finder_snipet_wrap'})
#     # print(product_items)
#     if not product_items:
#         print("No products found")
#         return {"error": "No products found"}

#     # Extract product names and prices
#     product_data = []
#     for item in product_items:
#         name_tag = item.find('div', {'class': 'content_info contentheight1'}).find('div',{'class':'pro_grid_name'}).find('a',{'class':'hover_blue_link name gaclick'}).text
#         price_tag = item.find('div', {'class': 'pro_grid_price'})
#         print(name_tag)
#         # product_name = name_tag.text.strip() if name_tag else "Name not found"
#         product_price = price_tag.text.strip() if price_tag else "Price not found"

#         product_data.append({"name": product_name, "price": product_price})

#     print("no data")
#     return {"error": "Product not found on Reliance Digital"}

