import re

def create_page(filename, title, active_nav, body_content):
    with open('index.html', 'r') as f:
        base_html = f.read()
        
    head_match = re.search(r'(.*?)</header>', base_html, re.DOTALL)
    footer_match = re.search(r'(<footer>.*)', base_html, re.DOTALL)

    if head_match and footer_match:
        head_html = head_match.group(1) + '</header>\n\n'
        head_html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', head_html)
        head_html = head_html.replace('class="nav-link active"', 'class="nav-link"')
        
        active_str = f'href="{active_nav}.html" class="nav-link"'
        if active_nav == 'home':
            active_str = f'href="index.html" class="nav-link"'
            
        head_html = head_html.replace(active_str, active_str.replace('nav-link', 'nav-link active'))
        
        footer_html = '\n' + footer_match.group(1)
        
        with open(filename, 'w') as out:
            out.write(head_html + body_content + footer_html)

# 3. Products
products_body = """
    <section class="hero" style="background-image: url('images/hero_background_1786601991936.png'); min-height: 50vh;">
        <div class="hero-overlay"></div>
        <div class="container hero-content text-center" style="align-items: center;">
            <h2 class="subtitle">TECHNOLOGY</h2>
            <h1 class="title">Premium Products</h1>
            <p class="description" style="max-width: 700px; margin: 0 auto 30px;">We source only Tier-1 equipment to guarantee maximum yield, reliability, and safety.</p>
        </div>
    </section>
    
    <section class="section-padding bg-darker">
        <div class="container">
            <div class="products-grid">
                <div class="product-card scroll-animate">
                    <div class="product-icon"><i class="fa-solid fa-solar-panel"></i></div>
                    <h3>Solar Panels</h3>
                    <p>High-efficiency monocrystalline panels featuring PERC technology for superior low-light performance and 25-year linear power output warranties.</p>
                </div>
                <div class="product-card scroll-animate">
                    <div class="product-icon"><i class="fa-solid fa-charging-station"></i></div>
                    <h3>Solar Inverters</h3>
                    <p>String, micro, and hybrid inverters from world-leading brands. Built-in Wi-Fi monitoring and smart grid integration.</p>
                </div>
                <div class="product-card scroll-animate">
                    <div class="product-icon"><i class="fa-solid fa-car-battery"></i></div>
                    <h3>Battery Storage</h3>
                    <p>Lithium Iron Phosphate (LiFePO4) battery systems for safe, deep-cycle, and long-lasting energy reserves. Scalable from 5kWh to 1MWh.</p>
                </div>
                <div class="product-card scroll-animate">
                    <div class="product-icon"><i class="fa-solid fa-layer-group"></i></div>
                    <h3>Mounting Structures</h3>
                    <p>Aerodynamic, corrosion-resistant aluminum and galvanized steel structures engineered to withstand extreme wind and snow loads.</p>
                </div>
            </div>
        </div>
    </section>
"""
create_page('products.html', 'Products | Venaarc', 'products', products_body)

# 4. Services
services_body = """
    <section class="hero" style="background-image: url('images/project_residential_1786602252499.png'); min-height: 50vh;">
        <div class="hero-overlay"></div>
        <div class="container hero-content text-center" style="align-items: center;">
            <h2 class="subtitle">WHAT WE DO</h2>
            <h1 class="title">End-to-End Services</h1>
            <p class="description" style="max-width: 700px; margin: 0 auto 30px;">From initial consultation to lifelong maintenance, we handle every aspect of your solar journey.</p>
        </div>
    </section>
    
    <section class="section-padding">
        <div class="container text-center">
            <h2 class="section-title">Comprehensive Solar EPC</h2>
            <div class="solutions-grid" style="margin-top: 40px;">
                <div class="solution-card">
                    <i class="fa-solid fa-comments"></i>
                    <h3>Consultation & Survey</h3>
                    <p>Detailed energy audit, load analysis, and physical site survey using drone technology.</p>
                </div>
                <div class="solution-card">
                    <i class="fa-solid fa-pen-ruler"></i>
                    <h3>System Design</h3>
                    <p>Custom 3D CAD modeling, shadow analysis, and generation forecasting for optimal layout.</p>
                </div>
                <div class="solution-card">
                    <i class="fa-solid fa-helmet-safety"></i>
                    <h3>Installation</h3>
                    <p>Execution by certified engineers ensuring minimal disruption and adherence to strict safety codes.</p>
                </div>
                <div class="solution-card">
                    <i class="fa-solid fa-desktop"></i>
                    <h3>Monitoring & Maintenance</h3>
                    <p>24/7 remote monitoring through our dedicated app. Preventive AMC contracts and rapid repair support.</p>
                </div>
            </div>
        </div>
    </section>
"""
create_page('services.html', 'Services | Venaarc', 'services', services_body)

