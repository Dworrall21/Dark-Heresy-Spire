#!/usr/bin/env python3
"""
Dark Heresy Spire — Playtest 9
GM + 4 PCs, "The Saint with the Wrong Shadow"
Seed: 42 (adversarial — not a lucky seed)
"""

import random
import json
from datetime import datetime

SEED = 42
random.seed(SEED)

# ─── DICE HELPERS ───────────────────────────────────────────────────────────────

def r(d): return random.randint(1, d)
def rpool(n): return sorted([r(10) for _ in range(n)], reverse=True)
def apply_diff(pool, diff):
    """Remove highest dice per difficulty. Returns remaining pool."""
    p = list(pool)
    if diff == "Safe": return p
    if diff == "Risky" and p: p.pop(0)
    if diff == "Dangerous" and len(p) >= 2: p.pop(0); p.pop(0)
    elif diff == "Dangerous" and len(p) == 1: p.pop(0)
    if diff == "Impossible":  # Dangerous + always costs
        if len(p) >= 2: p.pop(0); p.pop(0)
        elif len(p) == 1: p.pop(0)
    return p

def result(highest, diff):
    if highest is None or highest == 0:
        return "CRIT_FAIL"
    if diff == "Impossible" and highest >= 8:
        return "SUCCESS_COST"  # even clean rolls cost on Impossible
    if highest == 1: return "CRIT_FAIL"
    if highest <= 5: return "FAIL"
    if highest <= 7: return "SUCCESS_COST"
    if highest <= 9: return "SUCCESS"
    return "CRIT_SUCCESS"

def stress_die(size):
    return r(size)

def fallout_check(resistance_stress):
    """Check if stress triggers fallout. Thresholds: Minor 8+, Moderate 12+, Severe 16+, Critical 20+"""
    if resistance_stress >= 20: return "CRITICAL"
    if resistance_stress >= 16: return "SEVERE"
    if resistance_stress >= 12: return "MODERATE"
    if resistance_stress >= 8: return "MINOR"
    return None

# ─── CHARACTER CREATION ────────────────────────────────────────────────────────

def make_char(name, origin, former_allegiance, char_class, patron_rel,
              cover_id, cover_die, forbidden_edge,
              skills, domains, protection, gear, bonds, core_ability, refresh,
              playstyle, motivation, **kwargs):
    char = {
        "name": name,
        "origin": origin,
        "former_allegiance": former_allegiance,
        "class": char_class,
        "patron_relationship": patron_rel,
        "cover": {"id": cover_id, "die": cover_die},
        "forbidden_edge": forbidden_edge,
        "skills": skills,
        "domains": domains,
        "protection": protection,
        "gear": gear,
        "bonds": bonds,
        "core_ability": core_ability,
        "refresh": refresh,
        "playstyle": playstyle,
        "motivation": motivation,
        "stress": {"Body": 0, "Mind": 0, "Shadow": 0, "Authority": 0, "Corruption": 0},
        "fallout_marks": [],
        "advances": 0,
        "psychic_powers": [],
        "forbidden_methods": [],
    }
    char.update(kwargs)
    return char

# PC 1: KAEL MOURNE — The Tragic (Explicator)
# Playstyle: Emotional arc, moral cost, pushes into danger for truth
# Will take stress to find clues, struggles with what the truth costs
kael = make_char(
    name="Kael Mourn",
    origin="Hive World",
    former_allegiance="Adeptus Administratum",
    char_class="Explicator",
    patron_rel="Potential Interrogator",
    cover_id="Administratum tithe auditor",
    cover_die=6,
    forbidden_edge="Former Cultist",
    skills=["Investigate", "Deceive", "Resist"],
    domains=["Underworld", "Imperium", "Heresy"],
    protection={"Body": 0, "Mind": 1, "Shadow": 0, "Authority": 1, "Corruption": 0},
    gear=[
        {"name": "Steadfast Compact Laspistol", "tags": ["D6 Body", "Concealable", "Reliable"]},
        {"name": "Dependable Cogitator Cipher-Slate", "tags": ["D6", "Traceable"]},
        {"name": "Tried-and-Tested Evidence Kit", "tags": ["D6", "Suspicious"]},
        {"name": "Old cult token (hidden)", "tags": ["Forbidden", "Cult"]},
    ],
    bonds=[
        {"name": "Secutor Vale", "type": "acolyte", "die": 6,
         "positive": "Battlefield loyalty", "negative": "Shell-shocked under surprise"},
        {"name": "Younger brother in Hive Tarsus corpse starch office", "type": "external", "die": 6,
         "positive": "Unconditional trust", "negative": "Vulnerable to leverage"},
        {"name": "The cult Kael betrayed believes he died in the purge", "type": "faction", "die": 8,
         "positive": "Hidden identity", "negative": "Cult may recognize him"},
    ],
    core_ability="The Shape of Guilt: When Kael finds a clue, may ask one extra question: 'What does this imply that no one wants noticed?' Take D3 Mind stress if answer points toward someone powerful.",
    refresh="Remove stress when Kael explains the truth to someone who does not want to hear it.",
    playstyle="Tragic",
    motivation="Kael wants to prove his redemption is real. He'll push into moral danger to find the truth, and he'll take stress to protect others from learning what he did."
)

# PC 2: SEREN VALE — The Winner (Secutor)
# Playstyle: Efficiency, survival, protection stacking, authority use
# Wants to win clean, minimize stress, maximize tactical advantage
seren = make_char(
    name="Seren Vale",
    origin="Warzone",
    former_allegiance="Astra Militarum",
    char_class="Secutor",
    patron_rel="Favored Instrument",
    cover_id="Sanctioned bounty agent",
    cover_die=6,
    forbidden_edge="Hypno-Indoctrinated",
    skills=["Fight", "Move", "Command"],
    domains=["Militarum", "Imperium", "Frontier"],
    protection={"Body": 2, "Mind": 1, "Shadow": 0, "Authority": 0, "Corruption": 0},
    gear=[
        {"name": "Reliable Lasgun", "tags": ["D6 Body", "Loud", "Reliable"]},
        {"name": "Flak Armour", "tags": ["Body Protection 1"]},
        {"name": "Combat Knife", "tags": ["D3 Body", "Silent", "Concealable"]},
        {"name": "Vox-caster", "tags": ["D6", "Traceable"]},
    ],
    bonds=[
        {"name": "Kael Mourn", "type": "acolyte", "die": 6,
         "positive": "Kael once spared Seren during a purge", "negative": "Kael's secrets are a liability"},
        {"name": "Former squadmate Dren Kael", "type": "external", "die": 6,
         "positive": "Safehouse and weapons", "negative": "Guilt and exposure risk"},
        {"name": "Regimental honor", "type": "faction", "die": 6,
         "Positive": "Discipline and courage", "Negative": "Cannot abandon a fight"},
    ],
    core_ability="Shock and Awe: When Seren leads a violent action, gain Mastery on Fight. On a 6-7, the violence is effective but creates witnesses or evidence.",
    refresh="Remove stress when Seren executes a threat before it can become a tragedy.",
    playstyle="Winner",
    motivation="Seren wants the cell to survive and the mission to succeed with minimal casualties. She'll stack advantages before combat and use authority efficiently."
)

# PC 3: LYS THANE — The Combo-Seeker (Penumbra)
# Playstyle: System exploitation, clever builds, Cover mechanics, gear combos
# Wants to find the optimal path, use Cover creatively, exploit tag interactions
lys = make_char(
    name="Lys Thane",
    origin="Voidborn",
    former_allegiance="Underworld Asset",
    char_class="Penumbra",
    patron_rel="Blackmailed Servant",
    cover_id="Chartist vessel factor",
    cover_die=8,
    forbidden_edge="Unregistered Asset Network",
    skills=["Skulk", "Deceive", "Procure"],
    domains=["Void", "Underworld", "Imperium"],
    protection={"Body": 0, "Mind": 0, "Shadow": 1, "Authority": 0, "Corruption": 0},
    gear=[
        {"name": "Stub Revolver", "tags": ["D6 Body", "Concealable", "Loud", "Common"]},
        {"name": "Disguise Kit", "tags": ["Mastery on Cover creation/repair"]},
        {"name": "Signal Jammer", "tags": ["Shadow Protection 1 during surveillance"]},
        {"name": "False papers (multiple)", "tags": ["D6", "Forged"]},
    ],
    bonds=[
        {"name": "Seren Vale", "type": "acolyte", "die": 6,
         "positive": "Mutual respect from shared combat", "negative": "Seren's directness clashes with subtlety"},
        {"name": "Underhive fixer Yarrick", "type": "external", "die": 8,
         "positive": "Unlimited access to contraband", "negative": "Criminal loyalty — expects payment"},
        {"name": "The cell's shared cover story", "type": "faction", "die": 6,
         "positive": "Collective fiction", "negative": "One person's mistake burns everyone"},
    ],
    core_ability="Ghost Protocol: When Lys spends Cover to step down Difficulty, the Cover die does not step down on a roll of 8+. Once per Operation.",
    refresh="Remove stress when Lys burns a false identity and walks away.",
    playstyle="Combo-seeker",
    motivation="Lys wants to find the optimal solution — maximum effect for minimum cost. She'll look for Cover synergies, tag interactions, and creative uses of gear."
)

