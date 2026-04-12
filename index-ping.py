import datetime
import random
import requests
import json
import os

# --- 1. CONFIGURATION ---
BASE_URL = "https://brightlane.github.io/maxlen-approval-fast"
INDEXNOW_KEY = "817c039b282227a69abd9cfa9f9b87f2"
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949096598005765&atid=MaxlendWeb"
LOGO_PATH = "images/Mr-owl-with-brown-eyes.jpg"

PAGES_TO_GENERATE = {
    "index.html": "MaxLend Approval Fast",
    "instant-funding.html": "Instant Funding 2026",
    "emergency-loans.html": "Emergency Cash Advance",
    "tribal-lending-guide.html": "Tribal Loan Guide",
    "apply-now.html": "Apply at MaxLend",
    "bad-credit-approval.html": "Bad Credit Approval",
    "same-day-deposit.html": "Same Day Deposit",
    "privacy.html": "Privacy & Legal",
    "contact.html": "Contact Support",
    "blog.html": "Financial Success Blog"
}

STATES = ["Texas", "Florida", "Ohio", "California", "Illinois", "Georgia", "Michigan", "Virginia"]

# --- 2. CONTENT GENERATOR ---
def generate_3000_words(keyword, state):
    today = datetime.date.today().strftime("%B %d, 2026")
    content = f"<h2>{keyword} for {state} Residents - Updated {today}</h2>"
    sections = ["Why Choose MaxLend", "Tribal Sovereignty Benefits", "Fast Approval Process"]
    for section in sections:
        content += f"<h3>{section}</h3><p>" + (f"In {state}, {keyword} seekers choose MaxLend for speed and transparency. ") * 35 + "</p>"
    return content

# --- 3. THE MASTER TEMPLATE ---
def get_template(title, keyword, body):
    today_long = datetime.date.today().strftime("%B %d, 2026")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{ --primary: #002D62; --secondary: #D4AF37; }}
        body {{ font-family: sans-serif; margin: 0; background: #f4f7f9; color: #333; }}
        header {{ background: var(--primary); color: white; padding: 40px; text-align: center; border-bottom: 5px solid var(--secondary); }}
        .logo {{ height: 100px; border-radius: 5px; background: white; padding: 5px; }}
        .cta-btn {{ display: inline-block; background: #c00; color: white; padding: 15px 30px; text-decoration: none; border-radius: 50px; font-weight: bold; margin: 20px 0; }}
        .container {{ max-width: 800px; margin: 20px auto; padding: 20px; background: white; }}
        footer {{ background: #111; color: #ccc; padding: 40px 20px; font-size: 0.7rem; text-align: center; }}
    </style>
    <script>
        document.addEventListener("mouseleave", function(e) {{
            if (e.clientY < 0) {{ window.open("{AFFILIATE_URL}", "_blank"); }}
        }});
    </script>
</head>
<body>
    <header>
        <img src="{LOGO_PATH}" class="logo">
        <h1>{keyword}</h1>
        <a href="{AFFILIATE_URL}" class="cta-btn">APPLY NOW</a>
    </header>
    <div class="container">{body}</div>
    <footer>
        <p>Official MaxLend Affiliate | 1-877-936-4336 | 145 Tribal Business Council Rd, Mandaree, ND 58757</p>
        <p>Last Updated: {today_long}</p>
    </footer>
</body>
</html>"""

# --- 4. EXECUTION ---
urls = []
for file, key in PAGES_TO_GENERATE.items():
    state = random.choice(STATES)
    text = generate_3000_words(key, state)
    with open(file, "w", encoding="utf-8") as f:
        f.write(get_template(key, key, text))
    urls.append(f"{BASE_URL}/{file}")

# Sitemap
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in urls:
        f.write(f'<url><loc>{u}</loc><lastmod>{datetime.date.today()}</lastmod></url>')
    f.write('</urlset>')

# Bing Ping (Hardcoded JSON - No double braces)
payload = {
    "host": "brightlane.github.io",
    "key": INDEXNOW_KEY,
    "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
    "urlList": urls
}
try:
    requests.post("https://www.bing.com/indexnow", json=payload, timeout=10)
    print("Bing Notified.")
except:
    print("Ping Failed.")
