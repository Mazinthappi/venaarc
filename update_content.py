import glob
import re

# 1. Update index.html
with open('index.html', 'r') as f:
    index = f.read()

index = index.replace('<h1 class="title">Powering Progress<br><span>Sustainably</span></h1>', '<h1 class="title">Best Ongrid Solar<br><span>Installer In South India</span></h1>')
index = index.replace('<p class="description">Venaarc is committed to delivering innovative and reliable solar energy solutions for homes, businesses, and industries.</p>', '<p class="description">We create eco-friendly solutions that combine innovation and sustainability.</p>')
index = index.replace('<h2 class="section-title">Client Success Stories</h2>', '<h2 class="section-title">Trusted by Many, Loved by All</h2>')

with open('index.html', 'w') as f:
    f.write(index)

# 2. Update residential.html
with open('residential.html', 'r') as f:
    res = f.read()

res = res.replace('<h1 class="title">Reliable & Clean<br><span>Residential Solar</span></h1>', '<h1 class="title">Home Solar<br><span>Solutions</span></h1>')
res = res.replace('Take control of your energy costs, increase your property value, and reduce your carbon footprint with our tier-1 home solar solutions.', 'Cut your electricity bills with a PM Surya Ghar-eligible rooftop solar system. DCR-compliant panels, fast net metering approval, and quick ROI built for Indian homes.')

with open('residential.html', 'w') as f:
    f.write(res)

# 3. Update commercial.html
with open('commercial.html', 'r') as f:
    com = f.read()

com = com.replace('Optimize operational costs, meet ESG goals, and secure energy independence for your business.', 'Boost your bottom line with commercial solar built for accelerated depreciation and fast net metering approval. Scalable rooftop systems for offices, factories, and warehouses.')

with open('commercial.html', 'w') as f:
    f.write(com)

# 4. Update projects.html
with open('projects.html', 'r') as f:
    proj = f.read()

proj = proj.replace('Explore our track record of successful installations across residential, commercial, and utility sectors.', 'Powering Businesses Across South India. Explore large-scale, grid-connected solar parks and rooftop projects built for long-term reliability.')

with open('projects.html', 'w') as f:
    f.write(proj)

print("Updated content across pages with Kondaas data.")