# PC 4: PYRA VOSS — The Wildcard (Sanctioned Psyker)
# Playstyle: Unpredictable, creative, uses psychic powers, improvises
# Wants to use her powers, will take Corruption for effect, creates chaos
pyra = make_char(
    name="Pyra Voss",
    origin="Schola Progenium",
    former_allegiance="Astra Telepathica",
    char_class="Sanctioned Psyker",
    patron_rel="Secret Weapon",
    cover_id="Pilgrim confessor",
    cover_die=6,
    forbidden_edge="Daemon-Scarred",
    skills=["Resist", "Investigate", "Command"],
    domains=["Ecclesiarchy", "Warp", "Heresy"],
    protection={"Body": 0, "Mind": 1, "Shadow": 0, "Authority": 0, "Corruption": 1},
    gear=[
        {"name": "Needle Pistol", "tags": ["D6 Body", "Silent", "Toxin", "Illegal"]},
        {"name": "Psy-focus", "tags": ["Psychic amplification"]},
        {"name": "Warded Hood", "tags": ["Corruption Protection 1"]},
        {"name": "Sanctioning Brand", "tags": ["Proof of sanctioning"]},
    ],
    bonds=[
        {"name": "Kael Mourn", "type": "acolyte", "die": 6,
         "positive": "Kael understands being marked by the past", "negative": "Both are liabilities to the cell"},
        {"name": "Dead mentor's notes", "type": "faction", "die": 6,
         "positive": "Forbidden insight", "negative": "Possession is evidence of radical association"},
        {"name": "The Warp itself", "type": "faction", "die": 4,
         "positive": "Psychic sensitivity", "negative": "Daemons can sense her back"},
    ],
    core_ability="Disciplined Casting: When Pyra uses a psychic power, she may spend Cover to reduce the Corruption cost by one die step. Once per Operation.",
    refresh="Remove stress when Pyra submits to examination, restraint, or penance.",
    playstyle="Wildcard",
    motivation="Pyra wants to use her powers to help the cell, even at personal cost. She'll take Corruption stress to gain advantages, creating interesting chaos.",
    psychic_powers=["Witch-Sight", "Veil of Unnotice", "Hexagrammic Rebuke"],
    forbidden_methods=["Mind-Scrape"],
)

# ─── PATRON ─────────────────────────────────────────────────────────────────────

patron = {
    "name": "Inquisitor Vael Draven",
    "ordo": "Ordo Hereticus",
    "public_philosophy": "Puritan",
    "private_method": "Containment",
    "mandate": "Identify the source of the miracle, contain or destroy the threat, prevent public knowledge",
    "boons": [
        {"name": "Restricted Archive", "die": 8, "type": "Inquisition"},
        {"name": "Cover Story", "die": 6, "type": "Shadow"},
        {"name": "Sanctum Obscurus", "die": 8, "type": "Safehouse"},
    ],
    "liabilities": [
        {"name": "Demands Discretion", "trigger": "Public authority use or witness trail"},
        {"name": "Paranoid", "trigger": "Unexplained success or missing information"},
        {"name": "Hidden Philosophy", "trigger": "Cell discovers containment preference over destruction"},
    ],
    "patience": 4,
    "red_lines": [
        "Do not publicly deny a miracle without proof",
        "Do not reveal daemonic possibility to civilians",
        "Do not destroy the corpse before confirming the relic",
    ],
}

# ─── MISSION STATE ──────────────────────────────────────────────────────────────

state = {
    "mission": "The Saint with the Wrong Shadow",
    "heat": 2,
    "enemy_awareness": 1,
    "patron_notice": 0,
    "warp_trace": 0,
    "clocks": {
        "Wrong Shadow Awakens": {"current": 1, "max": 6},
        "Public Panic": {"current": 0, "max": 6},
        "Ecclesiarchy Complaint": {"current": 0, "max": 4},
        "Cult Escape Route": {"current": 0, "max": 4},
    },
    "friction_log": [],
    "narrative_log": [],
    "roll_log": [],
}

# ─── LOGGING HELPERS ────────────────────────────────────────────────────────────

def log(text):
    state["narrative_log"].append(text)
    print(text)

def log_roll(who, skill, domain, pool, diff, removed, remaining, highest, result, fiction, mech):
    entry = {
        "who": who, "skill": skill, "domain": domain,
        "pool": pool, "difficulty": diff,
        "removed": removed, "remaining": remaining,
        "highest": highest, "result": result,
        "fiction": fiction, "mechanical": mech,
    }
    state["roll_log"].append(entry)
    removed_str = f"-{diff}({','.join(map(str, removed))})" if removed else diff
    rem_str = ','.join(map(str, remaining)) if remaining else "∅"
    print(f"  {who}: {skill}+{domain} {len(pool)}D10 {removed_str}-> [{rem_str}] = {highest} [{result}]")
    print(f"    → {fiction}")
    if mech: print(f"    → {mech}")

def log_friction(text):
    state["friction_log"].append(text)
    print(f"  ⚠ FRICTION: {text}")

def apply_stress(char, resistance, amount):
    """Apply stress, accounting for Protection."""
    prot = char["protection"].get(resistance, 0)
    absorbed = min(prot, amount)
    applied = amount - absorbed
    if absorbed > 0:
        print(f"    {resistance} Protection {prot} absorbs {absorbed}, {applied} applied")
    char["stress"][resistance] += applied
    total = char["stress"][resistance]
    fo = fallout_check(total)
    if fo:
        print(f"    *** {fo} FALLOUT on {resistance} (stress={total}) ***")
        char["fallout_marks"].append({"resistance": resistance, "severity": fo})
    return applied

def do_roll(char, skill, domain, diff, help_die=0, gear_die=0, mastery=False, cover_step=False):
    """Execute a full roll for a character."""
    pool_size = 1  # base
    if skill in char["skills"]: pool_size += 1
    if domain in char["domains"]: pool_size += 1
    if mastery: pool_size += 1
    pool_size += help_die + gear_die

    pool = rpool(pool_size)
    remaining = apply_diff(pool, diff)

    # Track removed dice for logging
    removed = pool[:len(pool)-len(remaining)] if len(pool) > len(remaining) else []

    highest = remaining[0] if remaining else 0
    res = result(highest, diff)

    return pool, removed, remaining, highest, res

# ─── GM MOVES ───────────────────────────────────────────────────────────────────

def heat_move(heat_level):
    """Return a Heat Move based on the threshold crossed."""
    roll = r(10)
    moves_3 = [
        "A witness talks to the wrong person.",
        "A local official asks for paperwork or explanation.",
        "The enemy notices interference and tightens security.",
        "A faction becomes curious about the cell's Cover Identity.",
        "A Contact asks whether the cell is bringing danger to their door.",
        "A clue becomes time-sensitive because someone else is now looking for it.",
        "Pict-feed, cogitator logs, or vox chatter must be altered before review.",
        "A harmless NPC starts connecting details they should not understand.",
        "A rival investigator, journalist, or savant takes interest.",
        "A Patron Liability twitches: someone asks why the cell is making noise.",
    ]
    moves_6 = [
        "Local law begins looking for the cell, their aliases, or their methods.",
        "The enemy accelerates their timetable.",
        "A rival acolyte cell, faction agent, or hostile investigator appears.",
        "A safehouse, dead drop, Bond, or Contact is watched.",
        "The enemy plants a false victim, false clue, or counter-infiltrator.",
        "The Patron demands an explanation, proof, or cleaner results.",
        "A Cover Identity now requires active maintenance to keep using.",
        "An enemy names one of the cell's methods and prepares against it.",
        "A faction closes doors: Requisitions from them become Risky or Contested.",
        "The next quiet approach becomes Dangerous unless the cell changes tactics.",
    ]
    moves_9 = [
        "The enemy knows the cell is Inquisition or Inquisition-adjacent.",
        "The Operation's quiet objective becomes impossible.",
        "Planetary authorities, nobles, Arbites, Mechanicus, or Ecclesiarchy intervene.",
        "The cell's current Cover Identities are no longer safe.",
        "The Patron threatens disavowal, recall, punishment, or replacement.",
        "The enemy strikes first: ambush, assassination, hostage-taking, or ritual acceleration.",
        "The enemy destroys, moves, or corrupts the Core Clue.",
        "The cell must sacrifice a Bond, Contact, Cover, Resource, or Boon to keep operating.",
        "A public story forms. It is wrong, dangerous, and politically useful to someone.",
        "The Operation becomes a crisis: purge, flee, expose, negotiate, sacrifice, or finish loud.",
    ]
    if heat_level == 3: return moves_3[roll-1], roll
    if heat_level == 6: return moves_6[roll-1], roll
    if heat_level >= 9: return moves_9[roll-1], roll
    return None, roll

