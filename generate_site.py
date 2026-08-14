import re

def update_navbar_and_footer(content, active_page='home'):
    nav_old_pattern = r'<nav class="nav-menu">.*?</nav>'
    
    # Generate the new nav
    nav_links = [
        ('home', 'index.html', 'Home'),
        ('residential', 'residential.html', 'Residential Solar'),
        ('commercial', 'commercial.html', 'Commercial Solar'),
        ('projects', 'projects.html', 'Solar Projects'),
        ('products', 'products.html', 'Products'),
        ('services', 'services.html', 'Services'),
        ('about', 'about.html', 'About Us'),
        ('contact', 'contact.html', 'Contact Us'),
    ]
    
    nav_html = '<nav class="nav-menu">\n                <ul>\n'
    for id_val, href, text in nav_links:
        active_class = ' active' if id_val == active_page else ''
        nav_html += f'                    <li><a href="{href}" class="nav-link{active_class}">{text}</a></li>\n'
    nav_html += '                </ul>\n            </nav>'
    
    content = re.sub(nav_old_pattern, nav_html, content, flags=re.DOTALL)
    return content

with open('index.html', 'r') as f:
    index_html = f.read()

# Update index.html navbar
index_html = update_navbar_and_footer(index_html, 'home')

# Add "Solar Savings Calculator" to index.html before "Products" (which is id="products")
calculator_html = """
    <!-- Solar Savings Calculator -->
    <section id="calculator" class="calculator section-padding bg-darker">
        <div class="container">
            <div class="section-header text-center">
                <h4 class="section-subtitle">ESTIMATE YOUR SAVINGS</h4>
                <h2 class="section-title">Solar Savings Calculator</h2>
                <p>Discover how much you could save by switching to Venaarc Solar Solutions.</p>
            </div>
            <div class="calculator-container" style="background: #fff; padding: 40px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); max-width: 800px; margin: 0 auto; color: #333;">
                <div style="display: flex; flex-direction: column; gap: 20px;">
                    <div>
                        <label style="font-weight: 600; margin-bottom: 10px; display: block;">Average Monthly Electricity Bill ($)</label>
                        <input type="range" min="50" max="1000" step="10" value="200" style="width: 100%;">
                        <div style="text-align: right; font-weight: bold; font-size: 1.2rem; color: var(--primary-red);">$200</div>
                    </div>
                    <div>
                        <label style="font-weight: 600; margin-bottom: 10px; display: block;">Available Roof Space (sq. ft.)</label>
                        <input type="range" min="200" max="5000" step="100" value="1000" style="width: 100%;">
                        <div style="text-align: right; font-weight: bold; font-size: 1.2rem; color: var(--primary-red);">1,000 sq ft</div>
                    </div>
                    <div style="background: rgba(230, 28, 36, 0.1); padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px;">
                        <h3 style="color: var(--primary-red); font-size: 2rem; margin-bottom: 5px;">$65,000+</h3>
                        <p style="margin: 0; font-weight: 500;">Estimated 25-Year Lifetime Savings</p>
                    </div>
                    <a href="contact.html" class="btn btn-primary" style="text-align: center; display: block; margin-top: 10px;">Get a Precise Quote</a>
                </div>
            </div>
        </div>
    </section>
"""

# Insert calculator before products
index_html = index_html.replace('    <!-- Products Section -->', calculator_html + '\n    <!-- Products Section -->')

with open('index.html', 'w') as f:
    f.write(index_html)

# Now generate residential.html
# Extract shell
head_match = re.search(r'(.*?)</header>', index_html, re.DOTALL)
footer_match = re.search(r'(<footer>.*)', index_html, re.DOTALL)

