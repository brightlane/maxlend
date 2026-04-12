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

# 13-Page Authority Matrix
PAGES_TO_GENERATE = {
    "index.html": "MaxLend Approval Fast",
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

STATES = ["Texas", "Florida", "Ohio", "California", "Illinois", "Georgia", "Michigan", "Virginia", "Arizona", "New York"]

# --- 2. FAQ & SCHEMA ENGINE ---
def generate_faq(keyword, state):
    faqs = [
        {
            "q": f"How fast is {keyword} approval in {state}?",
            "a": f"Residents of {state} can typically receive a decision in minutes. Approved funds are sent via ACH as soon as the same business day."
        },
        {
            "q": "Does checking my rate impact my credit score?",
            "a": "No. MaxLend uses alternative data to verify eligibility, meaning there is no impact to your FICO score for checking your loan rate."
        },
        {
            "q": "Is MaxLend a sovereign lender?",
            "a": "Yes. MaxLend is an entity of the Mandan, Hidatsa, and Arikara Nation, operating under Tribal law to provide flexible credit access."
        }
    ]
    
    # Visible FAQ HTML
    faq_html = "<section class='faq-section'><h2>Frequently Asked Questions</h2>"
    # Invisible Google Schema
    schema_json = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": []}

    for item in faqs:
        faq_html += f"""
        <div class='faq-item'>
            <p><strong>Q: {item['q']}</strong></p>
            <p>A: {item['a']} <a href='{AFFILIATE_URL}'>Apply Now.</a></p>
        </div>"""
        schema_json["mainEntity"].append({
            "@type": "Question",
            "name": item['q'],
            "acceptedAnswer": {"@type": "Answer", "text": item['a']}
        })
    
    faq_html += f"</section><script type='application/ld+json'>{json.dumps(schema_json)}</script>"
    return faq_html

# --- 3. 3,000 WORD CONTENT GENERATOR ---
def generate_3000_words(keyword, state):
    today = datetime.date.today().strftime("%B %d, 2026")
    content = f"<h2>{keyword} for {state} Residents - Verified {today}</h2>"
    
    sections = [
        f"Why {keyword} is Trending in {state}",
        "The Advantage of Tribal Sovereign Lending",
        "How to Manage Short-Term Installment Loans",
        "Same Day Funding: The MaxLend Workflow"
    ]
    
    for section in sections:
        content += f"<h3>{section}</h3><p>"
        content += f"When looking for {keyword} in {state}, transparency is key. MaxLend stands out as a reliable partner for those needing immediate capital. " * 30
        content += "</p>"
    
    content += generate_faq(keyword, state)
    return content

# --- 4. THE MASTER TEMPLATE ---
def get_template(title, keyword, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | MaxLend Official</title>
    <style>
        :root {{ --primary: #002D62; --secondary: #D4AF37; --accent: #c00; }}
        body {{ font-family: sans-serif; margin: 0; background: #f9f9f9; color: #333; line-height: 1.6; }}
        header {{ background: var(--primary); color: white; padding: 50px 20px; text-align: center; border-bottom: 4px solid var(--secondary); }}
        .logo {{ height: 80px; background: white; padding: 5px; border-radius: 5px; }}
        .cta-btn {{ display: inline-block; background: var(--accent); color: white; padding: 20px 40px; font-size: 1.3rem; text-decoration: none; border-radius: 50px; font-weight: bold; margin: 20px 0; }}
        .container {{ max-width: 850px; margin: 30px auto; padding: 25px; background: white; border-radius: 10px; box-shadow: 0 2px 15px rgba(0,0,0,0.1); }}
        .faq-item {{ margin-bottom: 20px; padding: 15px; border: 1px solid #eee; background: #fdfdfd; }}
        footer {{ background: #111; color: #ccc; padding: 40px 20px; font-size: 0.75rem; }}
        .sticky-bar {{ position: fixed; bottom: 0; width: 100%; background: white; padding: 10px; text-align: center; border-top: 1px solid #ddd; }}
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
        <p>Sovereign Lending • No Hard Credit Pull • Fund by 5:00 PM</p>
        <a href="{AFFILIATE_URL}" class="cta-btn">GET STARTED AT MAXLEND</a>
    </header>
    <div class="container">{body}</div>
    <div class="sticky-bar"><a href="{AFFILIATE_URL}" class="cta-btn" style="padding: 10px 30px; margin:0;">APPLY NOW</a></div>
    <footer>
        <p><strong>Official Contact:</strong> 1-877-936-4336 | 145 Tribal Business Council Rd, Mandaree, ND 58757</p>
        <p>MaxLend is an entity of the MHA Nation. Tribal law applies. This is an expensive form of borrowing.</p>
        <p>Site Updated: {datetime.date.today()}</p>
    </footer>
    <br><br><br>
</body>
</html>"""

# --- 5. EXECUTION ---
urls = []
for filename, keyword in PAGES_TO_GENERATE.items():
    state = random.choice(STATES)
    body = generate_3000_words(keyword, state)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(get_template(keyword, keyword, body))
    urls.append(f"{BASE_URL}/{filename}")

# Sitemap
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in urls:
        f.write(f'<url><loc>{u}</loc><lastmod>{datetime.date.today()}</lastmod></url>')
    f.write('</urlset>')

# IndexNow Ping (Formatted correctly for Requests)
payload = {
    "host": "brightlane.github.io",
    "key": INDEXNOW_KEY,
    "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
    "urlList": urls
}
try:
    requests.post("https://www.bing.com/indexnow", json=payload, timeout=10)
    print("Bing/Google Ping Sent.")
except Exception as e:
    print(f"Ping Failed: {e}")
