
from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.veeam.com/")
        page.click("xpath=//button[contains(text(), 'Produc')]")
        assert "Veeam" in page.title()
        browser.close()
        


if __name__ == "__main__":
    run_test()
    print("Done !")