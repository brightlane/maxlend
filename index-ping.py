def get_template(title, keyword, body):
    today_long = datetime.date.today().strftime("%B %d, 2026")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | MaxLend Official Portal</title>
    <style>
        :root {{ --primary: #002D62; --secondary: #D4AF37; --accent: #c00; --bg: #f4f7f9; }}
        body {{ font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; margin: 0; background: var(--bg); color: #333; line-height: 1.6; }}
        
        /* Glassmorphism Header */
        header {{ background: linear-gradient(135deg, #001f44 0%, #00458b 100%); color: white; padding: 60px 20px; text-align: center; border-bottom: 5px solid var(--secondary); }}
        .logo {{ height: 90px; background: white; padding: 8px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }}
        
        /* High-Conversion Hero */
        .hero-h1 {{ font-size: 2.5rem; margin: 20px 0 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }}
        .hero-sub {{ font-size: 1.1rem; opacity: 0.9; margin-bottom: 30px; }}
        
        /* The Trust Bar */
        .trust-bar {{ display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 20px; }}
        .trust-tag {{ background: rgba(255,255,255,0.1); padding: 5px 15px; border-radius: 20px; font-size: 0.8rem; border: 1px solid rgba(255,255,255,0.2); }}

        /* Content Cards */
        .container {{ max-width: 900px; margin: -40px auto 40px; padding: 0 20px; }}
        .card {{ background: white; padding: 40px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #eef1f4; }}
        
        /* Readability Improvements */
        h2 {{ color: var(--primary); font-size: 1.8rem; border-left: 6px solid var(--secondary); padding-left: 15px; margin-top: 40px; }}
        p {{ font-size: 1.1rem; color: #444; margin-bottom: 25px; }}
        
        /* The Big Red Button */
        .cta-btn {{ display: inline-block; background: var(--accent); color: white; padding: 22px 50px; font-size: 1.4rem; text-decoration: none; border-radius: 50px; font-weight: bold; transition: 0.3s; box-shadow: 0 8px 20px rgba(204,0,0,0.3); border: none; cursor: pointer; }}
        .cta-btn:hover {{ transform: scale(1.05); background: #e60000; box-shadow: 0 12px 25px rgba(204,0,0,0.4); }}
        
        /* FAQ Styling */
        .faq-item {{ background: #f8fbff; border: 1px solid #d0e3ff; border-radius: 10px; padding: 20px; margin-bottom: 15px; }}
        .faq-item strong {{ color: var(--primary); display: block; margin-bottom: 10px; font-size: 1.1rem; }}
        
        /* Floating Mobile Footer */
        .sticky-bar {{ position: fixed; bottom: 0; width: 100%; background: white; padding: 15px; text-align: center; box-shadow: 0 -5px 20px rgba(0,0,0,0.1); z-index: 1000; border-top: 2px solid var(--secondary); }}
        
        footer {{ background: #0b1218; color: #999; padding: 60px 20px; text-align: center; font-size: 0.85rem; }}
        .legal-box {{ max-width: 700px; margin: auto; border-top: 1px solid #333; padding-top: 20px; }}
    </style>
    <script>
        // Exit Intent Pop-under
        document.addEventListener("mouseleave", function(e) {{
            if (e.clientY < 0) {{ window.open("{AFFILIATE_URL}", "_blank"); }}
        }});
    </script>
</head>
<body>

    <header>
        <img src="{LOGO_PATH}" class="logo" alt="MaxLend Seal">
        <h1 class="hero-h1">{keyword}</h1>
        <p class="hero-sub">Sovereign Installment Loans for Modern Borrowers</p>
        <div class="trust-bar">
            <span class="trust-tag">🛡️ 256-Bit Encrypted</span>
            <span class="trust-tag">⚡ Same Day Funding</span>
            <span class="trust-tag">🦅 MHA Nation Entity</span>
        </div>
    </header>

    <div class="container">
        <div class="card">
            <div style="text-align:center; margin-bottom:40px;">
                <h2 style="border:none; padding:0; margin-bottom:10px;">Check Your Eligibility in 60 Seconds</h2>
                <p>No hard credit pull. Checking your rate will not impact your FICO® score.</p>
                <a href="{AFFILIATE_URL}" class="cta-btn">GET MY CASH DECISION</a>
            </div>

            {body}
            
            <div style="background: #fff8e1; padding: 25px; border-radius: 10px; border: 1px dashed var(--secondary); margin-top: 40px;">
                <h3 style="margin-top:0;">Final April 2026 Notice</h3>
                <p style="margin-bottom:0; font-size: 1rem;">Applications are currently being prioritized for residents in high-demand states. Apply before 5:00 PM EST for the fastest processing times.</p>
            </div>
        </div>
    </div>

    <div class="sticky-bar">
        <a href="{AFFILIATE_URL}" class="cta-btn" style="font-size: 1.1rem; padding: 12px 40px;">APPLY NOW</a>
    </div>

    <footer>
        <div class="legal-box">
            <p><strong>Official Entity:</strong> MaxLend is a sovereign enterprise of the Mandan, Hidatsa, and Arikara Nation.</p>
            <p>145 Tribal Business Council Rd, Mandaree, ND 58757 | 1-877-936-4336</p>
            <p>Loans from MaxLend are expensive and intended for short-term financial needs only. Please borrow responsibly.</p>
            <p style="margin-top:20px;">&copy; 2026 MaxLend Approval Fast | Updated: {today_long}</p>
        </div>
    </footer>

</body>
</html>"""
