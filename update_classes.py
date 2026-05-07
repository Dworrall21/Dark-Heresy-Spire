import re

# Class Beats
class_beats = {
    "Legate": """### Class Beats

- **Minor:** Issue an order you know is wrong because the chain of command demands it.
- **Major:** Sacrifice a Contact, Cover, or political asset to shield the cell from institutional consequences.
- **Severe:** Assume full responsibility for something the Patron did, absorbing all fallout personally.""",

    "Explicator": """### Class Beats

- **Minor:** Connect two separate clues into a case file or theory.
- **Major:** Present evidence that changes the cell's understanding of the mission — and forces them to choose a harder path.
- **Severe:** Solve the case, but the answer implicates someone the cell cannot afford to accuse.""",

    "Cruciator": """### Class Beats

- **Minor:** Extract a confession you know is false but still useful.
- **Major:** Break someone who genuinely did not deserve it because the mission required it.
- **Severe:** Interrogate a fellow acolyte, Bond, or ally — and learn something you both wish you hadn't.""",

    "Penumbra": """### Class Beats

- **Minor:** Burn a cover identity to protect someone, or adopt a new one under pressure.
- **Major:** Sacrifice a real relationship to maintain a false one — or vice versa.
- **Severe:** Discover that one of your cover identities has done something terrible while you weren't wearing it.""",

    "Sanctioned Psyker": """### Class Beats

- **Minor:** Push a power slightly too far to achieve a mundane task.
- **Major:** Risk possession or severe warp backlash to save the cell.
- **Severe:** Voluntarily succumb to a warp manifestation to defeat an enemy.""",

    "Exorcist": """### Class Beats

- **Minor:** Perform a time-consuming ritual instead of acting immediately.
- **Major:** Trap a possessing entity at the cost of the victim's life or sanity.
- **Severe:** Take an entity into yourself to save someone else.""",

    "Hierophant": """### Class Beats

- **Minor:** Condemn someone for a minor sin when they were helping you.
- **Major:** Foment a riot, mob, or mass panic using religious authority.
- **Severe:** Declare a miracle that directly challenges the authority of the local Ecclesiarchy.""",

    "Secutor": """### Class Beats

- **Minor:** Escalate a tense situation into violence before the cell is ready.
- **Major:** Absorb a potentially lethal blow meant for another acolyte.
- **Severe:** Hold a position against overwhelming odds, knowing you will likely not survive.""",

    "Chirurgeon": """### Class Beats

- **Minor:** Perform a field procedure that leaves a permanent, visible scar.
- **Major:** Keep someone alive and functioning long past when their body should have failed.
- **Severe:** Use forbidden or xenos biological components to "save" someone.""",

    "Enginseer": """### Class Beats

- **Minor:** Prioritize the safety of a machine over the comfort of a person.
- **Major:** Awaken a dormant, dangerous, or heretical machine-spirit to solve a problem.
- **Severe:** Merge your consciousness with a machine to take direct control, risking your humanity.""",

    "Untouchable": """### Class Beats

- **Minor:** Use your aura to deliberately discomfort or isolate an ally.
- **Major:** Push your null field to its limit, causing physical harm to yourself to stop a warp threat.
- **Severe:** Become the focal point of a psychic attack to drain the caster completely.""",

    "Radical Asset": """### Class Beats

- **Minor:** Use a forbidden method in front of someone who doesn't know what you are.
- **Major:** Call upon your old faction for help, indebting yourself to them.
- **Severe:** Fully embrace your forbidden nature to solve a problem, confirming everyone's worst fears about you."""
}

with open('/home/david/.gemini/antigravity/brain/96600c91-3839-4e0d-8c44-c094fd08f702/implementation_plan.md', 'r') as f:
    plan = f.read()

with open('/home/david/Documents/DHSpire/Dark-Heresy-Spire/docs/04-complete-classes-v0.1.md', 'r') as f:
    classes_doc = f.read()

# Extract new abilities from plan
new_abilities = {}
plan_sections = re.split(r'### \d+\. ', plan)
for sec in plan_sections[1:]:
    lines = sec.split('\n')
    name = lines[0].split(' —')[0].strip()
    
    minor = re.search(r'\*\*New Minor:\*\*\n\n(.*?)(?=\n\n\*\*New Major:\*\*|$)', sec, re.DOTALL)
    major = re.search(r'\*\*New Major:\*\*\n\n(.*?)(?=\n\n\*\*New Severe:\*\*|$)', sec, re.DOTALL)
    severe = re.search(r'\*\*New Severe:\*\*\n\n(.*?)(?=\n\n---|\n\n### \d+\.|$)', sec, re.DOTALL)
    
    new_abilities[name] = {
        'minor': minor.group(1).strip() if minor else "",
        'major': major.group(1).strip() if major else "",
        'severe': severe.group(1).strip() if severe else ""
    }

# Process the classes document
# Split into classes
parts = re.split(r'(?=## \d+\. )', classes_doc)
header = parts[0]
class_sections = parts[1:]

updated_classes = []

for cls_sec in class_sections:
    if "Playtest Notes" in cls_sec:
        updated_classes.append(cls_sec)
        continue
        
    lines = cls_sec.split('\n')
    name = lines[0].replace('## ', '').split('.')[1].strip()
    
    if name not in new_abilities:
        updated_classes.append(cls_sec)
        continue
        
    # Find indices of sections
    try:
        idx_minor = lines.index('### Minor Advances')
        idx_major = lines.index('### Major Advances')
        idx_severe = lines.index('### Severe Advances')
        idx_end = lines.index('---', idx_severe)
    except ValueError as e:
        print(f"Error parsing sections for {name}: {e}")
        updated_classes.append(cls_sec)
        continue

    # Extract existing sections
    old_minor = '\n'.join(lines[idx_minor+1:idx_major]).strip()
    old_major = '\n'.join(lines[idx_major+1:idx_severe]).strip()
    old_severe = '\n'.join(lines[idx_severe+1:idx_end]).strip()
    
    # Reconstruct class section
    new_sec = '\n'.join(lines[:idx_minor]) + '\n'
    new_sec += '### Minor Advances\n\n' + old_minor + '\n\n' + new_abilities[name]['minor'] + '\n\n'
    new_sec += '### Major Advances\n\n' + old_major + '\n\n' + new_abilities[name]['major'] + '\n\n'
    new_sec += '### Severe Advances\n\n' + old_severe + '\n\n' + new_abilities[name]['severe'] + '\n\n'
    new_sec += class_beats[name] + '\n\n'
    new_sec += '\n'.join(lines[idx_end:])
    
    updated_classes.append(new_sec)

# Reassemble document
new_doc = header + ''.join(updated_classes)

with open('/home/david/Documents/DHSpire/Dark-Heresy-Spire/docs/04-complete-classes-v0.1.md', 'w') as f:
    f.write(new_doc)

print("Done updating classes!")
