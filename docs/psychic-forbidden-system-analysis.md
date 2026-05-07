# Psychic Powers & Forbidden Methods — System Position Analysis

## Overview

Psychic powers and forbidden methods are NOT isolated subsystems bolted onto the core
game. They sit at the intersection of every major system, acting as force multipliers
that create pressure across multiple tracks simultaneously. This analysis maps every
connection.

---

## 1. Core Roll System

**Connection: Complete integration.** Psychic powers and forbidden methods use the same
core roll engine as every other action: pool (Skill + Domain + Mastery + Help + Gear)
minus Difficulty (Safe/Risky/Dangerous/Imposed) read against the standard result table
(10/Crit Success, 8-9/Success, 6-7/Cost, 2-5/Fail, 1/Crit Fail).

The power or method defines the Skill + Domain + cost. Everything else is shared.

| Subsystem | Standard Action | Psychic Power | Forbidden Method |
|-----------|----------------|---------------|-----------------|
| Roll | Skill+Domain pool | Skill+Domain pool | Skill+Domain pool |
| Difficulty | Safe/Dangerous/etc. | Same + calibration table (Safe=prepared/sanctioned, Dangerous=hostile wards, Impossible=daemonic opposition) | Same + certainty option (no roll, just cost) |
| Result table | 10/8-9/6-7/2-5/1 | Same | Same + result bands for method outcomes |
| Stress | Per threat level (D3-D10) | Specified per power (usually Corruption) | Per method cost die |
| Mastery | +1D10 if skill/domain mastered | Same; psyker Mastery on Warp is common | Same |

**Key difference:** Psychic powers add a secondary stress track (Corruption on ≤7,
Burdens on 1) that standard actions don't have. Forbidden methods add tag-driven
pressure selection (Heat, EA, Patron Notice, clocks) that standard actions resolve
through the GM's general judgment.

---

## 2. Resistances (5-track stress system)

**Connection: Primary stress target.** Psychic powers stress Corruption and Mind.
Forbidden methods stress Authority, Shadow, and Corruption. Each interaction with
a different Resistance:

| Source | Primary Stress | Secondary Stress | Why It Matters |
|--------|---------------|-----------------|----------------|
| Psychic power (standard) | Corruption | Mind | Warp contact taints the soul |
| Psychic power (Invasive) | Mind | Corruption | Mental intrusion damages the mind first |
| Psychic power (Violent) | Body | Corruption | Backlash through the flesh |
| Psychic power (Ward) | Mind (on failure) | — | Wards strain the mind when broken |
| Forbidden Method (Authority) | Authority | Shadow | Using power you shouldn't have |
| Forbidden Method (Daemonological) | Corruption | — | Direct warp contact |
| Forbidden Method (Heretek) | Authority | Corruption | Machine blasphemy |
| Forbidden Method (Political) | Authority | Mind | Dangerous bargains |
| Forbidden Method (Memory Work) | Mind + Corruption | — | Soul-level tampering |
| Warp Trace clock (at 6/6) | Corruption (D3 to all) | Every Resistance | The accumulated taint presses on everyone |

**Design implication:** The Resistance system is the single integrating structure.
Psychic powers attack Corruption first, forbidden methods attack Authority first.
This means psykers degrade along a different axis than radicals, which creates
different narrative arcs and different end-game conditions.

**Corruption is the special Resistance:** It is the only one that has its own
Fallout table with unique consequences (warp-touched flesh, possession, daemonic
marks), its own clock (Warp Trace), and its own spiral mechanic (Corruption stress
at low Resistance values triggers fallout faster). This makes Corruption the
"canary in the coal mine" for the psychic/forbidden subsystem.

---

## 3. Protection

**Connection: Targeted defenses.** Protection absorbs stress before it hits
Resistance, and the Protection system has specific entries for psychic/forbidden
threats:

| Protection Source | Protects Against | Notes |
|--------|--------|-------|
| Wards, purity seals, hexagrammic chains | Corruption | The standard psychic defense. D6-D8 gear. |
| Hexagrammic Focus gear | Psychic backlash | Corruption Protection 1 → absorbs Warp stress |
| Warded tag on powers | Stress itself | Warded powers are safer when prepared |
| Mind conditioning | Mind | Absorbs Mind stress from psychic intrusion |
| Null field (Blank character) | Corruption 3 | The strongest anti-warp defense in the system |
| Sanctified/warp resistant gear | Corruption | Various items |

