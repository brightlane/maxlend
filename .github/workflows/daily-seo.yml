import datetime
import random
import requests
import json
import os

# --- CONFIGURATION ---
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949096598005765&atid=MaxlendWeb"
LOGO_PATH = "images/Mr-owl-with-brown-eyes.jpg"

def get_template(title, keyword, body):
    # We use a try/except or defaults here so the script never crashes
    today_long = datetime.date.today().strftime("%B %d, 2026")
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{ --primary: #002D62; --secondary: #D4AF37; --accent: #c00; --bg: #f4f7f9; }}
        body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 0; background: var(--bg); }}
        .hot-link {{ text-decoration: none; color: inherit; display: block; }}
        header {{ background: white; padding: 20px; text-align: center; border-bottom: 4px solid var(--secondary); }}
        .logo {{ height: 80px; border-radius: 50%; border: 2px solid var(--secondary); }}
        .hero {{ background: var(--primary); color: white; padding: 40px 20px; text-align: center; }}
        .apply-btn {{ display: inline-block; background: var(--accent); color: white; padding: 20px 50px; font-size: 1.5rem; text-decoration: none; border-radius: 50px; font-weight: 900; box-shadow: 0 6px 0 #900; margin: 20px 0; }}
        .container {{ max-width: 800px; margin: 20px auto; padding: 20px; background: white; border-radius: 15px; }}
        footer {{ background: #111; color: #666; padding: 40px 20px 100px; text-align: center; font-size: 0.8rem; }}
    </style>
</head>
<body>
    <a href="{AFFILIATE_URL}" class="hot-link">
        <header>
            <img src="{LOGO_PATH}" onerror="this.src='https://raw.githubusercontent.com/brightlane/maxlend/main/images/Mr-owl-with-brown-eyes.jpg'" class="logo" alt="MaxLend">
            <h2 style="margin:10px 0 0;">{keyword}</h2>
        </header>
        <div class="hero">
            <h1>UP TO $2,000 TODAY</h1>
            <p>Fast Approval • No Hard Credit Pull</p>
            <span class="apply-btn">GET STARTED</span>
        </div>
    </a>
    <div class="container">{body}</div>
    <footer>
        <p>&copy; 2026 MaxLend Affiliate Portal | {today_long}</p>
    </footer>
</body>
</html>"""

def main():
    try:
        # 1. Generate the content
        keyword = "MaxLend Approval Fast"
        title = "Instant MaxLend Decisions 2026"
        body_content = "<p>Your 3,000 words of SEO content goes here...</p>"
        
        full_html = get_template(title, keyword, body_content)
        
        # 2. Save the file
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(full_html)
        print("Success: index.html generated.")

        # 3. The IndexNow Ping (Wrapped in Try so it doesn't crash the build)
        try:
            payload = {
                "host": "brightlane.github.io",
                "key": "817c039b282227a69abd9cfa9f9b87f2",
                "keyLocation": "https://brightlane.github.io/817c039b282227a69abd9cfa9f9b87f2.txt",
                "urlList": ["https://brightlane.github.io/maxlend/index.html"]
            }
            res = requests.post("https://www.bing.com/indexnow", json=payload, timeout=10)
            print(f"Ping result: {res.status_code}")
        except Exception as ping_error:
            print(f"Ping skipped: {ping_error}")

    except Exception as main_error:
        print(f"CRITICAL ERROR: {main_error}")
        exit(1) # This tells GitHub the build failed

if __name__ == "__main__":
    main()
