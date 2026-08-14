import re

with open('index.html', 'r') as f:
    content = f.read()

# We want to extract the header and footer to reuse them.
header_match = re.search(r'(.*?<header id="header" class="floating-navbar">.*?</header>)', content, re.DOTALL)
header_html = header_match.group(1) if header_match else ""

footer_match = re.search(r'(<footer class="footer">.*)', content, re.DOTALL)
footer_html = footer_match.group(1) if footer_match else ""

print("Header length:", len(header_html))
print("Footer length:", len(footer_html))