**Key interaction:** Enemies can also have Protection. Daemons have Corruption
Protection (absorbing Corruption stress before it hits them), daemonhosts have
multi-Resistance Protection (Corruption + Body + Mind). This creates the two-phase
combat pattern: break Protection first, then damage the entity.

**Gap identified:** There is no Protection that absorbs Authority stress from
forbidden methods. The only Authority Protection is "patron writs" — but those
are a tool that CAUSES Authority stress when misused, not a defense against it.
This means forbidden method users always eat Authority stress raw. This may be
intentional (the Imperium doesn't protect you from its own judgment) but it's
worth noting as a potential design tension.

---

## 4. Heat / Subtlety / Cover

**Connection: Exposure amplifier.** Psychic powers and forbidden methods are
among the most Heat-generating actions in the game.

### Heat Triggers

From the Heat and Subtlety doc:
- "Reveals psychic phenomena" — explicit Heat trigger (Section 1, line 40)
- "The mission involves psykers, daemons, xenos artifacts" — +1 starting Heat (Section 3)

From the psychic powers doc:
- Visible powers: +1 Heat if public
- Forbidden methods with exposure risk: +1/+2 Heat on failure
- Warp Trace clock at 6/6: daemons can track the cell (functional Heat — the
  enemy always knows where you are)

### Cover Interactions

- **Visible/Area powers:** Cover is "Questioned" — witnesses saw something
  that doesn't fit the cover story
- **Psychic Tell burden:** D3 Shadow stress when a power is visible or repeated
- **Forbidden methods with Compromising tag:** Evidence of use can be turned
  against the cell, damaging Cover

### Conditional Ambush

At Heat 6+ (Hunted) or Heat 9+ (Burned), the Conditional Ambush system kicks in.
Psychic use accelerates Heat, which accelerates ambush risk. This creates a
feedback loop: the more the cell uses psychic powers for an advantage, the more
likely the enemy strikes.

**Design implication:** The Heat system is the primary balancing mechanism for
psychic powers. A psyker who uses powers freely will burn the Operation. A psyker
who uses powers sparingly preserves the cell's covert position. This is the
correct design — the cost of power IS the story.

---

## 5. Patron System

**Connection: Institutional judgment and resource pipeline.** The Patron is the
single most important external pressure on psychic/forbidden use.

### Patron Notice Triggers

From the psychic powers doc and Patron system:
- Psychic powers used publicly: Patron Notice (was the cell meant to be covert?)
- Forbidden Methods with "Radical" tag: accumulate Patron Notice on repeated use
- Red Line pressure: the Patron has hard constraints on forbidden use
- Warp Trace clock at 6/6: Patron Notice +1
- Failure on forbidden methods: Patron Notice +2

### Patron as Resource

- **Sanctioned Psyker Warrant** (Boons): D6 Resource — permission to use
  sanctioned psykers
- **Exorcism Protocols** (Boons): D8 Resource — permission to use exorcism
- **Forbidden Asset** advancement: Assets the Patron has vouched for
- **Sanctioned Monster** major advance: D10 forbidden Resource — but the Patron
  owns proof of what you are

### Patron Red Lines

The most direct interaction. A Patron may forbid:
- Using unsanctioned witchcraft (catches most psykers)
- Bargaining with daemonological entities
- Preserving forbidden assets
- Allowing full daemon manifestation

Crossing a Red Line is the nuclear option — the Patron will act against the cell.

**Design implication:** The Patron is both the enabler and the jailer. The cell
needs the Patron's resources (Boons, warrants, permission) but every use of those
resources is monitored. This creates the central tension of the Inquisition game:
you have terrible power, and terrible oversight.

---

## 6. Advancement

**Connection: Character growth through forbidden action.** The advancement system
actively rewards using forbidden methods and psychic powers.

### Radical Beats (Advancement Triggers)

From the advancement doc:
- "Use a psychic power in a way that frightens witnesses" — Radical Beat
- "Use forbidden knowledge to save the mission" — Radical Beat
- "Protect a source of corruption because it is too useful to destroy" — Radical Beat
- "Keep a forbidden artifact instead of destroying it" — Radical Beat
- "Conceal your own corruption, fear, or forbidden knowledge" — Radical Beat

### Advancement Options

| Advance | Type | Effect |
|---------|------|--------|
| **Forbidden Asset** | Minor | Gain D8 forbidden Resource (xenos device, daemonological index, unsanctioned psyker, heretek tool) |
| **Licensed Witch** | Core (class) | Begin with 2 Psychic Powers. Clear D3 stress on 10. Backlash on 1. |
| **Sanctioned Monster** | Major | Gain D10 forbidden Resource or power. Patron owns proof of what you are. |
| **Radicalization** | Major | Gain forbidden power. Gain Patron suspicion. |
| **Feedback Loop** | Class | On failed psychic power, take +D3 Mind to learn what interfered |
| **Psychic Bulwark** | Class | Take Mind/Corruption stress for allies, reduce by 1 die step |
| **Channel the Storm** | Class | Absorb warp phenomenon into self. D10 Corruption/Mind stress. |
| **Open the Eye** | Class | Once/Mission: ask one true question about warp influence. D8 Corruption/Mind. |
| **Null Field** | Class (Blank) | Psychic powers become Dangerous near you. Social comfort becomes Risky. |
| **No Soul to Take** | Class (Blank) | Once/Mission: ignore Severe/Critical Corruption effect. Heat/Authority fallout. |
| **Soulless Collapse** | Class (Blank) | Once/Mission: end all psychic effects in range. D8 Body to self, D8/D6 Mind to others. |

**Design implication:** The advancement system creates a ratchet. Every time you
use a forbidden method and survive, you advance toward being more forbidden. The
Radical axis on the advancement track is the mechanical expression of the Corruption
spiral. Characters who rely on these tools become more powerful and more condemned
simultaneously.

---

## 7. Enemy Design

**Connection: Asymmetric threat system.** Psychic and forbidden enemies require
psychic/forbidden tools to defeat efficiently.

### Enemy Archetypes

From the enemy design section and the Mission doc:

| Enemy Type | Protection | Weakness | Required Tool |
|------------|-----------|----------|---------------|
| Possessed human | Corruption Protection | Wards bypass Protection | Hexagrammic Rebuke |
| Daemon (incorporeal) | Body Protection (semi-immaterial) | Psychic powers ignore Body Prot. | Psychic attack |
| Daemonhost (bound) | Multi-Resistance (Corruption+Body+Mind) | Break wards first, then damage | Ward-breaking + physical |
| Warp phantom | None | Psychic vulnerability (+1 die step) | Any psychic power |
| Psyker (enemy) | Mind, Corruption | Null field, physical violence | Blank character or guns |
| Blank/Pariah (enemy) | Corruption 3 | Vulnerable to physical, not psychic | Melee weapons |

**Key design principle:** enemies with warp-Constitution resist the obvious approach.
A daemon with Corruption Protection 3 shrugs off Corruption stress from most attacks.
But wards bypass that Protection. A daemonhost's multi-Resistance armor requires
the cell to break through layers. This creates the "two-phase combat" pattern:
disable defenses, then deal damage.

**Enemy stress dice:** Enemies don't roll. Their stress die defines how much
damage they inflict on failed player rolls. A daemonhost with D10 stress die
(Brutal) is the most dangerous thing in the game — it can one-shot a character
on a CRIT_FAIL.

---

## 8. Requisition & Gear

**Connection: Equipment pipeline and permission system.**

### Forbidden Requisitions

From the requisition doc and quick reference:
- "Forbidden assets" are a valid Requisition type (d8 Resource die)
- The cell can requisition: xenos devices, daemonological indices, unsanctioned
  psykers, heretek tools — but these come with Burden Profiles
- Each use of a forbidden Requisition steps the die down (D10→D8→D6→D3→gone)
- Burdens include: "Patron Marked", "Witness-Magnet", "Paper Trail",
  "Sacred Obligation", "Machine-Spirit Temper"

### Psychic Gear

From the classes doc:
- **Psy-Focus** (D8 Resource): Grants permission and Mastery for controlled
  psychic work. Absorbs one Warp Trace complication per Mission. Step-down on use.
- **Hexagrammic Charms** (D8): Corruption Protection 1 against Warp Trace,
  possession, psychic intrusion. Refreshed by reconsecration.
- **Blessed Blade** (D6): Against daemonic/warp-touched, inflicts Corruption
  stress instead of Body stress.
- **Grimoire of Bound Names**: Daemonological text. D8 Resource. Steps down
  on use. Highly illegal.

**Design implication:** The Requisition system is how the cell gets access to
psychic/forbidden tools within the fiction. The Patron's permission (via Boons
and writs) determines what's available. The Burden system ensures that every
powerful item has a narrative cost beyond its mechanical one.