# 5. About Us
about_body = """
    <section class="hero" style="background-image: url('images/project_commercial_1786602265738.png'); min-height: 50vh;">
        <div class="hero-overlay"></div>
        <div class="container hero-content text-center" style="align-items: center;">
            <h2 class="subtitle">OUR STORY</h2>
            <h1 class="title">About Venaarc</h1>
            <p class="description" style="max-width: 700px; margin: 0 auto 30px;">Driving the transition to sustainable energy through innovation, integrity, and engineering excellence.</p>
        </div>
    </section>
    
    <section class="section-padding">
        <div class="container">
            <div style="display: flex; gap: 40px; align-items: center; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 300px;">
                    <img src="images/hero_background_1786601991936.png" style="width: 100%; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                </div>
                <div style="flex: 1; min-width: 300px;">
                    <h2 class="section-title" style="text-align: left;">Our Mission & Vision</h2>
                    <p><strong>Mission:</strong> To democratize clean energy by providing accessible, reliable, and highly efficient solar solutions tailored to every customer.</p>
                    <p><strong>Vision:</strong> A world powered entirely by renewable energy, where businesses and homes coexist harmoniously with the environment.</p>
                    <ul class="about-list" style="margin-top: 20px;">
                        <li><i class="fa-solid fa-check"></i> Quality Without Compromise</li>
                        <li><i class="fa-solid fa-check"></i> Customer-Centric Approach</li>
                        <li><i class="fa-solid fa-check"></i> Continuous Innovation</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
"""
create_page('about.html', 'About Us | Venaarc', 'about', about_body)

# 6. Contact Us
contact_body = """
    <section class="hero" style="background-image: url('images/hero_background_1786601991936.png'); min-height: 50vh;">
        <div class="hero-overlay"></div>
        <div class="container hero-content text-center" style="align-items: center;">
            <h2 class="subtitle">GET IN TOUCH</h2>
            <h1 class="title">Contact Us</h1>
            <p class="description" style="max-width: 700px; margin: 0 auto 30px;">Reach out today for a free consultation or technical support.</p>
        </div>
    </section>
    
    <section class="contact section-padding bg-darker">
        <div class="container contact-container">
            <div class="contact-info">
                <h4 class="section-subtitle">CONTACT DETAILS</h4>
                <h2 class="section-title">We're Here to Help</h2>
                <div class="contact-details">
                    <div class="contact-item">
                        <div class="icon"><i class="fa-solid fa-location-dot"></i></div>
                        <div>
                            <h4>Corporate Office</h4>
                            <p>123 Solar Avenue, Green District, 10001</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="icon"><i class="fa-solid fa-phone"></i></div>
                        <div>
                            <h4>Phone</h4>
                            <p>+1 (800) 555-0199</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="icon"><i class="fa-solid fa-envelope"></i></div>
                        <div>
                            <h4>Email</h4>
                            <p>info@venaarc.com</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="quote-form-container">
                <h3>Send a Message</h3>
                <form class="quote-form">
                    <div class="form-group">
                        <input type="text" placeholder="Full Name" required>
                    </div>
                    <div class="form-group">
                        <input type="email" placeholder="Email Address" required>
                    </div>
                    <div class="form-group">
                        <textarea placeholder="How can we help you?" rows="4" required></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary" style="width: 100%;">SUBMIT INQUIRY</button>
                </form>
            </div>
        </div>
    </section>
"""
create_page('contact.html', 'Contact Us | Venaarc', 'contact', contact_body)

print("Updated dummy pages with comprehensive layout structures.")
