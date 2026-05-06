# System Progress Tracker v0.1

This document tracks the current state of the **Dark Heresy Spire** playtest chassis, design commitments, and near-term cleanup work.

Use [Dark Heresy Spire Project Index](00-project-index.md) for navigation and reading order. Use this tracker for project status.

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

## Design Commitments

| Question | Current Answer |
|---|---|
| Use D10 pools? | Yes |
| Keep Skills + Domains? | Yes |
| Use Lex-style Difficulty? | Yes: remove highest die after rolling |
| Keep stress and fallout? | Yes |
| Use per-Resistance Fallout? | Yes |
| Keep money/Silver? | No |
| Add Authority Resistance? | Yes |
| Add Corruption Resistance? | Yes |
| Track shared Heat? | Yes |
| Make combat separate? | No |
| Make investigation clue-forward? | Yes |
| Use Patrons/Requisition? | Yes, simplified |
| Use classes instead of careers? | Yes, Spire-style classes inspired by Inquisition roles |
| Make forbidden tools strong? | Yes |
| Balance forbidden tools with cost? | Yes |

---

## Immediate Next Steps

### 1. Class Starting Package Gear Pass

Update class starting gear to reference the modular equipment structure from [Requisition and Gear v0.1](09-requisition-and-gear-v0.1.md).

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

Create or update a top-level `README.md` that points readers to the project index and gives a recommended playtest reading order.

### 3. Repo Hygiene

- Decide whether to rename `06-heat-subtlety-v0.1-outline.md` or keep it as the canonical Heat/Subtlety file for v0.1.
- Add cross-links from relevant docs to the Quick Reference and Sheets Index.
- Later, convert Markdown sheets into standalone site pages.

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
| Heat/Subtlety | Playtest-ready | Current file is `06-heat-subtlety-v0.1-outline.md`; decide later whether to rename. |
| GM Toolkit | Playtest-ready | Strong enough for first GM pass. |
| Requisition/Gear | Playtest-ready draft | Needs class starting package integration. |
| Psychic/Forbidden methods | Playtest-ready draft | Needs table testing for cost severity, Warp Trace, and forbidden shortcut frequency. |
| Quick Reference | Current | Includes compact gear/requisition reference. |
| Playtest mission | Current | First test mission exists as `11-the-saint-with-the-wrong-shadow-v0.1.md`. |
| README / entry point | Needed | Should point readers to the project index and the playtest running order. |
| Site/sheet pages | Future | Markdown sheets are ready to become standalone pages later. |
