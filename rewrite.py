import re

with open('projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header and footer
header_match = re.search(r'(?s)(<!DOCTYPE html>.*?</header>)', html)
footer_match = re.search(r'(?s)(<footer class="site-footer">.*)', html)

header = header_match.group(1)
footer = footer_match.group(1)

projects = [
    { 'title': 'Study Al Quran', 'desc': 'An international online Quran & Islamic education platform engineered for seamless student enrollment.', 'url': 'https://studyalquran.com' },
    { 'title': 'Cells Part Store', 'desc': 'A robust e-commerce platform for tech and mobile replacement parts featuring full product catalog management.', 'url': 'https://cellspart.com' },
    { 'title': '6Star Pools Australia', 'desc': 'A high-converting web platform built for a premier Australian swimming pool construction & maintenance company.', 'url': 'https://6starpools.au/' },
    { 'title': 'Al Noor Quran Academy', 'desc': 'A worldwide digital learning portal connecting students across the UK, USA, and Australia with certified tutors.', 'url': 'https://www.alnooronlinequranacademy.com/' },
    { 'title': 'Aspect Cleaning', 'desc': 'A modern commercial and residential service platform engineered for an Australian cleaning agency.', 'url': 'https://aspectwindowcleaning.com.au/' },
    { 'title': 'Nexus AI Interactive Book', 'desc': 'An intelligent online digital book & e-reading platform where users can read books online and chat with AI.', 'url': 'https://nexus-ai-book.vercel.app' },
    { 'title': 'HealthMate Wellness', 'desc': 'A comprehensive health tracking and wellness platform built to streamline patient data management.', 'url': 'https://healthmate-frontend-five.vercel.app/' },
    { 'title': 'Luxe Clothing Brand', 'desc': 'A robust MERN stack e-commerce web application featuring full CRUD capabilities and secure data routing.', 'url': 'https://luxe-brand.vercel.app/' },
]

main_content = '\n    <main class="page-shell" style="padding-top: 5rem;">\n      <h1 style="text-align: center; margin-bottom: 3rem; color: #fff;">My Recent <strong style="color: #c084fc;">Works</strong></h1>\n      <p style="text-align: center; color: var(--muted); margin-bottom: 4rem;">Here are a few projects I\'ve worked on recently.</p>\n      <section class="projects-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 3rem;">\n'

for p in projects:
    encoded_url = p['url'].replace('://', '%3A%2F%2F').replace('/', '%2F')
    img_url = f"https://image.thum.io/get/width/600/crop/800/{p['url']}"
    
    card = f'''
        <article class="project-card" style="display: flex; flex-direction: column; align-items: center; text-align: center; background: transparent; padding: 2rem; border-radius: 12px; border: 1px solid rgba(192, 132, 252, 0.4); box-shadow: 0 4px 15px rgba(192, 132, 252, 0.2); transition: all 0.3s ease;">
          <img src="{img_url}" alt="{p['title']}" style="width: 100%; border-radius: 8px; margin-bottom: 1.5rem; object-fit: cover; aspect-ratio: 16/10; border: 1px solid rgba(255,255,255,0.1);" />
          <h2 style="font-size: 1.5rem; margin-bottom: 1rem; color: #fff;">{p['title']}</h2>
          <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem; flex-grow: 1;">{p['desc']}</p>
          <div style="display: flex; gap: 1rem;">
            <a href="#" class="btn btn-secondary" style="background: transparent; border: 1px solid #c084fc; color: #fff;"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg" style="margin-right: 5px;"><path d="M511.6 76.3C264.3 76.2 64 276.4 64 523.5 64 718.9 189.3 885 363.8 946c23.5 5.9 19.9-10.8 19.9-22.2v-77.5c-135.7 15.9-141.2-73.9-150.3-88.9C215 726 171.5 718 184.5 703c30.9-15.9 62.4 4 98.9 57.9 26.4 39.1 77.9 32.5 104 26 5.7-23.5 17.9-44.5 34.7-60.8-140.6-25.2-199.2-111-199.2-213 0-49.5 16.3-95 48.3-131.7-20.4-60.5 1.9-112.3 4.9-120 58.1-5.2 118.5 41.6 123.2 45.3 33-8.9 70.7-13.6 112.9-13.6 42.4 0 80.2 4.9 113.5 13.9 11.3-8.6 67.3-48.8 121.3-43.9 2.9 7.7 24.7 58.3 5.5 118 32.4 36.8 48.9 82.7 48.9 132.3 0 102.2-59 188.1-200 212.9a127.5 127.5 0 0 1 38.1 91v112.5c.8 9 0 17.9 15 17.9 177.1-59.7 304.6-227 304.6-424.1 0-247.2-200.4-447.3-447.5-447.3z"></path></svg> GitHub</a>
            <a href="{p['url']}" target="_blank" class="btn btn-primary" style="background: #c084fc; border: none; color: #fff;"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg" style="margin-right: 5px;"><path fill="none" d="M0 0h24v24H0z"></path><path d="M19 19H5V5h7V3H5a2 2 0 00-2 2v14a2 2 0 002 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"></path></svg> Demo</a>
          </div>
        </article>
'''
    main_content += card

main_content += '\n      </section>\n    </main>\n\n'

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(header + main_content + footer)

