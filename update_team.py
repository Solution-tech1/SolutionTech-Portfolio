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
team_html = [
    (
        '''          <h3>M Raza</h3>
          <p class="role">CEO & Full Stack Lead (AI Integration)</p>
          <p>Lead architect engineering scalable MERN stack web applications and integrating advanced AI capabilities for global client growth.</p>''',
        '''          <h3>M Raza Rajput</h3>
          <p class="role">CEO & Full Stack Lead (AI Integration)</p>
          <div class="team-info" style="margin: 10px 0; font-size: 0.9em; color: var(--muted); text-align: left;">
            <p style="margin-bottom: 5px;">🎓 <strong>Edu:</strong> Intermediate completed in CS</p>
            <p style="margin-bottom: 5px;">💼 <strong>Exp:</strong> Almost 2 years</p>
          </div>
          <p>Lead architect engineering scalable MERN stack web applications and integrating advanced AI capabilities for global client growth.</p>'''
    ),
    (
        '''          <h3>Hamza Shamsi</h3>
          <p class="role">Full Stack Developer</p>
          <p>A versatile engineer specializing in building robust web applications, from dynamic React interfaces to powerful Python and Node.js backends.</p>''',
        '''          <h3>Hamza Shamsi</h3>
          <p class="role">Full Stack Developer</p>
          <div class="team-info" style="margin: 10px 0; font-size: 0.9em; color: var(--muted); text-align: left;">
            <p style="margin-bottom: 5px;">🎓 <strong>Edu:</strong> Inter completed in commerce</p>
            <p style="margin-bottom: 5px;">💼 <strong>Exp:</strong> 1 year</p>
          </div>
          <p></p>'''
    ),
    (
        '''          <h3>Aliyan</h3>
          <p class="role">Frontend Developer & Growth Marketer</p>
          <p>Bridges clean frontend code with digital marketing, building responsive Tailwind layouts optimized for SEO and conversion rates.</p>''',
        '''          <h3>Aliyan Kaleem</h3>
          <p class="role">Frontend Developer & Growth Marketer</p>
          <div class="team-info" style="margin: 10px 0; font-size: 0.9em; color: var(--muted); text-align: left;">
            <p style="margin-bottom: 5px;">🎓 <strong>Edu:</strong> Doing intermediate</p>
            <p style="margin-bottom: 5px;">💼 <strong>Exp:</strong> Fresh</p>
          </div>
          <p></p>'''
    ),
    (
        '''          <h3>Abdul Rafay</h3>
          <p class="role">Graphic Designer</p>
          <p>Creative visual artist specializing in modern graphic design, UI/UX conceptualization, and brand identity.</p>''',
        '''          <h3>Abdul Rafay</h3>
          <p class="role">Graphic Designer</p>
          <div class="team-info" style="margin: 10px 0; font-size: 0.9em; color: var(--muted); text-align: left;">
            <p style="margin-bottom: 5px;">🎓 <strong>Edu:</strong> Doing intermediate in CS</p>
            <p style="margin-bottom: 5px;">💼 <strong>Exp:</strong> 6 months</p>
          </div>
          <p></p>'''
    )
]

update_file('team.html', team_html)

# 2. Update about.html
about_html = [
    (
        '<li style="margin-bottom: 0.8rem;"><strong style="color: var(--text);">M Raza — CEO & Full Stack Lead (AI Integration)</strong><br/>Architecting scalable MERN stack web applications and integrating advanced AI capabilities for global clients.</li>',
        '<li style="margin-bottom: 0.8rem;"><strong style="color: var(--text);">M Raza Rajput — CEO & Full Stack Lead (AI Integration)</strong><br/><em>Edu: Intermediate completed in CS | Exp: Almost 2 years</em><br/>Architecting scalable MERN stack web applications and integrating advanced AI capabilities for global clients.</li>'
    ),
    (
        '<li style="margin-bottom: 0.8rem;"><strong style="color: var(--text);">Hamza Shamsi — Full Stack Developer</strong><br/>A versatile engineer specializing in building robust web applications, from dynamic React interfaces to powerful Python and Node.js backends.</li>',
        '<li style="margin-bottom: 0.8rem;"><strong style="color: var(--text);">Hamza Shamsi — Full Stack Developer</strong><br/><em>Edu: Inter completed in commerce | Exp: 1 year</em><br/></li>'
    ),
    (
        '<li style="margin-bottom: 0.8rem;"><strong style="color: var(--text);">Aliyan — Frontend Developer & Growth Marketer</strong><br/>Bridges clean frontend code with digital marketing, building responsive Tailwind layouts optimized for SEO.</li>',
        '<li style="margin-bottom: 0.8rem;"><strong style="color: var(--text);">Aliyan Kaleem — Frontend Developer & Growth Marketer</strong><br/><em>Edu: Doing intermediate | Exp: Fresh</em><br/></li>'
    ),
    (
        '<li style="margin-bottom: 0.8rem;"><strong style="color: var(--text);">Abdul Rafay — Graphic Designer</strong><br/>Creative visual artist specializing in modern graphic design, UI/UX conceptualization, and brand identity.</li>',
        '<li style="margin-bottom: 0.8rem;"><strong style="color: var(--text);">Abdul Rafay — Graphic Designer</strong><br/><em>Edu: Doing intermediate in CS | Exp: 6 months</em><br/></li>'
    )
]

update_file('about.html', about_html)
