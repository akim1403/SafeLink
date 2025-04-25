# from bs4 import BeautifulSoup
# from urllib.request import urlopen

# #url = "https://www.paypal.com/au/home"
# url = "http://olympus.realpython.org/profiles/dionysus"
# page = urlopen(url)
# html = page.read().decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")
# print(soup.get_text())
# #print(soup.find_all("img"))
# #print(soup.prettify())
# if "paypal" in soup.get_text().lower():
#     print("Found 'paypal' in page content (case-insensitive)")
# else:
#     print("Did not find the word paypal")

# Import required modules for browser automation and HTML parsing
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re  # For regular expression matching

# A dictionary mapping company names to their official domain URLs
# This is used to detect scam websites pretending to be from these companies
scam_companies_domains = {
    # Government Agencies
    "Australian Taxation Office (ATO)": ["https://www.ato.gov"],
    "myGov": ["https://login.my.gov.au", "https://my.gov.au"],
    "Services Australia": ["https://www.servicesaustralia.gov"],
    "Centrelink": ["https://www.servicesaustralia.gov/centrelink"],

    # Banks and Financial Institutions
    "Commonwealth Bank": ["https://www.commbank.com"],
    "ANZ": ["https://www.anz.com"],
    "Westpac": ["https://www.westpac.com"],
    "NAB": ["https://www.nab.com"],
    "HSBC": ["https://www.hsbc.com"],
    "PayPal": ["https://www.paypal.com"],
    
    # Delivery and Logistics
    "Australia Post": ["https://auspost.com"],
    "DHL": ["https://www.dhl.com"],
    "FedEx": ["https://www.fedex.com"],
    "Toll Group": ["https://www.tollgroup.com"],
    "Linkt (toll road scams)": ["https://www.linkt.com"],

    # Telecommunications
    "Telstra": ["https://www.telstra.com"],
    "Optus": ["https://www.optus.com"],
    "Vodafone": ["https://www.vodafone.com"],

    # Online Retailers and Marketplaces
    "Amazon": ["https://www.amazon.com"],
    "eBay": ["https://www.ebay.com"],
    "Facebook Marketplace": ["https://www.facebook.com/marketplace"],
    "Gumtree": ["https://www.gumtree.com"],

    # Cryptocurrency and Investment
    "Binance": ["https://www.binance.com"],
    "CoinSpot": ["https://www.coinspot.com"],
    "Crypto.com": ["https://crypto.com"],
    "ASX": ["https://www.asx.com"],
    "SelfWealth": ["https://www.selfwealth.com"],
    
    # Energy and Utility Providers
    "AGL": ["https://www.agl.com"],
    "Origin Energy": ["https://www.originenergy.com"],
    "EnergyAustralia": ["https://www.energyaustralia.com"],
    
    # Insurance and Superannuation
    "Medibank": ["https://www.medibank.com"],
    "Bupa": ["https://www.bupa.com"],
    "AustralianSuper": ["https://www.australiansuper.com"],
    "Hostplus": ["https://www.hostplus.com"],
    
    # Travel and Accommodation
    "Qantas": ["https://www.qantas.com"],
    "Virgin Australia": ["https://www.virginaustralia.com"],
    "Airbnb": ["https://www.airbnb.com"],
    "Booking.com": ["https://www.booking.com"],
    "Expedia": ["https://www.expedia.com"],
    
    # Subscription and Streaming Services
    "Netflix": ["https://www.netflix.com"],
    "Stan": ["https://www.stan.com"],
    "Spotify": ["https://www.spotify.com"],
    "Apple Music": ["https://music.apple.com"],
    "Disney+": ["https://www.disneyplus.com"],
    
    # Job and Recruitment Scams
    "SEEK": ["https://www.seek.com"],
    "LinkedIn": ["https://www.linkedin.com"],
    "Indeed": ["https://www.indeed.com"],

    # Tech Support and Software
    "Microsoft": ["https://www.microsoft.com"],
    "Apple": ["https://www.apple.com"],
    "Google": ["https://www.google.com"],
    "Norton Antivirus": ["https://www.norton.com"],
    "McAfee": ["https://www.mcafee.com"],
    
    # Charities and Donations
    "Red Cross": ["https://www.redcross.org"],
    "Salvation Army": ["https://www.salvationarmy.org"],
    "Cancer Council": ["https://www.cancer.org"],
    "RSPCA": ["https://www.rspca.org"]
}

# Prompt user to input the website URL to be checked
url = input("Enter website to check: ")

# Extract the base URL (protocol + domain) to match against known safe domains
stripped_url = "/".join(url.split("/")[:3])

# Set up Chrome browser options for Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run browser in the background
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
)

# Suppress logs for a cleaner output
options.add_argument('--log-level=3')
options.add_argument('--disable-logging')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Evade detection as an automated browser
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Prevent GPU-related crashes or unnecessary usage
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')

try:
    # Launch headless Chrome browser
    driver = webdriver.Chrome(options=options)

    # Load the target URL
    driver.get(url)

    # Scroll down to trigger loading of dynamic content (useful for JS-heavy pages)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Spoof the webdriver property to help bypass basic anti-bot detection
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    # Parse the fully loaded HTML page using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    found_comp = False  # Track if any known company name is found in page content

    # Loop through known company names
    for scam_comp in scam_companies_domains:
        # Search for the company name in the page's text content (case-insensitive)
        if re.search(rf'\b{re.escape(scam_comp.lower())}\b', soup.get_text().lower()):
            print(f"Found the company {scam_comp} in page content")
            print("Checking website link against safe website domains")

            # Check if the base URL is NOT in the list of official domains for that company
            if stripped_url not in scam_companies_domains[scam_comp]:
                print("This is a Scam Website!!!!!!!!!!!")
            else:
                print("This is a Safe Website")

            found_comp = True
            break  # Stop checking once a company has been found

    # If no company name is found in the page content
    if not found_comp:
        print("Did not find any major company names")
        print("Cannot check if it is a scam website")

# Ensure the browser closes no matter what happens
finally:
    driver.quit()
