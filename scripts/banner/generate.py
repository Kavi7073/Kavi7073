#!/usr/bin/env python3
from pathlib import Path
import base64, mimetypes

ROOT=Path(__file__).resolve().parents[2]
ASSETS=ROOT/'assets'

def photo():
    for name in ['profile-photo.png','profile-photo.jpg','profile-photo.jpeg']:
        p=ASSETS/name
        if p.exists():
            mime=mimetypes.guess_type(name)[0] or 'image/png'
            b64=base64.b64encode(p.read_bytes()).decode()
            return f'''<defs><clipPath id="clip"><circle cx="135" cy="148" r="78"/></clipPath></defs>
<circle cx="135" cy="148" r="80" fill="#111827" stroke="#AA9BEF" stroke-width="2"/>
<image href="data:{mime};base64,{b64}" x="57" y="70" width="156" height="156" preserveAspectRatio="xMidYMid slice" clip-path="url(#clip)"/>
<circle cx="135" cy="148" r="78" fill="none" stroke="#AA9BEF" stroke-width="2"/>'''
    return '''<circle cx="135" cy="148" r="78" fill="#111827" stroke="#AA9BEF" stroke-width="2"/>
<circle cx="135" cy="125" r="28" fill="#7D8AA5" opacity=".65"/>
<path d="M84 198 C91 160 111 151 135 151 C159 151 179 160 186 198 Z" fill="#7D8AA5" opacity=".45"/>
<text x="135" y="232" text-anchor="middle" fill="#7D8AA5" font-family="monospace" font-size="8">ADD YOUR PHOTO</text>'''

def make(dark):
    bg='#0A0A0F' if dark else '#F7F8FC'; panel='#0F172A' if dark else '#FFFFFF'
    stroke='#24324A' if dark else '#D8DEEA'; fg='#E8ECF4' if dark else '#182033'; muted='#7D8AA5' if dark else '#667085'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="430" viewBox="0 0 1200 430">
<rect width="1200" height="430" rx="14" fill="{bg}"/><rect x="18" y="18" width="1164" height="394" rx="12" fill="{panel}" stroke="{stroke}"/>
<circle cx="42" cy="42" r="6" fill="#FF5F56"/><circle cx="62" cy="42" r="6" fill="#FFBD2E"/><circle cx="82" cy="42" r="6" fill="#27C93F"/>
<text x="1035" y="45" fill="{muted}" font-family="monospace" font-size="10">kavi.kanda — live</text><line x1="45" y1="70" x2="1155" y2="70" stroke="{stroke}"/>
<text x="50" y="100" fill="#06B6D4" font-family="monospace" font-size="10" font-weight="700">VISUAL.MAP</text>{photo()}
<text x="255" y="98" fill="#06B6D4" font-family="monospace" font-size="10" font-weight="700">SYSTEM.INFO</text>
<text x="255" y="128" fill="{muted}" font-family="monospace" font-size="10">Subject</text><text x="510" y="128" fill="{fg}" font-family="monospace" font-size="10">Kavi Kanda</text>
<text x="255" y="151" fill="{muted}" font-family="monospace" font-size="10">Role</text><text x="510" y="151" fill="{fg}" font-family="monospace" font-size="10">AI Engineer</text>
<text x="255" y="174" fill="{muted}" font-family="monospace" font-size="10">Focus</text><text x="510" y="174" fill="{fg}" font-family="monospace" font-size="10">AI × Software × Automation</text>
<text x="255" y="197" fill="{muted}" font-family="monospace" font-size="10">Stack</text><text x="510" y="197" fill="{fg}" font-family="monospace" font-size="10">Java · JS/TS · React · Node</text>
<text x="255" y="220" fill="{muted}" font-family="monospace" font-size="10">Building</text><text x="510" y="220" fill="{fg}" font-family="monospace" font-size="10">THE NEXT STEP</text>
<text x="255" y="243" fill="{muted}" font-family="monospace" font-size="10">Location</text><text x="510" y="243" fill="{fg}" font-family="monospace" font-size="10">India</text>
<line x1="255" y1="270" x2="1125" y2="270" stroke="{stroke}"/><text x="255" y="296" fill="{muted}" font-family="monospace" font-size="9">STATUS</text>
<text x="315" y="296" fill="#27C93F" font-family="monospace" font-size="9">● ALL SYSTEMS NOMINAL</text>
<text x="600" y="350" text-anchor="middle" fill="#AA9BEF" font-family="monospace" font-size="26" font-weight="700">BUILDING INTELLIGENT THINGS.</text>
<text x="600" y="375" text-anchor="middle" fill="{muted}" font-family="monospace" font-size="9">AI ENGINEER · FULL STACK DEVELOPER · CREATOR</text></svg>'''

for dark in (True,False):
    (ASSETS/f'banner-{"dark" if dark else "light"}.svg').write_text(make(dark),encoding='utf-8')
print('Banner generated.')