---

## 9. Mission Structure

**Connection: Pacing and escalation container.** Psychic/forbidden content
naturally escalates through the Campaign → Mission → Operation → Situation
hierarchy.

### Starting Heat Modifiers

From the Heat and Subtlety doc:
- +1 starting Heat if the mission involves psykers, daemons, xenos artifacts
- This means psychic/forbidden content starts the Operation hotter,
  accelerating the pressure curve

### Encounter Design

From the Saint with the Wrong Shadow mission:
- **Quiet route:** Use Subtle powers (Witch-Sight, Veil), forbidden methods
  that don't create witnesses. Low Heat accumulation.
- **Loud route:** Visible powers, public authority, violence. High Heat.
- **Disaster route:** Possession clock fills, Warp Trace clock fills, daemon
  fully manifests. Maximum pressure.

### Clock Integration

Psychic/forbidden mechanics use almost every clock type in the game:
- **Warp Trace clock** (6-segment): Accumulated psychic residue → tracking/rift
- **Possession clock** (4-segment): Character being taken over → full possession
- **Betrayal clock** (varies): Double-agent forbidden assets → cover exposure
- **Ritual/daemonic clock** (varies): Enemy progress toward manifestation
- **Public Panic clock** (6-segment): Witness reaction to miracles/witchcraft
- **Audit clock** (varies): Authority investigation into forbidden activity
- **Debt clock** (varies): Payment owed to forbidden entities

