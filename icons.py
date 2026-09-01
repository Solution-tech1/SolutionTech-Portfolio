import re

# 1. Fix app.js typewriter roles
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the array
js = re.sub(
    r'const typewriterRoles = \[.*?\];',
    'const typewriterRoles = ["Full-Stack Dev", "MERN-Stack Dev", "AI Integration", "WordPress Dev", "Shopify Dev", "Graphic Designing", "Digital Marketing"];',
    js,
    flags=re.DOTALL
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 2. Fix index.html icons
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

svgs = {
    'Design-led thinking': '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>',
    'Built for clients': '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>',
    'Ready to scale': '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>',
    
    'Strategy & Branding': '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>',
    'UI/UX Design': '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>',
    'Web Development': '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>',
    'AI Solutions': '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>',
    
    'Rapid Agile Sprints': '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>',
    'Production-Grade Quality': '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>',
    'Direct Founder Access': '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>'
}

html = re.sub(r'<span class="card-icon">.*?</span>(.*?)Design-led thinking', f'<span class="card-icon">{svgs["Design-led thinking"]}</span>\g<1>Design-led thinking', html, flags=re.DOTALL)
html = re.sub(r'<span class="card-icon">.*?</span>(.*?)Built for clients', f'<span class="card-icon">{svgs["Built for clients"]}</span>\g<1>Built for clients', html, flags=re.DOTALL)
html = re.sub(r'<span class="card-icon">.*?</span>(.*?)Ready to scale', f'<span class="card-icon">{svgs["Ready to scale"]}</span>\g<1>Ready to scale', html, flags=re.DOTALL)

html = re.sub(r'<div class="card-icon">.*?</div>(\s*<h3>Strategy & Branding)', f'<div class="card-icon">{svgs["Strategy & Branding"]}</div>\g<1>', html, flags=re.DOTALL)
html = re.sub(r'<div class="card-icon">.*?</div>(\s*<h3>UI/UX Design)', f'<div class="card-icon">{svgs["UI/UX Design"]}</div>\g<1>', html, flags=re.DOTALL)
html = re.sub(r'<div class="card-icon">.*?</div>(\s*<h3>Web Development)', f'<div class="card-icon">{svgs["Web Development"]}</div>\g<1>', html, flags=re.DOTALL)
html = re.sub(r'<div class="card-icon">.*?</div>(\s*<h3>AI Solutions)', f'<div class="card-icon">{svgs["AI Solutions"]}</div>\g<1>', html, flags=re.DOTALL)

html = re.sub(r'<span class="card-icon">.*?</span>(.*?)Rapid Agile Sprints', f'<span class="card-icon">{svgs["Rapid Agile Sprints"]}</span>\g<1>Rapid Agile Sprints', html, flags=re.DOTALL)
html = re.sub(r'<span class="card-icon">.*?</span>(.*?)Production-Grade Quality', f'<span class="card-icon">{svgs["Production-Grade Quality"]}</span>\g<1>Production-Grade Quality', html, flags=re.DOTALL)
html = re.sub(r'<span class="card-icon">.*?</span>(.*?)Direct Founder Access', f'<span class="card-icon">{svgs["Direct Founder Access"]}</span>\g<1>Direct Founder Access', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

