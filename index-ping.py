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

# 13-Page Google Authority Engine
PAGES = {
    "index.html": "MaxLend Approval Fast - Official Portal",
    "instant-funding.html": "Instant Funding Solutions 2026",
    "emergency-loans.html": "Emergency Capital for Credit Invisible",
    "tribal-lending-guide.html": "Understanding Tribal Installment Loans",
    "apply-now.html": "Fast Application for MaxLend Cash",
    "same-day-deposit.html": "Same Day Deposit Loans Online",
    "no-credit-check.html": "No Credit Check Installment Loans",
    "bad-credit-approval.html": "Bad Credit Approval Fast Track",
    "small-personal-loans.html": "Small Personal Loans for Emergencies",
    "borrow-money-fast.html": "How to Borrow Money Fast with MaxLend",
    "privacy.html": "Privacy Policy & Compliance",
    "contact.html": "Customer Support & Official Contact",
    "blog.html": "Daily Financial Success Blog"
}

STATES = ["Texas", "Florida", "Ohio", "California", "Illinois", "Georgia", "Michigan", "Virginia", "New York", "Arizona"]

# --- 2. THE 3,000 WORD CONTENT ENGINE ---
def generate_content(keyword, state):
    today = datetime.date.today().strftime("%B %d, 2026")
    content = f"<h2>{keyword} for {state} Residents: {today} Update</h2>"
    content += f"<p>Accessing <strong>{keyword}</strong> in {state} has never been more critical. MaxLend provides a sovereign lending bridge...</p>"
    
    sections = [
        "Financial Literacy: How Installment Loans Work",
        "The Role of Tribal Sovereignty in Modern Lending",
        "Why Alternative Credit Data Beats the FICO System",
        "Safe Borrowing and Repayment Strategies"
    ]
    
    for section in sections:
        content += f"<h3>{section}</h3><p>"
        content += f"When navigating the financial landscape of {state}, {keyword} users prioritize speed. MaxLend ensures that {section} is handled with transparency and respect for the borrower. " * 30
        content += "</p>"
    
    content += '<p style="font-size:0.8rem;">Resource: Learn more about financial rights at <a href="https://www.consumerfinance.gov/" rel="nofollow">CFPB.gov</a>.</p>'
    return content

# --- 3. THE MASTER TEMPLATE ---
def get_template(title, keyword, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{ --primary: #002D62; --secondary: #D4AF37; }}
        body {{ font-family: sans-serif; margin: 0; background: #fff; color: #333; line-height: 1.6; }}
        nav {{ background: #001f44; padding: 10px; text-align: center; }}
        nav a {{ color: white; margin: 0 10px; text-decoration: none; font-size: 0.8rem; }}
        header {{ background: var(--primary); color: white; padding: 40px; text-align: center; border-bottom: 4px solid var(--secondary); }}
        .logo {{ height: 80px; background: white; padding: 5px; border-radius: 5px; }}
        .container {{ max-width: 800px; margin: 20px auto; padding: 20px; }}
        .btn {{ display: inline-block; background: #c00; color: white; padding: 15px 30px; text-decoration: none; font-weight: bold; border-radius: 50px; }}
        footer {{ background: #111; color: #ccc; padding: 40px 20px; font-size: 0.7rem; }}
    </style>
    <script>
        document.addEventListener("mouseleave", function(e) {{
            if (e.clientY < 0) {{ window.open("{AFFILIATE_URL}", "_blank"); }}
        }});
    </script>
</head>
<body>
    <nav><a href="index.html">Home</a><a href="blog.html">Blog</a><a href="privacy.html">Privacy</a></nav>
    <header>
        <img src="{LOGO_PATH}" class="logo">
        <h1>{keyword}</h1>
        <p>Sovereign Lending • Fast Approval • 2026 Official Hub</p>
        <br><a href="{AFFILIATE_URL}" class="btn">APPLY NOW</a>
    </header>
    <div class="container">{body}</div>
    <footer>
        <p>Contact: 1-877-936-4336 | 145 Tribal Business Council Rd, Mandaree, ND 58757</p>
        <p>MaxLend is an entity of the MHA Nation. Tribal law applies. This is expensive borrowing.</p>
    </footer>
</body>
</html>"""

# --- 4. EXECUTION ---
generated_urls = []
for file, key in PAGES.items():
    state = random.choice(STATES)
    text = generate_content(key, state)
    with open(file, "w", encoding="utf-8") as f:
        f.write(get_template(key, key, text))
    generated_urls.append(f"{BASE_URL}/{file}")

# Sitemap
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in generated_urls:
        f.write(f'<url><loc>{u}</loc><lastmod>{datetime.date.today()}</lastmod></url>')
    f.write('</urlset>')

# IndexNow Ping
payload = {{"host": "brightlane.github.io", "key": "{INDEXNOW_KEY}", "keyLocation": "{BASE_URL}/{INDEXNOW_KEY}.txt", "urlList": generated_urls}}
try:
    requests.post("https://www.bing.com/indexnow", json=payload, timeout=10)
    print("Bing notified.")
except:
    print("Ping failed.")
