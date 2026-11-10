#!/usr/bin/env python3
"""Build the README's editable, offline Corporate diagram sources."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/figures'
CSS = '''
*{box-sizing:border-box}body{margin:0;background:#f4f5f8;color:#20283c}
.diagram-container{width:100%;overflow-x:auto}svg{display:block;width:100%;min-width:1280px}
svg text{font-family:Arial,Helvetica,sans-serif;fill:#20283c}
.title{font-family:Georgia,serif;font-size:48px;letter-spacing:-1px}
svg .eyebrow{font-family:monospace;font-size:13px;letter-spacing:2px;fill:#566278}
.heading{font-size:24px;font-weight:600}.body{font-size:18px}
.small{font-size:16px;fill:#566278}.tiny{font-size:14px;fill:#566278}
.model{font-family:monospace;font-size:14px;fill:#384da0}
.line{fill:none;stroke:#566278;stroke-width:1.5}
.rule{fill:none;stroke:#d6dbe5;stroke-width:1}
svg .card{fill:#fff;stroke:#c8cfdd;stroke-width:1;rx:8}
.focal{fill:#e9ecf8;stroke:#384da0;stroke-width:1.5;rx:8}
@media print{.diagram-container{overflow-x:visible}svg{min-width:0}}
'''


def text(x, y, value, cls='body', anchor=None):
    attr = f' text-anchor="{anchor}"' if anchor else ''
    return f'<text x="{x}" y="{y}" class="{cls}"{attr}>{escape(value)}</text>'


def lines(x, y, values, cls='body', gap=28):
    return ''.join(text(x, y+i*gap, value, cls) for i, value in enumerate(values))


def rect(x, y, w, h, cls='card'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="{cls}"/>'


def arrow(d, slug):
    return f'<path d="{d}" class="line" marker-end="url(#{slug}-arrow)"/>'


def document(slug, title, desc, eyebrow, body):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720"
role="img" aria-labelledby="{slug}-title {slug}-desc">
<title id="{slug}-title">{escape(title)}</title>
<desc id="{slug}-desc">{escape(desc)}</desc>
<defs><marker id="{slug}-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6 Z" fill="#566278"/></marker></defs>
<rect width="1280" height="720" fill="#f4f5f8"/>
{text(40, 44, eyebrow, 'eyebrow')}
{text(40, 108, title, 'title')}
{body}
</svg>'''
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title>
<style>{CSS}</style></head><body><main><div class="diagram-container">{svg}</div></main></body></html>'''
    (OUT / f'{slug}.html').write_text(html)


def workflow():
    slug='workflow'
    body=text(40,148,'An approved direction becomes a reusable system, then a working interface.','small')
    for i in range(4):
        x=40+i*308
        body+=arrow(f'M{x+140} 240 V288',slug)
        if i<3:
            body+=arrow(f'M{x+280} 396 H{x+308}',slug)
    body+=rect(40,184,1200,56,'focal')
    body+=text(60,219,'DESIGN', 'heading')+text(208,219,'Brief + context → one lead skill + targeted specialists','body')
    rows=[('01','pen.dev','Concept', ['Composition, imagery,','icons and motion intent'],['Editable concept + assets','+ motion prototype'],'Sol · high'),
          ('02','Penpot','Design system',['Tokens, components,','states and responsiveness'],['System + screen IDs','+ motion specification'],'Sol · high'),
          ('03','Project code','Implementation',['Reuse the system,','assets and components'],['Working UI','+ interaction behavior'],'Sol · medium'),
          ('04','BrowserOS Neo','Verification',['Compare real rendering;','exercise user scenarios'],['Verified result','+ focused corrections'],'Sol · high')]
    for i,(num,name,stage,actions,outputs,model) in enumerate(rows):
        x=40+i*308
        body+=rect(x,288,280,288)
        body+=text(x+20,320,num,'eyebrow')+text(x+20,356,name,'heading')+text(x+20,384,stage,'small')
        body+=lines(x+20,428,actions)+f'<path d="M{x+20} 472 H{x+260}" class="rule"/>'
        body+=lines(x+20,504,outputs,'small')+text(x+20,556,model,'model')
    body+=text(40,620,'MOTION IS SPECIFIED, BUILT AND VERIFIED THROUGHOUT', 'eyebrow')
    body+=text(40,652,'Icons + complex procedural motion in pen.dev: Astra · medium','body')
    body+=text(40,684,'Models are recommendations. Fix discrepancies at the relevant stage; preserve the approved style.','tiny')
    document(slug,'From intent to verified interface',
             'Design routes a brief through pen.dev concepts, Penpot systems, implementation and BrowserOS Neo verification.',
             'CODEX DESIGN WORKFLOW / 01 — PROCESS',body)


def routing():
    slug='routing'
    body=text(40,148,'Choose for the task. Load the original instructions. Keep one visual direction.','small')
    # Separate root-edge ports and rounded elbows avoid an overlapping bus.
    centers=[152+i*244 for i in range(5)]
    for i,cx in enumerate(centers):
        port=[560,600,640,680,720][i]
        if cx<port:
            d=f'M{port} 244 V268 Q{port} 276 {port-8} 276 H{cx+8} Q{cx} 276 {cx} 284 V320'
        elif cx>port:
            d=f'M{port} 244 V268 Q{port} 276 {port+8} 276 H{cx-8} Q{cx} 276 {cx} 284 V320'
        else:d=f'M{port} 244 V320'
        # Each branch uses a distinct horizontal corridor.
        y=[268,284,296,284,268][i]
        if cx<port:d=f'M{port} 244 V{y-8} Q{port} {y} {port-8} {y} H{cx+8} Q{cx} {y} {cx} {y+8} V320'
        elif cx>port:d=f'M{port} 244 V{y-8} Q{port} {y} {port+8} {y} H{cx-8} Q{cx} {y} {cx} {y+8} V320'
        body+=arrow(d,slug)
    body+=rect(480,184,320,60,'focal')+text(640,222,'Design router','heading','middle')
    rows=[('New direction',['Frontend Design','or Taste'],['Composition, typography,','distinctive visual identity']),
          ('UX questions',['UI/UX Pro Max'],['Focused UX search','and stack guidance']),
          ('Existing UI',['Impeccable'],['Critique, polish, adapt,','harden and refine']),
          ('Motion + interaction',['Emil Kowalski'],['17 focused skills','for motion and UI behavior']),
          ('System + references',['Google DESIGN.md','Awesome Design MD'],['Document system decisions;','explore relevant references'])]
    for i,(task,skills,scope) in enumerate(rows):
        x=40+i*244
        body+=rect(x,320,224,240)+text(x+16,356,task,'small')
        body+=lines(x+16,400,skills,'body')+lines(x+16,496,scope,'tiny',24)
    body+=f'<path d="M40 608 H1240" class="rule"/>'
    body+=text(40,644,'ORIGINALS STAY ORIGINAL', 'eyebrow')
    body+=text(40,680,'Seven pinned sources · preserve licenses · load selectively · Diagram Design remains independent','small')
    document(slug,'The right specialist for each task',
             'The Design router selects concept, UX, refinement, motion or system resources according to the task.',
             'CODEX DESIGN WORKFLOW / 02 — ROUTING',body)


def setup():
    slug='setup'
    body=text(40,148,'One prompt guides setup. Your accounts and live app connections stay on your computer.','small')
    for x in [40,456]:
        body+=arrow(f'M{x+368} 364 H{x+416}',slug)
    rows=[('01','Install the bundle',['Inspect the task and plan.','Run install + doctor.'],['Design router','Seven pinned upstream sources','Original licenses + hash checks']),
          ('02','Connect your tools',['Install / open BrowserOS Neo.','Pair Codex from its MCP board.'],['Your own local endpoints','Your own account sign-ins','pen.dev + Penpot: manual setup']),
          ('03','Verify real access',['Load the Design skill.','Perform read-only live checks.'],['Files installed ≠ tools connected','Neo: open and read a test page','Design apps: read current state'])]
    for i,(num,title,actions,details) in enumerate(rows):
        x=40+i*416
        body+=rect(x,220,368,336,'focal' if i==0 else 'card')
        body+=text(x+24,260,num,'eyebrow')+text(x+24,308,title,'heading')
        body+=lines(x+24,352,actions)+f'<path d="M{x+24} 408 H{x+344}" class="rule"/>'
        body+=lines(x+24,448,details,'small',32)
    body+=text(40,620,'READY WHEN THE FILES AND THE LIVE CONNECTIONS ARE VERIFIED', 'eyebrow')
    body+=text(40,660,'The installer preserves existing Codex settings and reports skill conflicts.','body')
    body+=text(40,688,'No profiles, credentials, private projects or model settings are transferred.','small')
    document(slug,'Set up your own design environment',
             'Install and verify skills, pair the recipient’s own applications, then prove live tool access.',
             'CODEX DESIGN WORKFLOW / 03 — INSTALLATION',body)


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    workflow(); routing(); setup()
    print('Built workflow, routing and setup HTML sources.')
