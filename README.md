Malicious IP Analyzer
A lightweight Flask app to check multiple IP addresses at once using the AbuseIPDB API. It also provides WHOIS info for extra context.

🔧 Setup
Clone the repo and move into the project folder:

git clone https://github.com/yourusername/malicious-ip-analyzer.git
cd malicious-ip-analyzer
Create and activate a virtual environment:

python3 -m venv venv
source ./venv/bin/activate
Install dependencies:

pip install flask requests python-whois

🔑 API Key
1.	Create a free account on AbuseIPDB.
2.	Get your API key.
3.	Add it in your environment:



export ABUSEIPDB_API_KEY="your_api_key_here"
Windows (PowerShell):

$env:ABUSEIPDB_API_KEY="your_api_key_here"
⚠️ If the app stops working:
•	Your API key may have expired or hit its daily limit.
•	Generate a new key on AbuseIPDB and replace it.

▶️ Run the App

python app.py
The app will start on: 👉 http://127.0.0.1:5000
Paste a list of IPs (one per line) and get:
•	Abuse confidence scores from AbuseIPDB
•	WHOIS info for each IP

⚠️ Note
•	This tool is for educational and research purposes only.
•	Do not use it for malicious purposes.


Linux/macOS:<img width="757" height="388" alt="Screenshot 2025-08-29 at 3 37 59 pm" src="https://github.com/user-attachments/assets/0ce99653-60cf-4e95-a19d-458b2ceb70bf" />

