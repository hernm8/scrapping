import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_ofac_recent_actions(save_csv=True, csv_path="ofac_recent_actions.csv"):
    # 1️⃣ Configure headless Chrome
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    # 🛠️ If Chrome isn't in default path, uncomment & update:
    # options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    # 2️⃣ Install & launch ChromeDriver automatically
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        url = "https://home.treasury.gov/policy-issues/financial-sanctions/recent-actions"
        print("🌐 Loading OFAC Recent Actions page…")
        driver.get(url)
        time.sleep(5)  # allow JS to populate entries

        # 3️⃣ Find entries
        rows = driver.find_elements("css selector", ".view-content .views-row")
        print(f"✅ Found {len(rows)} entries")

        # 4️⃣ Parse entries
        data = []
        for row in rows:
            title_elem = row.find_element("css selector", ".font-sans-lg a")
            title = title_elem.text.strip()
            link = title_elem.get_attribute("href")
            meta = row.find_element("css selector", ".font-sans-2xs").text.strip()
            
            date_str, _, category = meta.partition(" -")
            date = pd.to_datetime(date_str.strip(), errors="coerce")
            category = category.strip(" -\n ")
            
            data.append({"Date": date, "Title": title, "Category": category, "Link": link})

        # 5️⃣ Build DataFrame
        df = pd.DataFrame(data)
        print("🧾 Latest entries:\n", df)

        # 6️⃣ (Optional) Save to CSV
        if save_csv:
            df.to_csv(csv_path, index=False)
            print(f"✅ Data saved to '{csv_path}'")

        return df

    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_ofac_recent_actions()
