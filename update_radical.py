import re

class_beat = """### Class Beats

- **Minor:** Use a forbidden method in front of someone who doesn't know what you are.
- **Major:** Call upon your old faction for help, indebting yourself to them.
- **Severe:** Fully embrace your forbidden nature to solve a problem, confirming everyone's worst fears about you."""

with open('/home/david/.gemini/antigravity/brain/96600c91-3839-4e0d-8c44-c094fd08f702/implementation_plan.md', 'r') as f:
    plan = f.read()

with open('/home/david/Documents/DHSpire/Dark-Heresy-Spire/docs/04-complete-classes-v0.1.md', 'r') as f:
    classes_doc = f.read()

# Extract Radical Asset from plan
sec = re.search(r'### 12\. Radical Asset(.*?)(?=\n\n---|\Z)', plan, re.DOTALL).group(1)
minor = re.search(r'\*\*New Minor:\*\*\n\n(.*?)(?=\n\n\*\*New Major:\*\*|$)', sec, re.DOTALL).group(1).strip()
major = re.search(r'\*\*New Major:\*\*\n\n(.*?)(?=\n\n\*\*New Severe:\*\*|$)', sec, re.DOTALL).group(1).strip()
severe = re.search(r'\*\*New Severe:\*\*\n\n(.*?)(?=\n\n---|\n\n### \d+\.|$)', sec, re.DOTALL).group(1).strip()

# Update classes doc
parts = re.split(r'(?=## \d+\. )', classes_doc)
for i, p in enumerate(parts):
    if '12. Radical Asset' in p:
        lines = p.split('\n')
        idx_minor = lines.index('### Minor Advances')
        idx_major = lines.index('### Major Advances')
        idx_severe = lines.index('### Severe Advances')
        idx_end = lines.index('---', idx_severe)
        
        old_minor = '\n'.join(lines[idx_minor+1:idx_major]).strip()
        old_major = '\n'.join(lines[idx_major+1:idx_severe]).strip()
        old_severe = '\n'.join(lines[idx_severe+1:idx_end]).strip()
        
        new_sec = '\n'.join(lines[:idx_minor]) + '\n'
        new_sec += '### Minor Advances\n\n' + old_minor + '\n\n' + minor + '\n\n'
        new_sec += '### Major Advances\n\n' + old_major + '\n\n' + major + '\n\n'
        new_sec += '### Severe Advances\n\n' + old_severe + '\n\n' + severe + '\n\n'
        new_sec += class_beat + '\n\n'
        new_sec += '\n'.join(lines[idx_end:])
        
        parts[i] = new_sec

with open('/home/david/Documents/DHSpire/Dark-Heresy-Spire/docs/04-complete-classes-v0.1.md', 'w') as f:
    f.write(''.join(parts))

print("Fixed Radical Asset!")