**Design implication:** Clocks are the temporal pressure system. Psychic and
forbidden actions create clocks that advance even when the players aren't acting.
The Warp Trace clock ticks every time a power is used. The Possession clock ticks
every time the entity feeds. This creates urgency: the longer the cell takes, the
more dangerous the forbidden situation becomes.

---

## 10. Quick Reference Sheet

**Connection: Table-facing summary.** The Quick Reference Sheet has a condensed
section (line 233) that reads:

> "On 7 or lower, psychic powers usually add Corruption stress unless the power
> says otherwise. A Forbidden Method may simply work and charge a cost when
> uncertainty is not interesting."

This is the one-line summary of the entire psychic/forbidden subsystem: always
costly, sometimes optional to roll.

---

## Interaction Map — Summary

```
                    ┌─────────────────────────────────────────┐
                    │           CORE ROLL SYSTEM              │
                    │   Pool + Difficulty → Result Table      │
                    └──────────┬──────────────┬───────────────┘
                               │              │
              ┌────────────────┼──────────────┼────────────────┐
              │                │              │                │
    ┌─────────▼──────┐ ┌──────▼──────┐ ┌─────▼──────┐ ┌──────▼───────┐
    │   RESISTANCES  │ │  PROTECTION │ │   HEAT &   │ │   PATRON     │
    │ Body/Mind/     │ │ Wards absorb│ │   COVER    │ │ Notice,      │
    │ Shadow/Auth/   │ │ Corruption  │ │ Psychic =  │ │ Permission,  │
    │ Corruption     │ │ stress      │ │ +1 Heat    │ │ Red Lines    │
    │                │ │             │ │ Public =   │ │              │
    │ Corruption is  │ │ Daemons     │ │ Cover      │ │ Boons enable │
    │ the special    │ │ have Pro-   │ │ Questioned │ │ forbidden    │
    │ Resistance     │ │ tection too │ │            │ │ tools        │
    └───────┬────────┘ └──────┬──────┘ └─────┬──────┘ └──────┬───────┘
            │                 │              │               │
            │    ┌────────────┼──────────────┼───────────────┤
            │    │            │              │               │
    ┌─────▼────▼────┐ ┌──────▼──────┐ ┌─────▼──────┐ ┌──────▼───────┐
    │   ADVANCEMENT │ │   ENEMY     │ │REQUISITION │ │   MISSION    │
    │ Radical Beats │ │ DESIGN     │ │ & GEAR     │ │   STRUCTURE  │
    │ reward for-   │ │ Daemons    │ │ Forbidden  │ │ Starting     │
    │ bidden use    │ │ need wards │ │ assets are │ │ Heat +1 for  │
    │               │ │ to defeat  │ │ Requisitions│ │ psychic/     │
    │ Ratchet: more │ │            │ │            │ │ forbidden    │
    │ forbidden →   │ │ Enemies    │ │ Gear steps │ │              │
    │ more powerful │ │ never roll │ │ down on    │ │ Clocks track │
    │ AND condemned │ │            │ │ use        │ │ escalating   │
    └───────────────┘ └────────────┘ └────────────┘ │ threats      │
                                                     └──────────────┘
```

