🛡 OFAC "Recent Actions" Web Scraper
A lightweight Python script that automatically scrapes and parses the latest actions from the U.S. Treasury OFAC Recent Actions page. Built to support analysts, compliance teams, and researchers who need quick, structured access to constantly changing sanctions data.

🔍 Why This Project Matters
In compliance, sanctions, and risk management, staying up-to-date with regulatory changes is critical. But OFAC updates are often buried in HTML pages or PDFs, making manual tracking time-consuming and error-prone. This script bridges that gap—turning raw public data into structured CSV output for faster analysis and alerting.

⚙️ Features
✅ Scrapes the 10 most recent entries from the OFAC “Recent Actions” page

✅ Extracts:

Date

Title

Category

Source Link

✅ Outputs clean CSV for downstream analysis

✅ Built using Selenium

✅ Lightweight, readable, and easy to customize

📁 Sample Output
javascript
Copy
Edit
| Date       | Title                                          | Category         | Link                                       |
|------------|------------------------------------------------|------------------|--------------------------------------------|
| 2025-06-25 | Russia-related Designations                    | Sanctions Update | https://home.treasury.gov/...              |
| 2025-06-24 | Counter Narcotics Designations                 | Enforcement      | https://home.treasury.gov/...              |
🛠️ Setup Instructions
🔧 Requirements
Python 3.8+

Chrome + ChromeDriver

pip install:

bash
Copy
Edit
pip install -r requirements.txt
📦 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/ofac-scraper.git
cd ofac-scraper
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the script:

bash
Copy
Edit
python ofac_scraper.py
Check the generated ofac_recent_actions.csv file.

🚧 Roadmap
 Filter by region or keyword (e.g., Russia, Iran)

 Add alerting (email, webhook, or Slack integration)

 Export to SQLite or Postgres

 Scrapers for related sites (FinCEN, FATF, UN sanctions)

🤝 Contributing
Pull requests and forks are welcome! If you'd like to suggest a new feature or improvement, open an issue.

🧠 Author
Michael Hernandez
LinkedIn | GitHub

