import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update Navbar
nav_old = """            <nav class="nav-menu">
                <ul>
                    <li><a href="#home" class="nav-link active">Home</a></li>
                    <li><a href="#journey" class="nav-link">3D Solar Journey</a></li>
                    <li><a href="#about" class="nav-link">About Us</a></li>
                    <li><a href="#dashboard" class="nav-link">Live Storage</a></li>
                    <li><a href="#solutions" class="nav-link">Solutions</a></li>
                    <li><a href="#projects" class="nav-link">Projects</a></li>
                    <li><a href="#contact" class="nav-link">Contact</a></li>
                </ul>
            </nav>"""

nav_new = """            <nav class="nav-menu">
                <ul>
                    <li><a href="#home" class="nav-link active">Home</a></li>
                    <li><a href="#solutions" class="nav-link">Solutions</a></li>
                    <li><a href="#projects" class="nav-link">Projects</a></li>
                    <li><a href="#about" class="nav-link">About Us</a></li>
                    <li><a href="#contact" class="nav-link">Contact</a></li>
                </ul>
            </nav>"""

content = content.replace(nav_old, nav_new)

# Update mobile footer nav if it exists? (Wait, I saw only one nav). Let's check if there's another nav in the file.

# 2. Extract `#dashboard` content and delete its section
dashboard_pattern = r'(\s*<!-- 2\. Battery Charging Loading & Energy Dashboard Animation Section -->\s*<section id="dashboard" class="section-padding bg-darker">\s*<div class="container">\s*<div class="section-header text-center">.*?</div>\s*</section>\s*)'
dashboard_match = re.search(dashboard_pattern, content, re.DOTALL)
if dashboard_match:
    dashboard_html = dashboard_match.group(1)
    # Extract inner content from dashboard section (everything inside <div class="container">)
    inner_dash_match = re.search(r'<div class="container">(.*)</div>\s*</section>', dashboard_html, re.DOTALL)
    if inner_dash_match:
        inner_dash = inner_dash_match.group(1)
    else:
        inner_dash = ""
    # Remove dashboard from content
    content = content.replace(dashboard_html, '')
else:
    print("Dashboard not found!")
    inner_dash = ""

# 3. Extract `#about` section and remove it from its current place
about_pattern = r'(\s*<!-- About Us Section -->\s*<section id="about" class="about section-padding">.*?</section>\s*)'
about_match = re.search(about_pattern, content, re.DOTALL)
if about_match:
    about_html = about_match.group(1)
    content = content.replace(about_html, '')
else:
    print("About not found!")
    about_html = ""

# 4. Modify `#timeline` - Delete steps 4-8 and append `#dashboard` inner content
# First find the timeline wrapper end
# We'll just regex replace steps 4-8
steps_pattern = r'(\s*<!-- Step 4 -->\s*<div class="timeline-step" data-index="3">.*?<!-- Step 8 -->.*?<div class="timeline-empty"></div>\s*</div>\s*)'
content = re.sub(steps_pattern, '\n                ', content, flags=re.DOTALL)

# Insert inner_dash at the end of timeline container
timeline_end_pattern = r'(\s*</div>\s*</div>\s*</section>\s*<!-- Statistics Section -->)'
replacement = r'\n            </div>\n' + inner_dash + r'\n        </div>\n    </section>\n\n    <!-- Statistics Section -->'
content = re.sub(timeline_end_pattern, replacement, content, flags=re.DOTALL)

# 5. Insert `#about` before `#contact`
# Wait, user wants: home -> solutions -> projects -> about us -> contact.
# Let's insert `#about` right before `<!-- Contact & Quote Section -->`
contact_pattern = r'(\s*<!-- Contact & Quote Section -->)'
content = re.sub(contact_pattern, about_html + r'\1', content)

with open('index.html', 'w') as f:
    f.write(content)

print("HTML reordering complete.")
