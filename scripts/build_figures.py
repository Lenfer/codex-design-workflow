#!/usr/bin/env python3
"""Build offline README diagrams with readable handoffs and installation scopes."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/figures'
CSS = '''
*{box-sizing:border-box}body{margin:0;background:#f4f5f8;color:#20283c}
.diagram-container{width:100%;overflow-x:auto}svg{display:block;width:100%;min-width:960px}
svg text{font-family:Arial,Helvetica,sans-serif;fill:#20283c}
svg .title{font-family:Georgia,serif;font-size:36px;letter-spacing:-.4px}
svg .heading{font-size:22px;font-weight:600}
svg .body{font-size:18px}svg .small{font-size:16px;fill:#566278}
svg .tiny{font-size:14px;fill:#566278}
svg .code{font-family:ui-monospace,monospace;font-size:16px;fill:#384da0}
svg .line{fill:none;stroke:#566278;stroke-width:1.5}
svg .rule{fill:none;stroke:#d6dbe5;stroke-width:1}
svg .panel{fill:#fff;stroke:#b6bfce;stroke-width:1.2}
svg .focal{fill:#e9ecf8;stroke:#384da0;stroke-width:1.5}
svg .zone{fill:#fff;stroke:#c8cfdd;stroke-width:1}
@media print{.diagram-container{overflow-x:visible}svg{min-width:0}}
'''


def text(x,y,value,cls='body',anchor=None):
    attr=f' text-anchor="{anchor}"' if anchor else ''
    return f'<text x="{x}" y="{y}" class="{cls}"{attr}>{escape(value)}</text>'


def lines(x,y,values,cls='small',gap=26):
    return ''.join(text(x,y+i*gap,value,cls) for i,value in enumerate(values))


def rect(x,y,w,h,cls='panel',radius=6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" class="{cls}"/>'


def arrow(d,slug):
    return f'<path d="{d}" class="line" marker-end="url(#{slug}-arrow)"/>'


def document(slug,title,desc,subtitle,body):
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 600" role="img" aria-labelledby="{slug}-title {slug}-desc">
<title id="{slug}-title">{escape(title)}</title>
<desc id="{slug}-desc">{escape(desc)}</desc>
<defs><marker id="{slug}-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 Z" fill="#566278"/></marker></defs>
<rect width="960" height="600" fill="#f4f5f8"/>
{text(40,68,title,'title')}{text(40,108,subtitle,'body')}{body}</svg>'''
    html=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title><style>{CSS}</style></head><body><main><div class="diagram-container">{svg}</div></main></body></html>'''
    (OUT/f'{slug}.html').write_text(html)


def workflow():
    slug='workflow'
    body=''.join(arrow(f'M{x} 280 H{x+60}',slug) for x in [216,452,688])
    rows=[(40,'01  Concept','pen.dev',['Layout and','original assets']),
          (276,'02  System','Penpot',['Tokens, components','and screen states']),
          (512,'03  Build','Project code',['Working UI','and interactions']),
          (748,'04  Check','BrowserOS Neo',['Visual comparison','and user scenarios'])]
    for x,stage,tool,payload in rows:
        body+=text(x,184,stage,'body')
        body+=rect(x,216,176,128,'focal' if x==276 else 'panel')
        body+=text(x,388,tool,'heading')+lines(x,424,payload)
    # Concept: composition and an original image asset.
    body+='<rect x="56" y="236" width="64" height="16" rx="3" fill="#d6dbe5"/><rect x="56" y="264" width="56" height="60" rx="3" fill="#e4e8f4"/><path d="M128 272 H196 M128 288 H188 M128 304 H172" class="rule"/>'
    # System: semantic tokens plus reusable UI parts.
    for x,c in [(304,'#384da0'),(336,'#20283c'),(368,'#ffffff')]:
        body+=f'<circle cx="{x}" cy="248" r="10" fill="{c}" stroke="#566278" stroke-width=".8"/>'
    body+='<rect x="292" y="280" width="144" height="20" rx="4" fill="#fff" stroke="#384da0"/><rect x="292" y="312" width="88" height="16" rx="3" fill="#384da0"/>'
    # Code: implementation, not another design canvas.
    body+=text(528,248,'<Page>','code')+text(540,280,'<Button />','code')+text(528,316,'</Page>','code')
    # Browser: render and scenario verification.
    body+='<path d="M748 244 H924" class="rule"/><circle cx="764" cy="230" r="3" fill="#b6bfce"/><circle cx="776" cy="230" r="3" fill="#b6bfce"/><rect x="764" y="260" width="60" height="64" rx="3" fill="#eceff5"/><path d="M848 288 L864 304 L892 268" fill="none" stroke="#384da0" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
    body+='<path d="M40 500 H920" class="rule"/>'
    body+=lines(40,536,['Codex uses the Design skill to choose specialists for these stages.',
                         'For a small change, start at the stage that needs work.'],'body',28)
    document(slug,'From a screen idea to a working UI',
             'Codex carries the concept and source assets into a design system, implementation and browser checks.',
             'Codex passes layout decisions and assets between tools.',body)


def elbow(sx,sy,cx,ex,ey):
    direction=1 if ey>sy else -1
    return f'M{sx} {sy} H{cx-8} Q{cx} {sy} {cx} {sy+8*direction} V{ey-8*direction} Q{cx} {ey} {cx+8} {ey} H{ex}'


def routing():
    slug='routing'
    tasks=[('Choose a new visual direction','Frontend Design or Taste'),
           ('Answer a UX or stack question','UI/UX Pro Max'),
           ('Review or refine an existing screen','Impeccable'),
           ('Motion, interactions or native/mobile UI','Emil Kowalski: 17 skills'),
           ('Document the system; find references','Google DESIGN.md + Awesome Design MD')]
    body=''
    for i in range(5):
        body+=arrow(elbow(248,272+i*20,[288,304,320,304,288][i],368,176+i*88),slug)
    body+=rect(40,248,208,136,'focal')+text(64,300,'Codex','heading')
    body+=lines(64,332,['Uses Design to','select a specialist.'])
    for i,(task,source) in enumerate(tasks):
        y=144+i*88
        body+=rect(368,y,552,64,'zone')
        body+=text(384,y+24,task,'small')+text(384,y+50,source,'body')
    document(slug,'Choose a specialist for the task',
             'Codex uses Design to select concept, UX, refinement, motion or system resources for the user’s request.',
             'Codex reads the relevant original skill from the pinned library.',body)


def setup():
    slug='setup'
    body=rect(40,152,416,340,'zone')
    body+='<rect x="504" y="152" width="416" height="340" rx="6" fill="none" stroke="#b6bfce" stroke-dasharray="6 5"/>'
    body+=text(64,192,'Codex installs the skills','heading')+text(528,192,'You connect the apps','heading')
    body+=rect(64,216,368,64,'focal')+text(84,244,'Design entry skill','body')+text(84,268,'design / SKILL.md','code')
    body+=rect(64,300,368,80)+text(84,332,'7 pinned source collections','body')+text(84,360,'Original files, licenses and hash checks','small')
    body+=lines(64,432,['Run doctor to verify these files.','The installer preserves Codex settings.'])
    for y,name,action in [(216,'BrowserOS Neo','Pair Codex on its MCP connection board.'),
                          (300,'pen.dev','Install the app and connect its tools.'),
                          (384,'Penpot','Set up your account and workspace.')]:
        body+=text(528,y+24,name,'body')+text(528,y+50,action,'tiny')
    body+=lines(40,540,['Then test live access: read a browser page and the design apps’ current state.'], 'body')
    document(slug,'Install skills, then connect your apps',
             'The installer places Design and seven source collections on disk; the recipient connects apps through their own MCP setup.',
             'MCP lets Codex call tools in your own apps and accounts.',body)


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    workflow();routing();setup()
    print('Built workflow, routing and setup HTML sources.')
