import re

with open('projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    'HealthMate Wellness': 'assets/projects/healthmate_ui_1788278809242.jpg',
    'Earthy Electronics': 'assets/projects/earthy_ui_1788278820511.jpg',
    'Cells Part Store': 'assets/projects/cells_ui_1788278832723.jpg',
    'Luxe Clothing Brand': 'assets/projects/luxe_ui_1788278845205.jpg',
    'Aspect Cleaning': 'assets/projects/aspect_ui_1788278879448.jpg',
    'Al Noor Quran Academy': 'assets/projects/alnoor_ui_1788278890743.jpg',
    '6Star Pools Australia': 'assets/projects/6star_ui_1788278903938.jpg',
    'Study Al Quran': 'assets/projects/study_ui_1788278915561.jpg',
    'Nexus AI Interactive Book': 'assets/projects/nexus_ui_1788278926934.jpg'
}

for alt_text, img_path in replacements.items():
    pattern = r'<img src="https://images\.unsplash\.com/[^"]*" alt="' + re.escape(alt_text) + r'"'
    replacement = f'<img src="{img_path}" alt="{alt_text}"'
    html = re.sub(pattern, replacement, html)

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(html)
