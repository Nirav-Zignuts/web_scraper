Price Comparison Platform: Develop a web scraping-based price comparison platform where users can compare product prices from different e-commerce websites. Key features:
User registration and login.
Scraping data from Amazon, Flipkart, or any other e-commerce site.

Installation Guide

Requirements
To run this project, you will need to have the following things installed:


Python 3.9
Django 





Installation
1. first clone the repository
go to terminal and do following
Copy 
git clone https://github.com/Nirav-Zignuts/web_scraper.git
cd task_manager_app


2. now Set up a virtual environment

Copy below command 
python3 -m venv task_venv
source task_venv/bin/activate  
3. Install dependencies
Install the required Python packages :

Copy
pip3 install -r requirements.txt

Run the following command to create the  database tables:
Copy
python manage.py migrate

5. Run the using below command server
Now, you can run the Django development server:
Copy
python3 manage.py runserver
Your application will be served at http://127.0.0.1:8000/.


Features
Basic User Authentication System Using OAuth (Provider--> Google ) includes -> registration , login , logout , 
Basic navigation (home page, login, register)
compare product price from diff website


