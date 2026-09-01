import re

def update_file(filename, replacements):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        for old, new in replacements:
            content = content.replace(old, new)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f'Error updating {filename}: {e}')

# 1. Update team.html
old_team = '''          <h3>Abdul Rafay</h3>
          <p class="role">MERN Stack Developer</p>
          <p>Backend and database specialist building high-performance Node.js REST APIs, MongoDB schemas, and reliable web workflows.</p>
          <div class="team-skills">
            <span class="skill-tag">React.js</span>
            <span class="skill-tag">Node.js</span>
            <span class="skill-tag">MongoDB</span>
          </div>'''

new_team = '''          <h3>Abdul Rafay</h3>
          <p class="role">Graphic Designer</p>
          <p>Creative visual artist specializing in modern graphic design, UI/UX conceptualization, and brand identity.</p>
          <div class="team-skills">
            <span class="skill-tag">Photoshop</span>
            <span class="skill-tag">Illustrator</span>
            <span class="skill-tag">Figma</span>
          </div>'''

update_file('team.html', [(old_team, new_team)])

# 2. Update about.html
old_about = '<li style="margin-bottom: 0.8rem;"><strong style="color: var(--text);">Abdul Rafay — MERN Stack Developer</strong><br/>Backend and database specialist engineering high-performance Node.js REST APIs and MongoDB schemas.</li>'
new_about = '<li style="margin-bottom: 0.8rem;"><strong style="color: var(--text);">Abdul Rafay — Graphic Designer</strong><br/>Creative visual artist specializing in modern graphic design, UI/UX conceptualization, and brand identity.</li>'
update_file('about.html', [(old_about, new_about)])

# 3. Update README.md
old_readme = '2. **Abdul Rafay** — MERN Stack Developer (Node.js & MongoDB)'
new_readme = '2. **Abdul Rafay** — Graphic Designer (UI/UX, Branding)'
update_file('README.md', [(old_readme, new_readme)])

# 4. Remove GitHub buttons from projects.html
with open('projects.html', 'r', encoding='utf-8') as f:
    projects_html = f.read()
projects_html = re.sub(r'<a href="[^"]*" class="btn btn-secondary"[^>]*>.*?GitHub</a>', '', projects_html, flags=re.DOTALL)
with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(projects_html)

print('Update complete')