if head_match and footer_match:
    head_html = head_match.group(1) + '</header>\n\n'
    # Update title and active nav in head_html
    head_html = head_html.replace('<title>Venaarc - Energizing Tomorrow | Sustainable Solar Solutions</title>', '<title>Residential Solar | Venaarc Solar Solutions</title>')
    head_html = update_navbar_and_footer(head_html, 'residential')
    
    footer_html = '\n' + footer_match.group(1)
    
    residential_body = """
    <!-- Hero Section -->
    <section id="residential-hero" class="hero" style="background-image: url('images/hero_background_1786601991936.png'); min-height: 60vh;">
        <div class="hero-overlay"></div>
        <div class="container hero-content text-center" style="align-items: center;">
            <h2 class="subtitle">POWER YOUR HOME</h2>
            <h1 class="title">Reliable & Clean<br><span>Residential Solar</span></h1>
            <p class="description" style="max-width: 700px; margin: 0 auto 30px;">Take control of your energy costs, increase your property value, and reduce your carbon footprint with our tier-1 home solar solutions.</p>
            <div class="hero-btns justify-content-center" style="justify-content: center;">
                <a href="#calculator" class="btn btn-primary">CALCULATE SAVINGS</a>
            </div>
        </div>
    </section>

    <!-- Why Homeowners Choose Solar -->
    <section class="section-padding">
        <div class="container text-center">
            <h4 class="section-subtitle">THE ADVANTAGE</h4>
            <h2 class="section-title">Why Homeowners Choose Solar</h2>
            <div class="solutions-grid" style="margin-top: 40px;">
                <div class="solution-card scroll-animate">
                    <i class="fa-solid fa-piggy-bank"></i>
                    <h3>Massive Cost Savings</h3>
                    <p>Drastically reduce or eliminate your monthly electricity bills from day one. Lock in your energy rates for decades.</p>
                </div>
                <div class="solution-card scroll-animate">
                    <i class="fa-solid fa-house-circle-check"></i>
                    <h3>Property Value Increase</h3>
                    <p>Homes equipped with solar energy systems sell for significantly more and faster than non-solar homes.</p>
                </div>
                <div class="solution-card scroll-animate">
                    <i class="fa-solid fa-earth-americas"></i>
                    <h3>Environmental Impact</h3>
                    <p>Reduce reliance on fossil fuels. A standard home solar system offsets tons of CO2 emissions annually.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- System Options -->
    <section class="section-padding bg-darker">
        <div class="container">
            <div class="section-header text-center">
                <h4 class="section-subtitle">CUSTOMIZATION</h4>
                <h2 class="section-title">Residential System Options</h2>
                <p>We design systems customized to your roof space, energy consumption, and storage needs.</p>
            </div>
            <div class="products-grid">
                <div class="product-card scroll-animate">
                    <div class="product-icon"><i class="fa-solid fa-plug"></i></div>
                    <h3>Grid-Tied Systems</h3>
                    <p>Stay connected to the local grid. Generate power during the day and use grid power at night, utilizing Net Metering for maximum ROI.</p>
                </div>
                <div class="product-card scroll-animate">
                    <div class="product-icon"><i class="fa-solid fa-car-battery"></i></div>
                    <h3>Hybrid Systems</h3>
                    <p>Combine grid connection with battery backup. Keep essential appliances running seamlessly during power outages.</p>
                </div>
                <div class="product-card scroll-animate">
                    <div class="product-icon"><i class="fa-solid fa-house-crack"></i></div>
                    <h3>Off-Grid Systems</h3>
                    <p>Achieve total energy independence. Perfect for remote homes with robust battery banks to store days of power.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Shared Calculator & Process (Copied from Home) -->
    """ + calculator_html + """

    <!-- Call to Action -->
    <section class="section-padding" style="background: var(--primary-red); color: white; text-align: center;">
        <div class="container">
            <h2 style="font-size: 2.5rem; font-weight: 700; margin-bottom: 20px; color: white;">Ready to Power Your Home?</h2>
            <p style="font-size: 1.1rem; max-width: 600px; margin: 0 auto 30px;">Join thousands of homeowners who have switched to clean, affordable solar energy with Venaarc.</p>
            <a href="contact.html" class="btn" style="background: white; color: var(--primary-red); font-weight: bold; padding: 15px 30px; border-radius: 30px;">GET A FREE HOME ASSESSMENT</a>
        </div>
    </section>
    """
    
    with open('residential.html', 'w') as f:
        f.write(head_html + residential_body + footer_html)

print("Generated residential.html and updated index.html")
