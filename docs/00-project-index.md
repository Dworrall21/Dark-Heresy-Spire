# Dark Heresy Spire Project Index

**Dark Heresy Spire** is a Spire / Resistance Toolbox style hack for **Imperium Maledictum - Inquisition** play.

The project is currently in a **v0.1 playtest chassis** state. The core loop, character creation, advancement, classes, Patron pressure, Heat/Subtlety, GM support, requisition/gear, and table sheets are present enough to support a first playtest.

---

## Core Design Pillars

1. **Competent acolytes, costly action** — roll to see what competence costs.
2. **Investigation before combat** — combat is a Situation, not a separate tactical minigame.
3. **Authority is weapon and liability** — writs, seals, Rosettes, and Patron authority solve problems while creating Heat, witnesses, paperwork, and rivals.
4. **Subtlety matters** — Heat, Shadow stress, Cover, and Enemy Awareness track exposure.
5. **Forbidden solutions work** — xenos tools, heretek methods, daemonology, torture, purges, and blackmail are tempting because they are effective.
6. **The Patron is not your friend** — the Patron is authority, resource source, ideology, pressure, mystery, and judgment.
7. **Fallout drives story forward** — consequences should expose truths, burn assets, create enemies, compromise covers, and force choices.

---

## Current Document Map

### System Core

| # | Document | Purpose | Status |
|---:|---|---|---|
| 01 | [Core Rules Skeleton v0.2](01-core-rules-skeleton-v0.2.md) | Core roll, difficulty, stress, fallout, resistances, psychic/forbidden examples | Current |
| 02 | [Character Creation v0.1](02-character-creation-v0.1.md) | Origins, former allegiances, class selection, cover, bonds, starting gear | Current |
| 03 | [Advancement v0.1](03-advancement-v0.1.md) | Duty, Humanity, and Radical Beats; minor/major/severe advances | Current |
| 04 | [Complete Classes v0.1](04-complete-classes-v0.1.md) | Playtest-ready classes, packages, refreshes, and advances | Current |
| 05 | [Patron System v0.1](05-patron-system-v0.1.md) | Ordo, Philosophy, Boons, Liabilities, Patience, Red Lines, Patron Notice | Current |
| 06 | [Heat and Subtlety v0.1](06-heat-subtlety-v0.1.md) | Heat, Shadow, Cover, Enemy Awareness, witnesses, evidence, Rosette use | Canonical |
| 07 | [Mission and Operation Template v0.1](07-mission-operation-template-v0.1.md) | Campaign, Mission, Operation, Situation, clue, opposition, and clock templates | Current |
| 08 | [GM Toolkit v0.1](08-gm-toolkit-v0.1.md) | GM agenda, moves, threats, factions, clue design, clocks, NPCs, procedures | Current |
| 09 | [Requisition and Gear v0.1](09-requisition-and-gear-v0.1.md) | Modular equipment, tags, burdens, requisition procedure, random gear/name tables | Current |

### Legacy / Superseded

| Document | Note |
|---|---|
| [Heat and Subtlety v0.1 Outline](06-heat-subtlety-v0.1-outline.md) | Superseded by the canonical `06-heat-subtlety-v0.1.md`. Keep only for comparison until cleanup/deletion. |

### Table Sheets

| # | Sheet | Purpose | Status |
|---:|---|---|---|
| 00 | [Sheets Index](sheets/00-sheets-index.md) | Overview of table-facing sheet files | Current |
| 01 | [Acolyte Character Sheet](sheets/01-acolyte-character-sheet-v0.1.md) | Player character sheet | Current |
| 02 | [Cell Sheet](sheets/02-cell-sheet-v0.1.md) | Shared cell resources, cover, bonds, contacts, and notes | Current |
| 03 | [Patron Sheet](sheets/03-patron-sheet-v0.1.md) | Patron profile, Boons, Liabilities, Patience, Red Lines | Current |
| 04 | [Operation Sheet](sheets/04-operation-sheet-v0.1.md) | Operation Heat, Awareness, clocks, clues, opposition, and fallout prompts | Current |
| 05 | [Quick Reference Sheet](sheets/05-quick-reference-sheet-v0.1.md) | Table-facing rules summary; gear/requisition summary is next cleanup item | Current |

---

## Current Playtest Chassis

The game currently supports:

- Core D10 pool rolls.
- Lex Ecclesiastica-style Risky/Dangerous difficulty, where the top die or dice are removed after rolling.
- Five Resistances: Body, Mind, Shadow, Authority, Corruption.
- Minor, Moderate, Severe, and Critical Fallout.
- Beat-driven advancement.
- Complete playtest class packages.
- Patron creation and Patron pressure.
- Heat/Subtlety and Enemy Awareness at the Operation level.
- Mission/Operation/Situation prep.
- GM-facing threat, clue, faction, clock, and NPC tools.
- Modular requisition and gear.
- Random equipment and equipment name generation.
- Player and table sheets.

This is enough to run a one-shot or short playtest mission.

---

## Immediate Next Steps

### 1. Quick Reference Gear Integration

Update:

```text
docs/sheets/05-quick-reference-sheet-v0.1.md
```

Add compact references for:

- Equipment structure.
- Gear functions.
- Resource dice.
- Common tags.
- Burden triggers.
- Requisition procedure.
- Weapon stress scale.
- Protection scale.

### 2. Psychic Powers and Forbidden Methods v0.1

Create a standalone reference that expands the core examples into complete table-facing systems.

Proposed file:

```text
10-psychic-powers-and-forbidden-methods-v0.1.md
```

Proposed contents:

1. Psychic Power Principles
2. Using Psychic Powers
3. Psychic Stress and Warp Trace
4. Psychic Power Tags
5. Psychic Power Chassis
6. Psychic Power Modules
7. Example Psychic Powers
8. Perils / Psychic Burdens
9. Forbidden Method Principles
10. Forbidden Method Tags
11. Forbidden Method Chassis
12. Example Forbidden Methods
13. Radical Use, Patron Notice, and Red Lines
14. Random Psychic / Forbidden Method Generator
15. One-Page Reference

### 3. First Playtest Mission

Create a short mission designed to test the core loop.

Working title:

```text
The Saint with the Wrong Shadow
```

It should test investigation, Heat/Subtlety, Requisition, Patron pressure, a forbidden shortcut, at least one psychic or occult threat, one quiet route, one loud route, and one disastrous route.

### 4. Cleanup / Repo Hygiene

- Delete or archive the superseded `06-heat-subtlety-v0.1-outline.md` after confirming nothing references it.
- Add links from relevant docs to the Quick Reference and Sheets Index.
- Consider a `README.md` that points to this index and explains the playtest order.

---

## Recommended Reading / Running Order

For a GM running a first test:

1. Read [Core Rules Skeleton v0.2](01-core-rules-skeleton-v0.2.md).
2. Read [Character Creation v0.1](02-character-creation-v0.1.md).
3. Read [Complete Classes v0.1](04-complete-classes-v0.1.md).
4. Build a Patron using [Patron System v0.1](05-patron-system-v0.1.md).
5. Prep the mission using [Mission and Operation Template v0.1](07-mission-operation-template-v0.1.md).
6. Run pressure using [Heat and Subtlety v0.1](06-heat-subtlety-v0.1.md).
7. Use [GM Toolkit v0.1](08-gm-toolkit-v0.1.md) during prep and play.
8. Use [Requisition and Gear v0.1](09-requisition-and-gear-v0.1.md) for equipment, assets, and rewards.
9. Keep [Quick Reference Sheet](sheets/05-quick-reference-sheet-v0.1.md) open at the table.

---

## Design Status

| Area | Status | Notes |
|---|---|---|
| Core roll | Playtest-ready | Needs table testing for dice pool size and difficulty feel. |
| Stress/Fallout | Playtest-ready | Fallout examples may need expansion after testing. |
| Character creation | Playtest-ready | Starting gear should now reference modular equipment. |
| Classes | Playtest-ready | Needs balance review after first mission. |
| Advancement | Playtest-ready | Beat rewards need table pacing test. |
| Patron system | Playtest-ready | Strong; should be tested with Heat and Requisition. |
| Heat/Subtlety | Playtest-ready | Canonical file exists; old outline should be removed later. |
| GM Toolkit | Playtest-ready | Strong enough for first GM pass. |
| Requisition/Gear | Playtest-ready draft | Needs quick reference integration and class starting package pass. |
| Psychic/Forbidden methods | Needed next | Currently exists only as core examples and Heat interactions. |
| Playtest mission | Needed soon | Required for practical validation. |
| Site/sheet pages | Future | Markdown sheets are ready to become standalone pages later. |
