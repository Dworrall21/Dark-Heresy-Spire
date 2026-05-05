# Dark Heresy Spire Project Index

**Dark Heresy Spire** is a Spire / Resistance Toolbox style hack for **Imperium Maledictum - Inquisition** play.

The project is currently in a **v0.1 playtest chassis** state. The core loop, character creation, advancement, classes, Patron pressure, Heat/Subtlety, GM support, requisition/gear, psychic and forbidden methods, a first playtest mission, and table sheets are present enough to support a first playtest.

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
| 10 | [Psychic Powers and Forbidden Methods v0.1](10-psychic-powers-and-forbidden-methods-v0.1.md) | Psychic powers, Warp trace, forbidden methods, radical costs, generators | Current |
| 11 | [The Saint with the Wrong Shadow v0.1](11-the-saint-with-the-wrong-shadow-v0.1.md) | First playtest mission testing investigation, Heat, Requisition, Patron pressure, psychic threats, and forbidden shortcuts | Current |

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
| 05 | [Quick Reference Sheet](sheets/05-quick-reference-sheet-v0.1.md) | Table-facing rules summary, including compact gear/requisition reference | Current |

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
- Psychic powers, Warp Trace, and Psychic Burdens.
- Forbidden methods, Radical pressure, Red Lines, and Patron Notice triggers.
- A first playtest mission: **The Saint with the Wrong Shadow**.
- Player and table sheets.

This is enough to run a one-shot or short playtest mission.

---

## Immediate Next Steps

### 1. Class Starting Package Gear Pass

Update class starting gear to reference the modular equipment structure from Requisition and Gear v0.1.

Focus on:

- Chassis.
- Tags.
- Resource dice.
- Burdens for restricted, forbidden, Patron-marked, or suspicious gear.
- Keeping class gear flavorful without turning it into a shopping list.

Proposed file to update:

```text
04-complete-classes-v0.1.md
```

### 2. README / Entry Point

Create or update a top-level `README.md` that points readers to this index and gives a recommended playtest reading order.

### 3. Repo Hygiene

- Delete or archive the superseded `06-heat-subtlety-v0.1-outline.md` after confirming nothing references it.
- Add cross-links from relevant docs to the Quick Reference and Sheets Index.
- Later, convert Markdown sheets into standalone site pages.

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
9. Use [Psychic Powers and Forbidden Methods v0.1](10-psychic-powers-and-forbidden-methods-v0.1.md) for psykers, Warp Trace, radical shortcuts, and forbidden assets.
10. Run or adapt [The Saint with the Wrong Shadow v0.1](11-the-saint-with-the-wrong-shadow-v0.1.md) as the first playtest mission.
11. Keep [Quick Reference Sheet](sheets/05-quick-reference-sheet-v0.1.md) open at the table.

---

## Design Status

| Area | Status | Notes |
|---|---|---|
| Core roll | Playtest-ready | Needs table testing for dice pool size and difficulty feel. |
| Stress/Fallout | Playtest-ready | Fallout examples may need expansion after testing. |
| Character creation | Playtest-ready | Starting gear should now reference modular equipment. |
| Classes | Playtest-ready | Needs balance review and modular gear pass after first mission. |
| Advancement | Playtest-ready | Beat rewards need table pacing test. |
| Patron system | Playtest-ready | Strong; should be tested with Heat and Requisition. |
| Heat/Subtlety | Playtest-ready | Canonical file exists; old outline should be removed later. |
| GM Toolkit | Playtest-ready | Strong enough for first GM pass. |
| Requisition/Gear | Playtest-ready draft | Needs class starting package integration. |
| Psychic/Forbidden methods | Playtest-ready draft | Needs table testing for cost severity, Warp Trace, and forbidden shortcut frequency. |
| Quick Reference | Current | Includes compact gear/requisition reference. |
| Playtest mission | Current | First test mission exists as `11-the-saint-with-the-wrong-shadow-v0.1.md`. |
| README / entry point | Needed | Should point readers to this index and the playtest running order. |
| Site/sheet pages | Future | Markdown sheets are ready to become standalone pages later. |
