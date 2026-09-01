import re
import random

with open('projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header and footer bounds
header_match = re.search(r'(?s)(.*?<section class="projects-grid"[^>]*>)', html)
footer_match = re.search(r'(?s)(</section>\s*</main>.*)', html)

header = header_match.group(1)
footer = footer_match.group(1)

# Extract all project cards
cards = re.findall(r'(?s)(<article class="project-card".*?</article>)', html)

# Shuffle the cards
random.shuffle(cards)

main_content = '\n'.join(cards)

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(header + '\n' + main_content + '\n' + footer)

