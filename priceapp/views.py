from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .scrapping import get_flipkart_price,get_reliance_price
# Create your views here.
def home(request):
    return render(request,'home.html')

def login_user(request):
    if request.user.is_authenticated:
        redirect('home')
    return render(request,'login.html')
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')
# @login_required
# def search(request):
#     if request.method == "POST":
#         search = request.POST['search']
#         if search == "":
#             return redirect('search')
#         a_price = get_flipkart_price(search)
#         a_prices = get_reliance_price(search)
#         print(a_price)
#         return render(request,'search.html',{'a_price':a_price,'name':search})
#     return render(request,'search.html')
# #
# 
@login_required
def search(request):
    if request.method == "POST":
        search_query = request.POST.get('search', '').strip()
        if not search_query:
            return render(request, 'search.html')

        # Fetch product data from multiple e-commerce platforms
        flipkart_data = get_flipkart_price(search_query)
        reliance_data = get_reliance_price(search_query)  # Another scraper function
        print(flipkart_data)
        print(flipkart_data.get("Image_URL", ""))
        # Pass the data to the template
        formatted_flipkart = {
            "name": flipkart_data.get("Product Name", "N/A"),  # Fix key
            "price": flipkart_data.get("price", "N/A"),
            "specifications": flipkart_data.get("Specifications", []),
            "url": flipkart_data.get("URL", "#"),
            "image_url": flipkart_data.get("Image_URL", ""),  # Ensure image URL is provided
        }

        formatted_reliance = {
            "name": reliance_data.get("Product Name", "N/A"),
            "price": reliance_data.get("price", "N/A"),
            "specifications": reliance_data.get("Specifications", []),
            "url": reliance_data.get("URL", "#"),
            "image_url": reliance_data.get("Image_URL", ""),
             
        }

        return render(request, 'search.html', {
            'flipkart': formatted_flipkart,
            'reliance': formatted_reliance,
            'name': search_query
        })

    return render(request, 'search.html')
headers =({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36' ,'Accept-Language': 'en-US,en;q=0.8'})