def advance_clock(clock_name, amount=1):
    clock = state["clocks"][clock_name]
    old = clock["current"]
    clock["current"] = min(clock["current"] + amount, clock["max"])
    log(f"  Clock — {clock_name}: {old}/{clock['max']} → {clock['current']}/{clock['max']}")
    if clock["current"] >= clock["max"]:
        log(f"  *** CLOCK FULL: {clock_name} — CONSEQUENCE TRIGGERS ***")

# ─── PLAYTEST BEGINS ────────────────────────────────────────────────────────────

log("=" * 80)
log("DARK HERESY SPIRE — PLAYTEST 9")
log("Seed: 42 | GM + 4 PCs")
log("Mission: The Saint with the Wrong Shadow")
log("=" * 80)
log("")

log("## PATRON")
log(f"  {patron['name']} — {patron['ordo']}")
log(f"  Public: {patron['public_philosophy']} | Private: {patron['private_method']}")
log(f"  Patience: {patron['patience']}/6 | Notice: {state['patron_notice']}/3")
log("")

log("## CELL ROSTER")
for char in [kael, seren, lys, pyra]:
    log(f"  {char['name']} — {char['class']} ({char['playstyle']})")
    log(f"    Skills: {', '.join(char['skills'])} | Domains: {', '.join(char['domains'])}")
    log(f"    Cover: {char['cover']['id']} D{char['cover']['die']}")
    log(f"    Protection: Body {char['protection']['Body']}, Mind {char['protection']['Mind']}, "
        f"Shadow {char['protection']['Shadow']}, Authority {char['protection']['Authority']}, "
        f"Corruption {char['protection']['Corruption']}")
    if char.get("psychic_powers"):
        log(f"    Psychic Powers: {', '.join(char['psychic_powers'])}")
    if char.get("forbidden_methods"):
        log(f"    Forbidden Methods: {', '.join(char['forbidden_methods'])}")
    log(f"    Motivation: {char['motivation']}")
    log("")

log("## STARTING STATE")
log(f"  Heat: {state['heat']} | Enemy Awareness: {state['enemy_awareness']} | "
    f"Patron Notice: {state['patron_notice']} | Warp Trace: {state['warp_trace']}")
for name, clock in state["clocks"].items():
    log(f"  Clock — {name}: {clock['current']}/{clock['max']}")
log("")

# ═══════════════════════════════════════════════════════════════════════════════
# OPERATION 1: ENTER THE SHRINE
# ═══════════════════════════════════════════════════════════════════════════════

log("=" * 80)
log("OPERATION 1: Audit of Saint Septima's Ashes")
log("Objective: Establish cover, access the chapel, and observe the miracle.")
log(f"Starting Heat: {state['heat']} | Enemy Awareness: {state['enemy_awareness']}")
log("=" * 80)
log("")

# ─── Situation: The Pilgrim Queue ─────────────────────────────────────────────

log("--- Situation: The Pilgrim Queue ---")
log("Rain-slick devotional plaza outside the chapel. Hundreds of pilgrims wait in line.")
log("A blind pilgrim claims the saint whispered her name. The crowd is fervent, hopeful, and fragile.")
log("")

# Lys uses her Chartist vessel factor cover to enter the plaza
log("Lys Thane approaches the pilgrim queue under her Chartist vessel factor cover,")
log("looking for the candle seller using coded phrases.")
pool, removed, remaining, highest, res = do_roll(lys, "Skulk", "Underworld", "Safe", gear_die=1)
log_roll("Lys", "Skulk", "Underworld", pool, "Safe", removed, remaining, highest, res,
         "Lys slips through the crowd, signal jammer active, scanning for the candle seller.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Lys spots the candle seller — a thin man with blackened fingertips who whispers")
    log("to pilgrims near the front. She notes the coded phrase: 'The last candle casts the truest shadow.'")
    log("She also notices Mira Vorn watching from a broken hab-window across the plaza.")
    state["clues_found"] = ["candle_seller_code", "mira_spotted"]
elif res == "SUCCESS_COST":
    log("Lys finds the candle seller but a cult lookout notices her signal jammer's faint hum.")
    apply_stress(lys, "Shadow", stress_die(6))
    log_friction("Signal jammer's Shadow Protection 1 absorbed some stress, but the lookout is now curious.")
    state["clues_found"] = ["candle_seller_code", "mira_spotted"]
    state["enemy_awareness"] += 1
    log(f"  Enemy Awareness: {state['enemy_awareness']-1} → {state['enemy_awareness']}")
else:
    log("Lys loses the candle seller in the crowd. She'll need another approach.")
    state["clues_found"] = ["mira_spotted"]

log("")

