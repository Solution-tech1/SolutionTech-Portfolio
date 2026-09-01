import re

# 1. Update index.html Text
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('Hi There! <span class=\"wave\">', 'Welcome! <span class=\"wave\">')
html = html.replace('I\'M <span class=\"highlight-purple\">SOLUTION TECH</span>', 'WE ARE <span class=\"highlight-purple\">SOLUTION TECH</span>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Hard-clean boxes from main-v2.css
with open('main-v2.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add a foolproof, ultra-high specificity CSS block at the very end
nuclear_css = '''
/* --- NUCLEAR BOX REMOVAL --- */
body .page-shell .info-card,
body .page-shell .stat-card,
body .page-shell .service-card,
body .page-shell .process-card,
body .page-shell .section-block {
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
}

body .page-shell .info-card:hover,
body .page-shell .stat-card:hover,
body .page-shell .service-card:hover,
body .page-shell .process-card:hover,
body .page-shell .section-block:hover {
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    transform: none !important;
}
'''
css += nuclear_css

with open('main-v2.css', 'w', encoding='utf-8') as f:
    f.write(css)

