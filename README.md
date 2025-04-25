# 🔐 SafeLink – Scam Website Detector

SafeLink is a Python-based tool that helps detect potentially scammy or phishing websites by analyzing their content and comparing them to a list of trusted domains for well-known companies.

It performs the following:
- Loads the given website in a headless browser.
- Extracts and parses the website content using BeautifulSoup.
- Looks for mentions of major company names (e.g., PayPal, ATO, Netflix).
- Checks whether the website's base URL matches a list of official domains for those companies.
- Flags mismatches as potentially scam websites.

---

An example video of this program working can be found through this link:
https://youtu.be/iuc3TkIYI08

## 🚀 Features

- ✅ **Detects scam attempts mimicking trusted organizations.**
- 🧠 **Parses full webpage content with JavaScript support using Selenium.**
- 🔒 **Uses headless Chrome with anti-bot features to avoid detection.**
- 🔎 **Matches detected company names to known-safe base URLs.**
- 💡 **Supports a wide range of industries:** government, banking, e-commerce, crypto, healthcare, etc.

---

## 📦 Requirements

Make sure you have the following installed:

- Python 3.x
- Google Chrome
- ChromeDriver (make sure it's compatible with your Chrome version)

Install required Python libraries:

```bash
pip install selenium beautifulsoup4
```

---

## 🛠️ How to Use

1. Clone the repository or download the script:

    ```bash
    git clone https://github.com/yourusername/safelink.git
    cd safelink
    ```

2. Run the script:

    ```bash
    python SafeLink.py
    ```

3. Input a URL when prompted:

    ```
    Enter website to check: http://example.com
    ```

4. The output will indicate whether the site is safe or potentially a scam:

    ```
    Found the company PayPal in page content
    Checking website link against safe website domains
    This is a Scam Website!!!!!!!!!!!
    ```

---

## 📋 How It Works

1. User inputs a URL.
2. The tool loads the page in a headless Chrome browser.
3. Webpage content is scraped using BeautifulSoup.
4. Each major company name is checked against the text content.
5. If a company is mentioned, the base URL is compared to that company's official domain(s).
6. If mismatched, the site is flagged as suspicious.

---

## 🧠 Supported Companies

The script currently supports a wide range of entities, including:

- **Australian government services**: ATO, myGov, Centrelink
- **Major banks**: ANZ, Westpac, Commonwealth, NAB
- **Retailers**: Amazon, eBay, Facebook Marketplace
- **Delivery services**: Australia Post, DHL, FedEx
- **Streaming and subscription platforms**: Netflix, Disney+, Spotify
- **Investment & crypto platforms**: Binance, CoinSpot, ASX
- **Healthcare and insurance providers**: Bupa, Medibank
- **Job portals, tech companies, charities**, and more.

---

## ⚠️ Disclaimer

This tool provides basic heuristic checking and should not be considered a comprehensive phishing detection system. Always verify suspicious websites through official channels.

---

