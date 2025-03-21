import requests
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

# Example usage


# def get_flipkart_price(product_name):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#         "Accept-Language": "en-US,en;q=0.9",
#     }

#     # Construct Flipkart search URL
#     search_url = f"https://www.flipkart.com/search?q={product_name}"
    
#     response = requests.get(search_url, headers=headers)
    
#     # Check if request was successful
#     if response.status_code != 200:
#         print("Failed to fetch data. Status Code:", response.status_code)
#         return None
#     print("yes")
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Locate first product container
#     dta= soup.find('a', {'class': 'CGtC98'}).find('div', {'class': 'yKfJKb row'}).find('div',{'class':'_6NESgJ'}).find('ul',{'class':'G4BRas'}).find('li',{'class':'J+igdf'})
#     print(dta.text)
#     product = soup.find('a', {'class': 'CGtC98'}).find('div', {'class': 'yKfJKb row'}).find('div', {'class': 'Nx9bqj _4b5DiR'})  # Find the first product container
    
#     if product:
#         # title_tag = product.find('a', {'class': 'IRpwTa'}) or product.find('a', {'class': 's1Q9rs'})
#         # price_tag = product.find('div', {'class': '_30jeq3'})
#         print(product.text)
#         return product.text,search_url
#         # if title_tag and price_tag:
#         #     title = title_tag.text.strip()
#         #     price = price_tag.text.replace('₹', '').replace(',', '').strip()
#         #     return title, float(price)
    
#     return None

import urllib.parse

def get_reliance_price(product_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    search_url = f"https://www.reliancedigital.in/search?q={product_name.replace(' ', '%20')}"
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    print(search_url)
    first_product = soup.find("a", class_="sp__name")
    if first_product:
        product_url = "https://www.reliancedigital.in" + first_product["href"]
        response = requests.get(product_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        title = soup.find("h1", class_="pdp__title")
        price = soup.find("span", class_="pdp__offerPrice")
        
        if title and price:
            print({"title": title.text.strip(), "price": price.text.strip(), "url": product_url})
    print("no data")
    return {"error": "Product not found on Reliance Digital"}

