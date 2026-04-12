def get_template(title, keyword, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{ --primary: #002D62; --secondary: #D4AF37; --accent: #c00; --text: #333; }}
        body {{ font-family: 'Arial', sans-serif; margin: 0; background: #f0f2f5; color: var(--text); }}
        
        /* Ultra-Clean Header */
        header {{ background: white; padding: 20px; text-align: center; border-bottom: 3px solid var(--secondary); }}
        .logo {{ height: 60px; }}

        /* Visual Progress Tracker */
        .stepper {{ display: flex; justify-content: space-around; max-width: 600px; margin: 20px auto; padding: 0 10px; }}
        .step {{ text-align: center; flex: 1; font-size: 0.75rem; font-weight: bold; color: #999; }}
        .step.active {{ color: var(--primary); }}
        .step-circle {{ width: 30px; height: 30px; border-radius: 50%; background: #ddd; margin: 0 auto 5px; line-height: 30px; color: white; }}
        .step.active .step-circle {{ background: var(--secondary); }}

        /* Hero Card */
        .hero-card {{ background: linear-gradient(rgba(0,45,98,0.9), rgba(0,45,98,0.9)), url('https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&q=80&w=1000'); background-size: cover; color: white; padding: 60px 20px; text-align: center; }}
        .hero-card h1 {{ font-size: 2.2rem; margin: 0; text-transform: uppercase; letter-spacing: 1px; }}
        
        /* Icon Grid */
        .icon-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 15px; max-width: 900px; margin: -30px auto 30px; padding: 0 20px; }}
        .icon-item {{ background: white; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-bottom: 4px solid var(--secondary); }}
        .icon-item div {{ font-size: 2rem; margin-bottom: 10px; }}
        .icon-item span {{ display: block; font-size: 0.9rem; font-weight: bold; color: var(--primary); }}

        /* High-Visibility Button */
        .cta-wrap {{ text-align: center; margin: 40px 0; }}
        .main-btn {{ display: inline-block; background: var(--accent); color: white; padding: 25px 60px; font-size: 1.5rem; text-decoration: none; border-radius: 12px; font-weight: 800; box-shadow: 0 10px 0 #900; transition: all 0.1s; }}
        .main-btn:active {{ transform: translateY(4px); box-shadow: 0 6px 0 #900; }}

        /* Clean Content Area */
        .content-area {{ max-width: 800px; margin: auto; padding: 20px; background: white; border-radius: 15px; margin-bottom: 100px; font-size: 1.1rem; line-height: 1.8; }}
        
        /* Sticky Bar for Mobile */
        .sticky-bar {{ position: fixed; bottom: 0; width: 100%; background: white; padding: 15px; box-shadow: 0 -5px 15px rgba(0,0,0,0.1); text-align: center; z-index: 100; border-top: 2px solid var(--secondary); }}

        footer {{ background: #111; color: #777; padding: 40px 20px; text-align: center; font-size: 0.8rem; }}
    </style>
</head>
<body>

<header>
    <img src="{LOGO_PATH}" class="logo" alt="MaxLend">
</header>

<div class="stepper">
    <div class="step active"><div class="step-circle">1</div>Application</div>
    <div class="step active"><div class="step-circle">2</div>Approval</div>
    <div class="step"><div class="step-circle">3</div>Funding</div>
</div>

<div class="hero-card">
    <h1>{keyword}</h1>
    <p>Get up to $2,000 sent directly to your bank account.</p>
</div>

<div class="icon-grid">
    <div class="icon-item"><div>⚡</div><span>Fast Approval</span></div>
    <div class="icon-item"><div>🛡️</div><span>Secure Data</span></div>
    <div class="icon-item"><div>💸</div><span>Next Day Cash</span></div>
    <div class="icon-item"><div>📉</div><span>No FICO Impact</span></div>
</div>

<div class="cta-wrap">
    <a href="{AFFILIATE_URL}" class="main-btn">CHECK YOUR RATE &raquo;</a>
    <p style="font-size: 0.8rem; color: #666; margin-top: 15px;">Secure 256-bit encrypted application process.</p>
</div>

<div class="content-area">
    {body}
</div>

<div class="sticky-bar">
    <a href="{AFFILIATE_URL}" class="main-btn" style="padding: 15px 40px; font-size: 1.2rem; box-shadow: 0 5px 0 #900;">APPLY NOW</a>
</div>

<footer>
    <p>MaxLend is a sovereign enterprise of the Mandan, Hidatsa, and Arikara Nation.</p>
    <p>145 Tribal Business Council Rd, Mandaree, ND 58757 | 1-877-936-4336</p>
    <p>&copy; 2026 MaxLend Official Affiliate Portal</p>
</footer>

<script>
    // Exit Intent
    document.addEventListener("mouseleave", function(e) {{
        if (e.clientY < 0) {{ window.open("{AFFILIATE_URL}", "_blank"); }}
    }});
</script>

</body>
</html>"""
