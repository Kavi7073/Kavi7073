#!/usr/bin/env python3
import json, os, urllib.request
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'assets'
USERNAME=json.loads((ROOT/'data/profile.json').read_text())['username']

def get(url):
    req=urllib.request.Request(url,headers={'Accept':'application/vnd.github+json','User-Agent':'profile-generator'})
    token=os.getenv('GITHUB_TOKEN')
    if token: req.add_header('Authorization',f'Bearer {token}')
    with urllib.request.urlopen(req,timeout=20) as r: return json.load(r)

try:
    user=get(f'https://api.github.com/users/{USERNAME}')
    repos=get(f'https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner')
except Exception as exc:
    print(f'GitHub API unavailable: {exc}')
    user={'public_repos':4,'followers':1}
    repos=[]
stars=sum(r.get('stargazers_count',0) for r in repos)
langs=Counter()
for r in repos:
    try:
        for k,v in get(r['languages_url']).items(): langs[k]+=v
    except Exception: pass

if not langs:
    langs=Counter({'JavaScript':1,'HTML':1,'CSS':1,'Python':1})
vals={'repos':user.get('public_repos',4),'followers':user.get('followers',1),'stars':stars if repos else 1,'languages':len(langs)}

def card(dark):
    bg='#0d1117' if dark else '#ffffff'; fg='#e6edf3' if dark else '#24292f'; muted='#8b949e' if dark else '#57606a'; border='#30363d' if dark else '#d0d7de'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="520" height="190"><rect x="1" y="1" width="518" height="188" rx="12" fill="{bg}" stroke="{border}"/>
<text x="22" y="30" fill="#AA9BEF" font-family="monospace" font-size="12" font-weight="700">{USERNAME}</text><text x="498" y="30" text-anchor="end" fill="{muted}" font-family="monospace" font-size="9">GITHUB / LIVE</text>
<text x="22" y="70" fill="{fg}" font-family="Arial" font-size="23" font-weight="700">GitHub statistics</text><line x1="22" y1="91" x2="498" y2="91" stroke="{border}"/>
<text x="22" y="120" fill="{muted}" font-family="Arial" font-size="10">REPOSITORIES</text><text x="22" y="143" fill="{fg}" font-family="Arial" font-size="19" font-weight="700">{vals['repos']}</text>
<text x="145" y="120" fill="{muted}" font-family="Arial" font-size="10">FOLLOWERS</text><text x="145" y="143" fill="{fg}" font-family="Arial" font-size="19" font-weight="700">{vals['followers']}</text>
<text x="268" y="120" fill="{muted}" font-family="Arial" font-size="10">PUBLIC STARS</text><text x="268" y="143" fill="{fg}" font-family="Arial" font-size="19" font-weight="700">{vals['stars']}</text>
<text x="391" y="120" fill="{muted}" font-family="Arial" font-size="10">LANGUAGES</text><text x="391" y="143" fill="{fg}" font-family="Arial" font-size="19" font-weight="700">{vals['languages']}</text>
<text x="22" y="173" fill="{muted}" font-family="Arial" font-size="9">Generated from the public GitHub API.</text></svg>'''
for dark in (True,False):
    (ASSETS/f'card-stats-{"dark" if dark else "light"}.svg').write_text(card(dark),encoding='utf-8')

total=sum(langs.values()) or 1
rows=sorted(langs.items(),key=lambda x:x[1],reverse=True)[:6]
items=[]
for i,(name,val) in enumerate(rows):
    y=45+i*20; pct=val/total*100
    items.append(f'<text x="20" y="{y}" fill="#e6edf3" font-family="Arial" font-size="10">{name}</text><rect x="105" y="{y-9}" width="{min(310,pct*7):.1f}" height="10" rx="5" fill="#AA9BEF"/><text x="430" y="{y}" fill="#8b949e" font-family="Arial" font-size="9">{pct:.1f}%</text>')
svg='<svg xmlns="http://www.w3.org/2000/svg" width="520" height="165"><rect width="520" height="165" rx="10" fill="#0d1117" stroke="#30363d"/><text x="20" y="24" fill="#AA9BEF" font-family="monospace" font-size="11" font-weight="700">MOST USED LANGUAGES</text>'+''.join(items)+'</svg>'
(ASSETS/'metrics.languages.svg').write_text(svg,encoding='utf-8')
print('Stats generated.')