# Kael approaches the blind pilgrim
log("Kael Mourn approaches the blind pilgrir who claims the saint whispered her name.")
pool, removed, remaining, highest, res = do_roll(kael, "Investigate", "Heresy", "Risky")
log_roll("Kael", "Investigate", "Heresy", pool, "Risky", removed, remaining, highest, res,
         "Kael kneels beside the blind pilgrim, asking gentle questions about what the saint said.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("The pilgrim describes how Sella's shadow bent toward her during prayer — not toward the light.")
    log("This is the core clue: the effect responds to devotion, not light.")
    log("Kael also learns the pilgrim has been having the same dream as other healed pilgrims.")
    if "shared_dream" not in state.get("clues_found", []):
        state.setdefault("clues_found", []).append("shared_dream")
    apply_stress(kael, "Mind", stress_die(3))  # the dream description is unsettling
    log("  Kael takes D3 Mind stress from the pilgrim's description of the shared dream.")
elif res == "SUCCESS_COST":
    log("The pilgrim tells Kael about the shadow, but Frater Loam overhears and becomes suspicious.")
    log("Loam makes a note of Kael's questions. Shadow stress.")
    apply_stress(kael, "Shadow", stress_die(6))
    state.setdefault("clues_found", []).append("shadow_bends_to_prayer")
else:
    log("The pilgrim becomes frightened and clams up. Kael gets nothing useful.")
    log("However, he notices the shadow behavior himself — the core clue is never hidden.")
    log("He observes Sella's shadow moving toward prayer from a distance. D3 Corruption from the wrongness.")
    apply_stress(kael, "Corruption", stress_die(3))
    state.setdefault("clues_found", []).append("shadow_bends_to_prayer")

log("")

# Seren secures the perimeter
log("Seren Vale positions herself to watch the chapel exits, ready for trouble.")
pool, removed, remaining, highest, res = do_roll(seren, "Command", "Militarum", "Safe")
log_roll("Seren", "Command", "Militarum", pool, "Safe", removed, remaining, highest, res,
         "Seren identifies sight lines, exit routes, and notes the Arbites snipers watching the pilgrim line.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Seren maps the entire plaza. She notes Marshal Rork's sniper positions and identifies")
    log("three exit routes. She also spots a cult lookout pretending to be a pilgrim.")
    state.setdefault("tactical_notes", []).append("arbites_snipers")
    state.setdefault("tactical_notes", []).append("cult_lookout_spotted")
    log("Seren's preparation will give the cell an advantage in any future combat here.")
else:
    log("Seren gets a general sense of the layout but misses some details.")

log("")

# Pyra uses Witch-Sight to observe the chapel
log("Pyra Voss activates Witch-Sight to observe the chapel from the plaza edge.")
log("Psychic power use: Investigate + Warp, Dangerous (warp risk in a public place).")
pool, removed, remaining, highest, res = do_roll(pyra, "Investigate", "Warp", "Dangerous", mastery=True)
log_roll("Pyra", "Investigate", "Warp", pool, "Dangerous", removed, remaining, highest, res,
         "Pyra's inner eye opens. She sees the warp-echo coiled inside Sella's corpse like a black flame.",
         None)

# Psychic power cost
cor_cost = stress_die(6)  # D6 Corruption on <=7
if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Pyra clearly sees the embryonic warp-echo feeding on devotion. She can feel its hunger.")
    log("She also senses the daemon-scar connection — the shadow recognizes her.")
    apply_stress(pyra, "Corruption", cor_cost)
    state["warp_trace"] += 1
    log(f"  Warp Trace: {state['warp_trace']-1} → {state['warp_trace']}/6")
    state.setdefault("clues_found", []).append("warp_echo_seen")
    state.setdefault("clues_found", []).append("shadow_recognizes_pyra")
    advance_clock("Wrong Shadow Awakens", 1)  # psychic attention feeds it
elif res == "SUCCESS_COST":
    log("Pyra sees the warp-echo but the effort draws its attention. It turns toward her.")
    apply_stress(pyra, "Corruption", cor_cost)
    apply_stress(pyra, "Mind", stress_die(6))
    state["warp_trace"] += 1
    log(f"  Warp Trace: {state['warp_trace']-1} → {state['warp_trace']}/6")
    advance_clock("Wrong Shadow Awakens", 2)  # it noticed her
    state.setdefault("clues_found", []).append("warp_echo_seen")
    state.setdefault("clues_found", []).append("shadow_recognizes_pyra")
    log_friction("Psychic use in public: Warp Trace +1 and Wrong Shadow advances. This is the core tension of psyker play.")
else:
    log("The Witch-Sight flickers. Pyra gets a sense of wrongness but no clear image.")
    log("The shadow still notices the attempt.")
    apply_stress(pyra, "Corruption", cor_cost)
    state["warp_trace"] += 1
    advance_clock("Wrong Shadow Awakens", 1)
    log_friction("Failed psychic roll still advances Warp Trace and Wrong Shadow. The cost of trying is real.")

log("")

# ─── End of Situation 1: First Viewing of the Corpse ─────────────────────────

log("--- Situation: First Viewing of the Corpse ---")
log("The cell enters the chapel reliquary alcove. Frater Loam watches nervously.")
log("Sella's body lies on a stone slab, surrounded by candles. Her shadow moves wrong.")
log("")

# Kael examines the corpse (core clue delivery)
log("Kael Mourn approaches the corpse to examine it. Frater Loam hovers anxiously.")
pool, removed, remaining, highest, res = do_roll(kael, "Investigate", "Heresy", "Risky", gear_die=1)
log_roll("Kael", "Investigate", "Heresy", pool, "Risky", removed, remaining, highest, res,
         "Kael uses his evidence kit to examine Sella's wounds while Frater Loam prays nearby.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Kael finds black glass residue in Sella's chest wound — a shard or bead is inside her body.")
    log("The shadow bends toward the nearest praying pilgrim, not toward the chapel lamps.")
    apply_stress(kael, "Corruption", stress_die(3))  # minor warp exposure
    state.setdefault("clues_found", []).append("black_glass_residue")
    state.setdefault("clues_found", []).append("shadow_bends_to_prayer")
elif res == "SUCCESS_COST":
    log("Kael finds the black residue, but Frater Loam sees him pocket a sample.")
    log("Loam's eyes widen. He says nothing but his hand moves to his vox-bead.")
    apply_stress(kael, "Corruption", stress_die(3))
    apply_stress(kael, "Shadow", stress_die(3))
    state.setdefault("clues_found", []).append("black_glass_residue")
    state.setdefault("clues_found", []).append("shadow_bends_to_prayer")
    log("  Frater Loam is now a complication. He may report to Canoness-Adjunct Vale.")
else:
    log("Kael can't get a clear look — Frater Loam is too watchful. But the core clue is never hidden:")
    log("any pilgrim can tell the cell that the shadow moves toward prayer. Kael learns this from")
    log("a whispered conversation nearby. The clue is free; the cost is that everyone knows it too.")
    state.setdefault("clues_found", []).append("shadow_bends_to_prayer")

log("")

# Lys tries to get Frater Loam's cooperation
log("Lys Thane approaches Frater Loam privately, threatening donation fraud charges.")
pool, removed, remaining, highest, res = do_roll(lys, "Deceive", "Imperium", "Risky")
log_roll("Lys", "Deceive", "Imperium", pool, "Risky", removed, remaining, highest, res,
         "Lys implies she's found irregularities in the chapel's donation records and can make them go away.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Loam cracks. He admits he's been faking minor healings to encourage donations.")
    log("He gives Lys the private corpse schedule and access to the chapel's back rooms.")
    log("He also mentions that Overseer Cale visited the chapel the night Sella died.")
    state.setdefault("clues_found", []).append("loam_cooperation")
    state.setdefault("clues_found", []).append("cale_visited_chapel")
    state.setdefault("clues_found", []).append("loam_fraud")
elif res == "SUCCESS_COST":
    log("Loam cooperates but warns Canoness-Adjunct Vale that the auditors are asking hard questions.")
    state.setdefault("clues_found", []).append("loam_cooperation")
    state.setdefault("clues_found", []).append("cale_visited_chapel")
    advance_clock("Ecclesiarchy Complaint", 1)
    log_friction("Lys got the clue but triggered Ecclesiarchy Complaint. The quiet path has costs too.")
else:
    log("Loam panics and calls for Canoness-Adjunct Vale. The cell now faces ecclesiastical authority.")
    advance_clock("Ecclesiarchy Complaint", 2)
    state["heat"] += 1
    log(f"  Heat: {state['heat']-1} → {state['heat']} (clergy confrontation)")

log("")

# ─── End of Operation 1 ──────────────────────────────────────────────────────

log("--- End of Operation 1 ---")
log("")

# End-of-Operation checklist
log("End-of-Operation Checklist:")
log(f"  1. Did anyone see what happened? Yes — Frater Loam, cult lookout, pilgrims.")
log(f"  2. Did anyone record it? Possible — chapel may have pict-feeds.")
log(f"  3. Did anyone survive with useful information? Yes — Loam cooperated (partially).")
log(f"  4. Was there loud violence? No.")
log(f"  5. Did Cover hold? Mostly — audit cover is plausible but being tested.")
log(f"  6. Did the enemy learn something? Yes — cult knows outsiders are investigating.")
log(f"  7. Did the Patron have reason to notice? Not yet — no public authority used.")
log(f"  8. Did any faction gain reason to intervene? Ecclesiarchy — Loam may have warned Vale.")
log(f"  9. Did evidence remain unsecured? The black glass residue sample Kael took.")
log(f" 10. Was a Red Line approached? No.")

log("")
log(f"  Heat: {state['heat']}")
log(f"  Enemy Awareness: {state['enemy_awareness']}")
log(f"  Patron Notice: {state['patron_notice']}")
log(f"  Warp Trace: {state['warp_trace']}/6")
for name, clock in state["clocks"].items():
    log(f"  Clock — {name}: {clock['current']}/{clock['max']}")

log("")
for char in [kael, seren, lys, pyra]:
    log(f"  {char['name']}: Body={char['stress']['Body']}, Mind={char['stress']['Mind']}, "
        f"Shadow={char['stress']['Shadow']}, Authority={char['stress']['Authority']}, "
        f"Corruption={char['stress']['Corruption']}")
log("")

# Check Heat threshold
if state["heat"] >= 3 and state["heat"] < 6:
    move, roll = heat_move(3)
    log(f"  Heat 3 Threshold — Heat Move (rolled {roll}): {move}")
    if "Patron" in move or "Liability" in move:
        state["patron_notice"] += 1
        log(f"  Patron Notice: {state['patron_notice']-1} → {state['patron_notice']}")

log("")

# ═══════════════════════════════════════════════════════════════════════════════
# OPERATION 2: FOLLOW THE DEAD WOMAN'S LIFE
# ═══════════════════════════════════════════════════════════════════════════════

log("=" * 80)
log("OPERATION 2: Sella Vorn's Last Day")
log("Objective: Reconstruct Sella's movements and identify who wanted the corpse in the chapel.")
log(f"Starting Heat: {state['heat']} | Enemy Awareness: {state['enemy_awareness']}")
log("=" * 80)
log("")

# ─── Situation: The Dormitory Search ──────────────────────────────────────────

log("--- Situation: The Dormitory Search ---")
log("Sella's hab-block dormitory, sealed for sanitation. The room has been searched badly already.")
log("A cult lookout watches from the corridor.")
log("")

# Seren handles the cult lookout
log("Seren Vale spots the cult lookout and moves to intercept quietly.")
pool, removed, remaining, highest, res = do_roll(seren, "Fight", "Militarum", "Risky")
log_roll("Seren", "Fight", "Militarum", pool, "Risky", removed, remaining, highest, res,
         "Seren moves to neutralize the cult lookout before he can raise an alarm.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Seren disarms and restrains the lookout silently. He's a low-level cultist — frightened.")
    log("She gags him and ties him to a pipe. He'll be found eventually, but not soon.")
    state.setdefault("captures", []).append("cult_lookout")
elif res == "SUCCESS_COST":
    log("Seren tackles the lookout but he gets off a vox warning before she silences him.")
    apply_stress(seren, "Body", stress_die(6))
    state["enemy_awareness"] += 1
    log(f"  Enemy Awareness: {state['enemy_awareness']-1} → {state['enemy_awareness']}")
    log("  The cult now knows someone is searching Sella's dormitory.")
    log_friction("The lookout's vox warning is a classic 'success at cost' consequence — the cell got their fight but the enemy knows.")
else:
    log("The lookout spots Seren and flees into the underhive. He'll report to the cult.")
    state["enemy_awareness"] += 1
    advance_clock("Cult Escape Route", 1)
    log(f"  Enemy Awareness: {state['enemy_awareness']-1} → {state['enemy_awareness']}")
    log("  The cult now knows someone is investigating Sella's past.")

log("")

# Kael searches the dormitory
log("Kael Mourn searches Sella's dormitory for clues about her last day.")
pool, removed, remaining, highest, res = do_roll(kael, "Investigate", "Imperium", "Safe", gear_die=1)
log_roll("Kael", "Investigate", "Imperium", pool, "Safe", removed, remaining, highest, res,
         "Kael goes through Sella's belongings with his evidence kit.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Kael finds: a hidden child's charm (Mira's), black dust under a floor grate,")
    log("a transit chit for the chapel district, and a torn chapel token.")
    log("The black dust matches the residue in Sella's wound — the Noctilith Tear.")
    state.setdefault("clues_found", []).append("child_charm")
    state.setdefault("clues_found", []).append("black_dust")
    state.setdefault("clues_found", []).append("transit_chit")
    state.setdefault("clues_found", []).append("chapel_token")
elif res == "SUCCESS_COST":
    log("Kael finds the black dust and transit chit, but the search takes too long.")
    log("A hab neighbor sees him and demands to know if Sella is really a saint or a heretic.")
    apply_stress(kael, "Mind", stress_die(3))
    state.setdefault("clues_found", []).append("black_dust")
    state.setdefault("clues_found", []).append("transit_chit")
else:
    log("The room has been too thoroughly searched. Kael finds only the transit chit.")
    state.setdefault("clues_found", []).append("transit_chit")

log("")

# Lys traces the transit chit
log("Lys Thane uses her Underworld contacts to trace the transit chit.")
pool, removed, remaining, highest, res = do_roll(lys, "Procure", "Underworld", "Risky")
log_roll("Lys", "Procure", "Underworld", pool, "Risky", removed, remaining, highest, res,
         "Lys calls in a favor with her underhive fixer to trace the transit chit's origin.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("The transit chit leads to Overseer Cale's manufactorum. Sella worked there.")
    log("Lys also learns Cale has been asking questions about 'outsiders' in the district.")
    state.setdefault("clues_found", []).append("cale_manufactorum")
    state.setdefault("clues_found", []).append("cale_asking_questions")
elif res == "SUCCESS_COST":
    log("Lys traces the chit to Cale's manufactorum, but her fixer wants payment.")
    log("She owes Yarrick a favor — a D6 debt that will come due later.")
    apply_stress(lys, "Shadow", stress_die(3))
    state.setdefault("clues_found", []).append("cale_manufactorum")
    state.setdefault("debts", []).append("yarrick_favor")
else:
    log("The trail is cold. Lys can't trace the chit through official channels.")
    log("She'll need to find another way to identify Sella's connections.")

log("")

# ─── Situation: Finding Mira ─────────────────────────────────────────────────

log("--- Situation: Finding Mira Vorn ---")
log("The cell learns Mira is hiding in an abandoned ration lift beneath the manufactorum district.")
log("She thinks officials killed her mother. A cult hunter is also looking for her.")
log("")

# Pyra uses Veil of Unnotice to approach Mira's hideout
log("Pyra Voss uses Veil of Unnotice to scout the ration lift area without being seen.")
log("Psychic power: Skulk + Warp, Risky (subtle power, but still warp-touched).")
pool, removed, remaining, highest, res = do_roll(pyra, "Skulk", "Warp", "Risky")
log_roll("Pyra", "Skulk", "Warp", pool, "Risky", removed, remaining, highest, res,
         "Pyra wraps herself in the Veil and slips through the abandoned manufactorum.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Pyra locates Mira in the ration lift. The girl is terrified, alone, and armed with a knife.")
    log("Pyra also spots the cult hunter — a manufactorum enforcer with a shock maul — approaching.")
    apply_stress(pyra, "Corruption", stress_die(3))  # minor cost for subtle power
    state["warp_trace"] += 1
    log(f"  Warp Trace: {state['warp_trace']-1} → {state['warp_trace']}/6")
    state.setdefault("clues_found", []).append("mira_location")
    state.setdefault("clues_found", []).append("cult_hunter_spotted")
elif res == "SUCCESS_COST":
    log("Pyra finds Mira but the Veil flickers as she passes a ward-statue. The cult hunter notices.")
    apply_stress(pyra, "Corruption", stress_die(6))
    state["warp_trace"] += 1
    state.setdefault("clues_found", []).append("mira_location")
    state.setdefault("clues_found", []).append("cult_hunter_spotted")
    log_friction("Veil of Unnotice failing near wards is a good fictional complication — wards should disrupt warp powers.")
else:
    log("The Veil fails. Pyra is visible. The cult hunter spots her and raises the alarm.")
    apply_stress(pyra, "Corruption", stress_die(6))
    state["warp_trace"] += 1
    state["enemy_awareness"] += 1
    log(f"  Enemy Awareness: {state['enemy_awareness']-1} → {state['enemy_awareness']}")
    log("  Pyra can still reach Mira, but the cult hunter is coming.")

log("")

# Kael approaches Mira
log("Kael Mourn approaches Mira Vorn. She's a frightened child who thinks officials killed her mother.")
pool, removed, remaining, highest, res = do_roll(kael, "Command", "Imperium", "Risky")
log_roll("Kael", "Command", "Imperium", pool, "Risky", removed, remaining, highest, res,
         "Kael kneels to Mira's level and tells her he wants to help find out what really happened to Sella.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Mira breaks down. She tells Kael: her mother stole a black bead from Overseer Cale.")
    log("Cale sent men after her. Sella hid in the chapel and died in a panic crush.")
    log("Mira knows the cult phrase: 'The last candle casts the truest shadow.'")
    apply_stress(kael, "Mind", stress_die(3))  # emotional weight of a child's trauma
    state.setdefault("clues_found", []).append("mira_testimony")
    state.setdefault("clues_found", []).append("sella_stole_bead")
    state.setdefault("clues_found", []).append("cult_phrase")
    state.setdefault("clues_found", []).append("cale_sent_men")
elif res == "SUCCESS_COST":
    log("Mira talks but she's traumatized. She tells Kael about the bead and Cale, but she also")
    log("remembers Kael's face as someone who might hurt her. She'll be a reluctant witness.")
    apply_stress(kael, "Mind", stress_die(6))
    state.setdefault("clues_found", []).append("mira_testimony")
    state.setdefault("clues_found", []).append("sella_stole_bead")
    log_friction("Mira's trauma is real — even success has a human cost. This is good design.")
else:
    log("Mira runs. She's too frightened. The cell will need to find another way to get her testimony.")
    log("However, Pyra's earlier scouting means they know where she is. They can try again.")
    state.setdefault("clues_found", []).append("mira_fled")

log("")

# Seren intercepts the cult hunter
if "cult_hunter_spotted" in state.get("clues_found", []):
    log("Seren Vale intercepts the cult hunter before he can reach Mira.")
    pool, removed, remaining, highest, res = do_roll(seren, "Fight", "Militarum", "Risky")
    log_roll("Seren", "Fight", "Militarum", pool, "Risky", removed, remaining, highest, res,
             "Seren engages the cult hunter in the abandoned ration lift.",
             None)

    if res in ["SUCCESS", "CRIT_SUCCESS"]:
        log("Seren disarms the cult hunter and knocks him unconscious. Clean takedown.")
        log("She confiscates his shock maul and finds a cult token on him.")
        state.setdefault("captures", []).append("cult_hunter")
        state.setdefault("clues_found", []).append("cult_hunter_token")
    elif res == "SUCCESS_COST":
        log("Seren wins the fight but takes a shock maul hit. The hunter escapes into the underhive.")
        apply_stress(seren, "Body", stress_die(6))
        state["enemy_awareness"] += 1
        advance_clock("Cult Escape Route", 1)
        log(f"  Enemy Awareness: {state['enemy_awareness']-1} → {state['enemy_awareness']}")
    else:
        log("The cult hunter fights hard and escapes. He'll report to Cale.")
        state["enemy_awareness"] += 1
        advance_clock("Cult Escape Route", 2)
        log(f"  Enemy Awareness: {state['enemy_awareness']-1} → {state['enemy_awareness']}")

log("")

# ─── End of Operation 2 ──────────────────────────────────────────────────────

log("--- End of Operation 2 ---")
log("")

log("End-of-Operation Checklist:")
log(f"  1. Did anyone see what happened? Yes — hab neighbors, cult lookout, cult hunter.")
log(f"  2. Did anyone record it? Unlikely in the underhive.")
log(f"  3. Did anyone survive with useful information? Yes — captured cult lookout/hunter.")
log(f"  4. Was there loud violence? Minor — Seren's fight with the cult hunter.")
log(f"  5. Did Cover hold? The audit cover is weakening — Cale knows outsiders are asking questions.")
log(f"  6. Did the enemy learn something? Yes — Cale knows someone is investigating Sella.")
log(f"  7. Did the Patron have reason to notice? Not yet.")
log(f"  8. Did any faction gain reason to intervene? The cult is now actively hunting the cell.")
log(f"  9. Did evidence remain unsecured? The cult hunter's token, Mira's testimony.")
log(f" 10. Was a Red Line approached? No.")

log("")
log(f"  Heat: {state['heat']}")
log(f"  Enemy Awareness: {state['enemy_awareness']}")
log(f"  Patron Notice: {state['patron_notice']}")
log(f"  Warp Trace: {state['warp_trace']}/6")
for name, clock in state["clocks"].items():
    log(f"  Clock — {name}: {clock['current']}/{clock['max']}")

log("")
for char in [kael, seren, lys, pyra]:
    log(f"  {char['name']}: Body={char['stress']['Body']}, Mind={char['stress']['Mind']}, "
        f"Shadow={char['stress']['Shadow']}, Authority={char['stress']['Authority']}, "
        f"Corruption={char['stress']['Corruption']}")
log("")

# Check Heat threshold
if state["heat"] >= 3 and state["heat"] < 6:
    move, roll = heat_move(3)
    log(f"  Heat 3 Threshold — Heat Move (rolled {roll}): {move}")
    if state["heat"] >= 6:
        move, roll = heat_move(6)
        log(f"  Heat 6 Threshold — Heat Move (rolled {roll}): {move}")

log("")

# ═══════════════════════════════════════════════════════════════════════════════
# OPERATION 3: BREAK THE CHOIR
# ═══════════════════════════════════════════════════════════════════════════════

log("=" * 80)
log("OPERATION 3: The Last Candle")
log("Objective: Identify and disrupt the Choir of the Last Candle before the mass vigil.")
log(f"Starting Heat: {state['heat']} | Enemy Awareness: {state['enemy_awareness']}")
log("=" * 80)
log("")

# ─── Situation: Cult Meeting in the Candle-Vault ─────────────────────────────

log("--- Situation: Cult Meeting in the Candle-Vault ---")
log("Wax storage chamber beneath the manufactorum chapel annex. Cale, three cult faithful,")
log("one marked pilgrim, and a hidden worker. The cult is deciding whether to kill Mira or use her.")
log("")

# Lys infiltrates the cult meeting
log("Lys Thane infiltrates the candle-vault during the cult meeting, disguised as a new recruit.")
pool, removed, remaining, highest, res = do_roll(lys, "Deceive", "Heresy", "Dangerous")
log_roll("Lys", "Deceive", "Heresy", pool, "Dangerous", removed, remaining, highest, res,
         "Lys uses the cult phrase and her forged credentials to pose as a sympathizer.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Lys is accepted into the meeting. She learns: the mass vigil is tomorrow at dusk.")
    log("The cult plans to use Mira as a 'prayer anchor' — her blood connection to Sella will")
    log("strengthen the wrong shadow. Overseer Cale is the cult's patron.")
    log("She also learns about Sister Ashen, the ritual leader.")
    state.setdefault("clues_found", []).append("mass_vigil_tomorrow")
    state.setdefault("clues_found", []).append("mira_prayer_anchor")
    state.setdefault("clues_found", []).append("sister_ashen")
    state.setdefault("clues_found", []).append("cale_cult_patron")
elif res == "SUCCESS_COST":
    log("Lys gets into the meeting but Cale recognizes something off about her.")
    log("He doesn't expose her immediately but assigns a cultist to watch her.")
    apply_stress(lys, "Shadow", stress_die(6))
    state.setdefault("clues_found", []).append("mass_vigil_tomorrow")
    state.setdefault("clues_found", []).append("cale_suspicious")
    log_friction("Cale's suspicion is a ticking time bomb — Lys got the clue but created a future problem.")
else:
    log("Lys's cover is blown. Cale recognizes her as an outsider. The cult moves to seize her.")
    apply_stress(lys, "Shadow", stress_die(6))
    state["heat"] += 1
    log(f"  Heat: {state['heat']-1} → {state['heat']} (cover blown)")
    log("  Lys fights her way out — the cult meeting becomes a combat.")

log("")

# Kael interrogates the captured cult lookout
log("Kael Mourn interrogates the captured cult lookout about the Choir's structure.")
pool, removed, remaining, highest, res = do_roll(kael, "Investigate", "Heresy", "Risky")
log_roll("Kael", "Investigate", "Heresy", pool, "Risky", removed, remaining, highest, res,
         "Kael questions the frightened cultist about the Choir's leadership and plans.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("The lookout breaks. He tells Kael about Sister Ashen, the candle-vault meetings,")
    log("and the plan to awaken the wrong shadow during the mass vigil.")
    log("He also reveals: the Noctilith Tear is one of two fragments. The second is hidden.")
    apply_stress(kael, "Mind", stress_die(3))  # moral weight of interrogation
    state.setdefault("clues_found", []).append("choir_structure")
    state.setdefault("clues_found", []).append("second_fragment")
elif res == "SUCCESS_COST":
    log("The lookout talks but gives one true answer and one lie to protect the cult.")
    log("Kael gets the meeting location but the lookout lies about the ritual timing.")
    apply_stress(kael, "Mind", stress_die(3))
    state.setdefault("clues_found", []).append("choir_structure")
    log_friction("The 'one true, one lie' pattern is good for interrogation — players must verify information.")
else:
    log("The lookout refuses to talk. He's too afraid of Sister Ashen.")
    log("Kael learns nothing from this source.")

log("")

# Pyra uses Witch-Sight on the marked pilgrim
log("Pyra Voss uses Witch-Sight on the marked pilgrim found in the candle-vault.")
log("Psychic power: Investigate + Warp, Dangerous.")
pool, removed, remaining, highest, res = do_roll(pyra, "Investigate", "Warp", "Dangerous", mastery=True)
log_roll("Pyra", "Investigate", "Warp", pool, "Dangerous", removed, remaining, highest, res,
         "Pyra examines the marked pilgrim's warp signature.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Pyra sees the shadow-mark under the pilgrim's tongue — a warp-brand connecting")
    log("him to the wrong shadow. He's a living relay. She also senses the shared dream network:")
    log("dozens of pilgrims are psychically linked through the shadow.")
    apply_stress(pyra, "Corruption", stress_die(6))
    state["warp_trace"] += 1
    log(f"  Warp Trace: {state['warp_trace']-1} → {state['warp_trace']}/6")
    state.setdefault("clues_found", []).append("shadow_mark")
    state.setdefault("clues_found", []).append("dream_network")
    advance_clock("Wrong Shadow Awakens", 1)
elif res == "SUCCESS_COST":
    log("Pyra sees the shadow-mark but the wrong shadow pushes back through the connection.")
    log("For a moment, she feels its hunger directly. D8 Corruption.")
    apply_stress(pyra, "Corruption", stress_die(8))
    apply_stress(pyra, "Mind", stress_die(6))
    state["warp_trace"] += 1
    advance_clock("Wrong Shadow Awakens", 2)
    state.setdefault("clues_found", []).append("shadow_mark")
    log_friction("The wrong shadow fighting back through Witch-Sight is excellent horror — the tool that reveals also exposes.")
else:
    log("The Witch-Sight is blocked — the shadow has warded the pilgrim.")
    apply_stress(pyra, "Corruption", stress_die(6))
    state["warp_trace"] += 1
    log("Pyra learns nothing but the attempt still feeds the shadow.")

log("")

# Seren prepares the tactical approach
log("Seren Vale plans the cell's approach to disrupting the mass vigil.")
pool, removed, remaining, highest, res = do_roll(seren, "Command", "Militarum", "Safe")
log_roll("Seren", "Command", "Militarum", pool, "Safe", removed, remaining, highest, res,
         "Seren maps the chapel's defensive positions and plans the cell's approach.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Seren identifies: the chapel has three exits, the cult has four enforcers in the crowd,")
    log("and the mass vigil will pack 200+ pilgrims into a space meant for 80.")
    log("She plans a two-pronged approach: Lys infiltrates, Seren handles enforcers,")
    log("Kael secures Mira, Pyra contains the shadow.")
    state.setdefault("tactical_plan", []).append("two_pronged")
    state.setdefault("tactical_plan", []).append("infiltration_route")
elif res == "SUCCESS_COST":
    log("Seren plans the approach but realizes the Arbites cordon will complicate extraction.")
    apply_stress(seren, "Mind", stress_die(3))
    state.setdefault("tactical_plan", []).append("arbites_complication")
else:
    log("The situation is too chaotic for a clean plan. The cell will need to improvise.")

log("")

# ─── End of Operation 3 ──────────────────────────────────────────────────────

log("--- End of Operation 3 ---")
log("")

log("End-of-Operation Checklist:")
log(f"  1. Did anyone see what happened? Yes — cult members, marked pilgrim.")
log(f"  2. Did anyone recorded it? Possible — cult may have pict records.")
log(f"  3. Did anyone survive with useful information? Yes — captured lookout, marked pilgrim.")
log(f"  4. Was there loud violence? Minor — Lys's escape if cover was blown.")
log(f"  5. Did Cover hold? Barely — Cale is suspicious, cult knows outsiders are close.")
log(f"  6. Did the enemy learn something? Yes — cult knows the cell is closing in.")
log(f"  7. Did the Patron have reason to notice? Not yet — no public authority used.")
log(f"  8. Did any faction gain reason to intervene? The cult is now in active defense mode.")
log(f"  9. Did evidence remain unsecured? The marked pilgrim, cult tokens, second fragment clue.")
log(f" 10. Was a Red Line approached? No.")

log("")
log(f"  Heat: {state['heat']}")
log(f"  Enemy Awareness: {state['enemy_awareness']}")
log(f"  Patron Notice: {state['patron_notice']}")
log(f"  Warp Trace: {state['warp_trace']}/6")
for name, clock in state["clocks"].items():
    log(f"  Clock — {name}: {clock['current']}/{clock['max']}")

log("")
for char in [kael, seren, lys, pyra]:
    log(f"  {char['name']}: Body={char['stress']['Body']}, Mind={char['stress']['Mind']}, "
        f"Shadow={char['stress']['Shadow']}, Authority={char['stress']['Authority']}, "
        f"Corruption={char['stress']['Corruption']}")
log("")

# Check Heat thresholds
if state["heat"] >= 3 and state["heat"] < 6:
    move, roll = heat_move(3)
    log(f"  Heat 3 Threshold — Heat Move (rolled {roll}): {move}")
if state["heat"] >= 6:
    move, roll = heat_move(6)
    log(f"  Heat 6 Threshold — Heat Move (rolled {roll}): {move}")
    if "AMBUSH" in move or "enemy" in move.lower():
        log("  *** CONDITIONAL AMBUSH CHECK ***")
        log(f"  Heat: {state['heat']}, Enemy Awareness: {state['enemy_awareness']}")
        if state["enemy_awareness"] >= 4:
            log("  Enemy Awareness 4+ — Ambush triggers if cell is in vulnerable position!")
        else:
            log("  Enemy Awareness < 4 — No ambush, but the threat is present.")

log("")

# ═══════════════════════════════════════════════════════════════════════════════
# OPERATION 4: DECIDE THE MIRACLE
# ═══════════════════════════════════════════════════════════════════════════════

log("=" * 80)
log("OPERATION 4: The Wrong Shadow")
log("Objective: Contain, destroy, exploit, or bury the miracle.")
log(f"Starting Heat: {state['heat']} | Enemy Awareness: {state['enemy_awareness']}")
log("=" * 80)
log("")

# ─── Situation: Mass Vigil ───────────────────────────────────────────────────

log("--- Situation: The Mass Vigil ---")
log("Chapel nave, packed beyond safety limits. 200+ pilgrims crowd the space.")
log("The wrong shadow stirs beneath Sella's skin. The cult begins the rite.")
log("Canoness-Adjunct Vale presides. Marshal Rork's Arbites wait outside.")
log("")

# The cell's plan: Lys infiltrates to disrupt the rite, Seren handles cult enforcers,
# Kael secures Mira, Pyra contains the shadow

# Lys disrupts the rite from within
log("Lys Thane, positioned among the pilgrims, moves to disrupt the cult's devotional focus.")
pool, removed, remaining, highest, res = do_roll(lys, "Skulk", "Underworld", "Dangerous")
log_roll("Lys", "Skulk", "Underworld", pool, "Dangerous", removed, remaining, highest, res,
         "Lys works through the crowd toward the cult's candle-array, planning to replace it with a warded decoy.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Lys successfully replaces the cult's devotional candles with warded decoys.")
    log("The rite's power source is disrupted. The wrong shadow's awakening slows.")
    advance_clock("Wrong Shadow Awakens", -1)  # disruption
    log("  Wrong Shadow Awakens clock reduced by 1!")
elif res == "SUCCESS_COST":
    log("Lys plants the decoys but a cult enforcer spots her. She must fight in the crowd.")
    apply_stress(lys, "Body", stress_die(6))
    apply_stress(lys, "Shadow", stress_die(6))
    advance_clock("Public Panic", 1)
    state["heat"] += 1
    log(f"  Heat: {state['heat']-1} → {state['heat']} (fight in crowd)")
else:
    log("Lys is caught by the cult enforcer. The rite proceeds unhindered.")
    apply_stress(lys, "Body", stress_die(6))
    advance_clock("Wrong Shadow Awakens", 2)
    state["heat"] += 1
    log(f"  Heat: {state['heat']-1} → {state['heat']}")

log("")

# Seren handles the cult enforcers
log("Seren Vale engages the cult enforcers before they can stop Lys.")
pool, removed, remaining, highest, res = do_roll(seren, "Fight", "Militarum", "Risky")
log_roll("Seren", "Fight", "Militarum", pool, "Risky", removed, remaining, highest, res,
         "Seren moves to neutralize the cult enforcers in the chapel.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Seren takes down two cult enforcers with precise, controlled violence.")
    log("The crowd doesn't notice — she makes it look like a pilgrim collapse.")
    log("Her Body Protection 2 absorbs the glancing blow from a third enforcer.")
elif res == "SUCCESS_COST":
    log("Seren fights the enforcers but it's messy. A pilgrim is injured in the scuffle.")
    apply_stress(seren, "Body", stress_die(6))
    apply_stress(seren, "Mind", stress_die(3))  # civilian harm
    advance_clock("Public Panic", 1)
    log_friction("Civilian harm during chapel fight — this is the 'Prepare or Suffer' principle in action.")
else:
    log("The enforcers overwhelm Seren. She's pinned. The cult's rite continues.")
    apply_stress(seren, "Body", stress_die(8))
    advance_clock("Wrong Shadow Awakens", 1)

log("")

# Kael secures Mira
log("Kael Mourn reaches Mira, who's been brought to the chapel by the cult as a 'prayer anchor.'")
pool, removed, remaining, highest, res = do_roll(kael, "Command", "Imperium", "Dangerous")
log_roll("Kael", "Command", "Imperium", pool, "Dangerous", removed, remaining, highest, res,
         "Kael pushes through the crowd to reach Mira before the cult can use her.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Kael reaches Mira and shields her. He uses his body to block the cult's attempt")
    log("to draw blood from her. The girl is safe — for now.")
    apply_stress(kael, "Body", stress_die(3))  # physical shielding
elif res == "SUCCESS_COST":
    log("Kael reaches Mira but the cult has already drawn a drop of her blood.")
    log("The wrong shadow surges. Kael shields Mira from the worst of it.")
    apply_stress(kael, "Body", stress_die(6))
    apply_stress(kael, "Corruption", stress_die(3))
    advance_clock("Wrong Shadow Awakens", 1)
else:
    log("The crowd is too thick. Kael can't reach Mira in time.")
    log("The cult uses her blood in the rite. The wrong shadow awakens.")
    advance_clock("Wrong Shadow Awakens", 2)
    apply_stress(kael, "Mind", stress_die(6))  # guilt

log("")

# Pyra contains the shadow
log("Pyra Voss uses Hexagrammic Rebuke to contain the wrong shadow.")
log("Psychic power: Fight + Warp, Dangerous. This is the big one.")
pool, removed, remaining, highest, res = do_roll(pyra, "Fight", "Warp", "Dangerous", mastery=True)
log_roll("Pyra", "Fight", "Warp", pool, "Dangerous", removed, remaining, highest, res,
         "Pyra channels the Hexagrammic Rebuke — golden fire that burns the warp-echo.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("The Hexagrammic Rebuke sears the wrong shadow. It screams through Sella's corpse.")
    log("The warp-echo is contained — not destroyed, but bound. The Noctilith Tear cracks.")
    log("Pyra's daemon-scar burns. The shadow knows her now.")
    apply_stress(pyra, "Corruption", stress_die(8))
    apply_stress(pyra, "Mind", stress_die(6))
    state["warp_trace"] += 2
    log(f"  Warp Trace: {state['warp_trace']-2} → {state['warp_trace']}/6")
    state.setdefault("clues_found", []).append("shadow_contained")
elif res == "SUCCESS_COST":
    log("The Rebuke works but the shadow fights back. Pyra contains it partially.")
    log("The Noctilith Tear cracks but doesn't shatter. The shadow is wounded, not bound.")
    apply_stress(pyra, "Corruption", stress_die(10))
    apply_stress(pyra, "Mind", stress_die(8))
    state["warp_trace"] += 2
    log(f"  Warp Trace: {state['warp_trace']-2} → {state['warp_trace']}/6")
    log_friction("D10 Corruption on a psyker is brutal but appropriate for a daemon-shadow fight.")
    state.setdefault("clues_found", []).append("shadow_wounded")
else:
    log("The Rebuke fails. The wrong shadow surges through the chapel.")
    log("Sella's corpse sits up. The shadow speaks: 'I am the saint you wanted.'")
    apply_stress(pyra, "Corruption", stress_die(10))
    apply_stress(pyra, "Mind", stress_die(10))
    state["warp_trace"] += 2
    advance_clock("Wrong Shadow Awakens", 3)
    advance_clock("Public Panic", 2)
    state["heat"] += 2
    log(f"  Heat: {state['heat']-2} → {state['heat']} (mass psychic event)")
    log("  *** The wrong shadow speaks publicly. This is the disaster route. ***")

log("")

# ─── The Relic Extraction ────────────────────────────────────────────────────

log("--- The Relic Extraction ---")
log("With the shadow contained (or not), the cell must extract the Noctilith Tear.")
log("")

# Kael performs the extraction
log("Kael Mourn cuts into Sella's corpse to extract the Noctilith Tear.")
pool, removed, remaining, highest, res = do_roll(kael, "Investigate", "Heresy", "Dangerous", gear_die=1)
log_roll("Kael", "Investigate", "Heresy", pool, "Dangerous", removed, remaining, highest, res,
         "Kael uses his evidence kit to carefully extract the black glass bead from Sella's chest wound.",
         None)

if res in ["SUCCESS", "CRIT_SUCCESS"]:
    log("Kael extracts the Noctilith Tear cleanly. It's a black glass bead, warm to the touch.")
    log("He places it in a warded containment case (requisitioned earlier).")
    apply_stress(kael, "Corruption", stress_die(3))
    state.setdefault("clues_found", []).append("relic_extracted")
elif res == "SUCCESS_COST":
    log("Kael extracts the Tear but the process is messy. Black fluid spills.")
    log("A pilgrim sees and screams. The crowd panics.")
    apply_stress(kael, "Corruption", stress_die(6))
    advance_clock("Public Panic", 1)
    state["heat"] += 1
    log(f"  Heat: {state['heat']-1} → {state['heat']}")
    state.setdefault("clues_found", []).append("relic_extracted")
else:
    log("The Tear resists extraction. It's fused with Sella's ribcage.")
    log("Kael must choose: leave it, destroy the corpse, or use a forbidden method.")
    log("He chooses to use the Excruciator Protocol on the corpse to loosen the relic.")
    apply_stress(kael, "Mind", stress_die(6))
    apply_stress(kael, "Corruption", stress_die(6))
    state.setdefault("clues_found", []).append("relic_extracted_forbidden")
    log_friction("Using forbidden methods on a corpse in a chapel — this is exactly the kind of choice the system should create.")

log("")

# ─── End of Operation 4 ──────────────────────────────────────────────────────

log("--- End of Operation 4 ---")
log("")

log("End-of-Operation Checklist:")
log(f"  1. Did anyone see what happened? Yes — the entire chapel witnessed the psychic battle.")
log(f"  2. Did anyone record it? Almost certainly — pilgrims with pict-recorders.")
log(f"  3. Did anyone survive with useful information? Yes — Mira, captured cultists.")
log(f"  4. Was there loud violence? Yes — psychic battle, cult enforcer fight, possible corpse desecration.")
log(f"  5. Did Cover hold? No — the audit cover is burned.")
log(f"  6. Did the enemy learn something? Yes — the cult knows the cell's capabilities.")
log(f"  7. Did the Patron have reason to notice? Yes — psychic phenomena, possible public exposure.")
log(f"  8. Did any faction gain reason to intervene? Ecclesiarchy, Arbites, possibly Mechanicus.")
log(f"  9. Did evidence remain unsecured? The Noctilith Tear (contained), Sella's corpse, cult tokens.")
log(f" 10. Was a Red Line approached? Possibly — depending on how the extraction was handled.")

log("")

# ─── Patron Notice Check ─────────────────────────────────────────────────────

log("--- Patron Debrief ---")
state["patron_notice"] += 2  # psychic use + public exposure
log(f"Patron Notice: {state['patron_notice']-2} → {state['patron_notice']}")
if state["patron_notice"] >= 3:
    patron_roll = r(10)
    patron_moves = {
        1: "Commendation: Gain a D8 Requisition for the next Operation.",
        2: "Correction: The Patron issues a new restriction — no more psychic powers in public shrines.",
        3: "Audit: A savant observes the cell's next Operation.",
        4: "Escalation: The Patron reveals the threat is worse — there are more Noctilith fragments.",
        5: "Demand: The Patron requires the Noctilith Tear delivered immediately.",
        6: "Suspicion: Each acolyte who completed a Radical Beat marks D3 Authority or Shadow stress.",
        7: "Doctrine: The Patron forbids daemonological methods and endorses purging.",
        8: "Requisition Freeze: One Boon cannot be used until the cell explains itself.",
        9: "Rival Cell: Another cell is assigned to the same theater.",
        10: "Forbidden Offer: The Patron offers a powerful but compromising solution for the next mission.",
    }
    log(f"Patron Move (rolled {patron_roll}): {patron_moves[patron_roll]}")
    state["patron_notice"] = 0

log("")

# ═══════════════════════════════════════════════════════════════════════════════
# FINAL STATE
# ═══════════════════════════════════════════════════════════════════════════════

log("=" * 80)
log("FINAL STATE")
log("=" * 80)
log("")

log(f"  Heat: {state['heat']}")
log(f"  Enemy Awareness: {state['enemy_awareness']}")
log(f"  Patron Notice: {state['patron_notice']}")
log(f"  Warp Trace: {state['warp_trace']}/6")
for name, clock in state["clocks"].items():
    log(f"  Clock — {name}: {clock['current']}/{clock['max']}")
    if clock["current"] >= clock["max"]:
        log(f"    *** FULL ***")

log("")
log("  Character Stress:")
for char in [kael, seren, lys, pyra]:
    total = sum(char["stress"].values())
    fo = ", ".join([f"{f['resistance']}({f['severity']})" for f in char["fallout_marks"]]) or "None"
    log(f"    {char['name']}: Body={char['stress']['Body']}, Mind={char['stress']['Mind']}, "
        f"Shadow={char['stress']['Shadow']}, Authority={char['stress']['Authority']}, "
        f"Corruption={char['stress']['Corruption']} | Total: {total} | Fallout: {fo}")

log("")
log(f"  Clues Found: {state.get('clues_found', [])}")
log(f"  Captures: {state.get('captures', [])}")
log(f"  Tactical Notes: {state.get('tactical_notes', [])}")
log(f"  Debts: {state.get('debts', [])}")

# ─── MISSION OUTCOME ──────────────────────────────────────────────────────────

log("")
log("=" * 80)
log("MISSION OUTCOME")
log("=" * 80)
log("")

relic_extracted = "relic_extracted" in state.get("clues_found", []) or "relic_extracted_forbidden" in state.get("clues_found", [])
shadow_contained = "shadow_contained" in state.get("clues_found", []) or "shadow_wounded" in state.get("clues_found", [])
mira_safe = "mira_testimony" in state.get("clues_found", [])
heat_final = state["heat"]

if relic_extracted and shadow_contained and mira_safe and heat_final < 9:
    log("PARTIAL SUCCESS — The Noctilith Tear is contained, the shadow is wounded,")
    log("and Mira is safe. But the operation was not quiet. Heat is high.")
    log("The Ecclesiarchy is angry. The cult's leadership may have escaped.")
    log("The Patron is watching more closely now.")
elif relic_extracted and heat_final >= 9:
    log("MESSY SUCCESS — The relic is contained but the operation is burned.")
    log("Public panic, Ecclesiarchy intervention, and Patron scrutiny.")
    log("The cell survived but their cover in this district is destroyed.")
else:
    log("PARTIAL FAILURE — The relic was not fully contained or the shadow escaped.")
    log("The wrong shadow's influence remains in the district.")
    log("The Patron is displeased. The next mission starts at higher Heat.")

log("")
log("=" * 80)
log("END OF PLAYTEST 9")
log("=" * 80)

# Save state to JSON
with open("/home/david/Dark-Heresy-Spire/docs/simulation/playtest9_state.json", "w") as f:
    json.dump(state, f, indent=2)

print("\nState saved to playtest9_state.json")
