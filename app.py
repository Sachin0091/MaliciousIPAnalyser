from flask import Flask, render_template, request
import requests
import whois

app = Flask(__name__)

API_KEY = '8001617f2e1e10ea8e7fe523b568306f694a3dfb26e0ec8084ca7cb9e4bc43ac67a960314268d4be'

def get_ip_reputation(ip):
    try:
        url = "https://api.abuseipdb.com/api/v2/check"
        querystring = {
            'ipAddress': ip,
            'maxAgeInDays': '90',
            'verbose': True
        }
        headers = {
            'Accept': 'application/json',
            'Key': API_KEY
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()["data"]

        # Get last 10 reports
        recent_reports = data.get("reports", [])[:10]
        comments = "\n\n".join([
            f"Date: {r.get('reportedAt', '')}\nComment: {r.get('comment', '')}"
            for r in recent_reports
        ]) or "No recent comments."

        return {
            "ip": data["ipAddress"],
            "reputation": "Malicious" if data["abuseConfidenceScore"] > 50 else "Clean",
            "score": data["abuseConfidenceScore"],
            "details": f"{data['countryCode']} - {data['domain'] or 'No domain'} - Reports: {data['totalReports']}",
            "comments": comments
        }

    except Exception as e:
        return {
            "ip": ip,
            "reputation": "Error",
            "score": "-",
            "details": str(e),
            "comments": "-"
        }

def get_whois_data(ip):
    try:
        w = whois.whois(ip)
        return str(w)
    except Exception as e:
        return f"Whois lookup failed: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        ips_raw = request.form.get("ip_addresses", "")
        if ips_raw:
            ip_list = [ip.strip() for ip in ips_raw.splitlines() if ip.strip()]
            for ip in ip_list:
                rep = get_ip_reputation(ip)
                whois_info = get_whois_data(ip)
                rep["whois"] = whois_info
                results.append(rep)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
