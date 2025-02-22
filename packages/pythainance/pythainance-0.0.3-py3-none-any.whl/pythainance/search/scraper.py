from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def scrape_url(url):
    """
    Scrape JavaScript-rendered content using Playwright and save to a file.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until='networkidle')
        content = page.content()
        browser.close()
        
        soup = BeautifulSoup(content, 'html.parser')
        text_content = soup.get_text()
        
        with open("dataset/scraped_content.txt", "w", encoding="utf-8") as file:
            file.write(text_content)
        
        return text_content
    