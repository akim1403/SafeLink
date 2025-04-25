# 🔐 SafeLink – Scam Website Detector

SafeLink is a Python-based tool that helps detect potentially scammy or phishing websites by analyzing their content and comparing them to a list of trusted domains for well-known companies.

It performs the following:
- Loads the given website in a headless browser.
- Extracts and parses the website content using BeautifulSoup.
- Looks for mentions of major company names (e.g., PayPal, ATO, Netflix).
- Checks whether the website's base URL matches a list of official domains for those companies.
- Flags mismatches as potentially scam websites.

---

## 🚀 Features

- ✅ Detects scam attempts mimicking trusted organizations.
- 🧠 Parses full webpage content with JavaScript support using Selenium.
- 🔒 Uses headless Chrome with anti-bot features to avoid detection.
- 🔎 Matches detected company names to known-safe base URLs.
- 💡 Supports a wide range of industries: government, banking, e-commerce, crypto, healthcare, etc.

---

## 📦 Requirements

Make sure you have the following installed:

- Python 3.x
- Google Chrome
- ChromeDriver (make sure it's compatible with your Chrome version)

Install required Python libraries:

```bash
pip install selenium beautifulsoup4

