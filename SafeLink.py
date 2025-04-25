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

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re


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


url = input("Enter website to check: ")

# Gets the Base URL
stripped_url = "/".join(url.split("/")[:3])

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in background
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

options.add_argument('--log-level=3')  # Suppress console logs
options.add_argument('--disable-logging')  # Disable ChromeDriver logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Hide DevTools logs

# Anti-bot evasion
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-features=FingerprintingClientConfigurationRector')

# GPU fixes
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')


options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)



try:
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    found_comp = False

    for scam_comp in scam_companies_domains:
        if re.search(rf'\b{re.escape(scam_comp.lower())}\b', soup.get_text().lower()):
            print(f"Found the company {scam_comp} in page content")
            print("Checking website link against safe website domains")

            # Change: Check if stripped_url is in the list
            if stripped_url not in scam_companies_domains[scam_comp]:  
                print("This is a Scam Website!!!!!!!!!!!")
            else:
                print("This is a Safe Website")
            
            found_comp = True
            break
    
    if not found_comp:
        print("Did not find any major company names")
        print("Cannot check if it is a scam website")
        
finally:
    driver.quit()