---

## Key Design Findings

1. **Corruption is the keystone Resistance.** Everything psychic/forbidden flows
   through Corruption: powers stress it, the Warp Track clock measures it,
   the Possession clock tracks its culmination, and the Fallout table defines
   its consequences. Characters with low Corruption Resistance are living on
   borrowed time.

2. **The system is intentionally asymmetric.** Psykers stress Corruption first.
   Radicals stress Authority first. This means they degrade along different
   axes and create different end-game conditions. A psyker falls to possession.
   A radical falls to institutional judgment. Both are tragic, but differently.

3. **Heat is the primary balancing mechanism.** Every forbidden action risks
   Heat. Heat triggers ambushes, Patron Notice, and conditional enemy action.
   The psychic/forbidden subsystem is not balanced by making powers weak — it's
   balanced by making them visible.

4. **Advancement creates the ratchet.** The more you use forbidden tools, the
   more powerful AND more condemned you become. Radical Beats actively reward
   the behavior the Patron may punish. This tension IS the Inquisition game.

5. **The Patron is the load-bearing wall.** Remove the Patron system and psychic/
   forbidden methods lose their institutional context — they're just "magic with
   a cost." The Patron's permission, oversight, Red Lines, and secrets create
   the political dimension that makes the cost meaningful.

6. **Clocks are the temporal pressure.** Warp Trace and Possession clocks create
   escalating situations that can't be solved by rolling better. They force
   narrative action: the cell must deal with the daemon NOW, not after they've
   prepared more.

7. **Protection is the puzzle key.** Daemons with Corruption Protection, daemonhosts
   with multi-Resistance armor — enemies are designed to resist the obvious
   approach. The cell must figure out the right tool for the right threat:
   wards for daemons, null fields for psykers, violence for the physical.

---

## Gaps and Recommendations

1. **Authority Protection gap (partial).** The core rules list "Patron writs" as
   Authority Protection, which covers the case of acting under explicit Patron
   authorization. However, there is no general Authority Protection for characters
   using forbidden methods *without* explicit Patron backing. The existing "Patron
   writs" entry is narrow — it absorbs institutional stress from *authorized* use,
   not from rogue radicalism. Consider: no additional mechanical fix needed, but
   GMs should be aware that forbidden method users always eat Authority stress from
   unauthorized use. This is intentional — the Imperium doesn't protect you from
   its own judgment when you act without authorization. The design is correct; the
   gap is more of a clarifying note than a missing rule.

2. **Warp Trace clock cross-reference.** The Warp Trace clock definition now lives
   in the psychic powers doc but should also be referenced in the GM Toolkit's
   clock section (around line 93) and the Operation Sheet. Add it as a named
   clock option.

3. **Possession clock cross-reference.** Same as above — the Possession clock
   should appear in the GM Toolkit's "clocks as pressure tools" section.

4. **Mind-Scrape scenario gap.** The mission doc doesn't include a situation where
   memory-ripping is the obvious solution. Consider adding a "locked witness" NPC
   — someone who knows the answer but will never speak. This makes the choice to
   use a Forbidden power concrete.

5. **Psychic power interaction with Cover.** The rules mention "Cover Questioned"
   for visible powers but don't specify the mechanical result. Consider: using
   a Visible power in a Cover identity's area steps down the Cover die by one
   (in addition to any Heat cost). This creates resource tension: the power works
   but your cover is damaged.

6. **Pyker vs. Blank interaction undefined.** A Blank nullifies psychic powers
   nearby. But what happens when a Blank and a psyker cooperate? The Blank's
   Absence ability makes powers Risky/Dangerous. The psyker's Mastery adds a
   die. These interact but the rules don't specify how. Recommendation: Blank's
   null field increases Difficulty by one step; psyker's Mastery adds +1D10.
   The net effect depends on pool size and base Difficulty.
