# Analysis: Should the 6 Gap Fixes Be Folded Into Classes?

## Short Answer

**Some should, some shouldn't.** The right approach is:

| Gap | Currently In | Better Home | Why |
|-----|-------------|-------------|-----|
| Visible + Cover rule | Psychic Powers doc (general) | **Sanctioned Psyker class** as a minor advance | It's a specific technique a trained psyker learns |
| Psyker + Blank interaction | Psychic Powers doc (general) | **Blank class** (expand Absence) + **Sanctioned Psyker** (new minor advance) | It's a class-to-class interaction, not a general rule |
| Warp Trace clock | Both psychic docs + GM Toolkit | **Keep distributed** | It's a shared clock — belongs in GM Toolkit and referenced from psychic doc |
| Possession clock | Both psychic docs + GM Toolkit | **Keep distributed** | Same as above |
| Mind-Scrape scenario | Mission doc | **Keep in mission** | It's content, not a rule |
| Authority Protection | Analysis doc | **No change needed** | Confirmed as intentional design |

## Detailed Reasoning

### Visible + Cover → Sanctioned Psyker Class

The rule says: "When a Visible power is used where Cover is active, step down Cover by one die size."

This is exactly the kind of thing a **trained, sanctioned psyker** would learn as part of their operational discipline. The Unsanctioned Psyker doesn't care about Cover. The Sanctioned Psyker is trained to minimize exposure.

**Move to:** Sanctioned Psyker class, as a new Minor Advance:

> **Disciplined Casting:** When you use a Visible or Area psychic power in a location where you have an active Cover identity, you may choose to step down your Cover die by one size (D10→D8→D6→D3) to avoid the Heat and witness consequences of the visible power. The power still works, but your Cover story now has a gap that doesn't quite fit. You may use this ability once per Situation.

This reframes the rule from a *penalty* ("your cover is damaged") to a *choice* ("you can sacrifice cover to avoid heat"). This is much better design — it creates a meaningful resource tension that the player controls.

**Remove from:** The general psychic powers doc. The general rule about Visible powers causing Heat and questioning Cover stays, but the mechanical step-down becomes a class ability.

### Psyker + Blank Interaction → Both Classes

The 49-line interaction rule is really two things:

**Part A — What the Blank does to the Blank:** The Absence field's effect on psychic powers is already in the Blank's Core Ability. But it only says "powers become Risky/Dangerous" — it doesn't explain edge cases (Mastery, Protection, targeting the Blank directly, Cut the Thread, Soulless Collapse).

**Expand Blank's Absence ability** to include:
- Mastery still applies (the psyker's skill isn't nullified)
- Corruption Protection absorbs Corruption stress from powers targeting the Blank
- Cut the Thread and Null Anchor suppress power effects but don't prevent stress
- Soulless Collapse ends all powers in range, stress still triggered

**Part B — What the psyker experiences:** The disruption, the Corruption stress from the null field interfering with power flow, the tactical choice of whether to use powers near the Blank at all.

**Add a new Minor Advance to Sanctioned Psyker:**

> **Null Adaptation:** You have learned to operate near Blanks and null fields. When a Blank ally is present, your psychic powers are stepped up by only one Difficulty level (instead of two or more). On a 7 or lower, take +D10 Corruption stress from the field disruption. You can still use powers near Blanks — it just costs more.

**Remove from:** The general psychic powers doc. The general note "Blank's Absence increases Difficulty" stays as a single sentence referencing the two classes for details.

### Warp Trace Clock → Keep as-is

The Warp Trace clock is a **shared resource** — it's not owned by any class. It's a consequence of using psychic powers, like Heat. It belongs in the GM Toolkit (where GMs look up what clocks do) with a reference in the psychic powers doc (where the mechanic is introduced). The fill effects should stay in both places.

**No change needed.** This is correctly distributed.

### Possession Clock → Keep as-is

Same reasoning as Warp Trace. The Possession clock is a consequence engine, not a class feature. The Exorcist class interacts with it (Seal the Vessel, Binding Chains) but doesn't own it.

**Add a reference in the Exorcist class** to the Possession clock:

> **Clock Interaction:** When you use Seal the Vessel or Binding Chains on a character with an active Possession clock, reduce the clock by 1 segment on success, 2 on a 10. See Psychic Powers and Forbidden Methods v0.1 for full Possession clock rules.

**Keep the full definition** in the psychic powers doc and the GM Toolkit.

### Mind-Scrape Scenario → Keep in Mission

This is content design, not rules design. The Marked Pilgrim is an NPC in a specific mission. It doesn't belong in a class.

**Already in the right place.** No change.

### Authority Protection → No Change

Confirmed as intentional. Patron writs protect authorized use. Unauthorized use has no shield. This is correct Inquisition design.

**No change needed.**

## Summary of Changes

### Remove from Psychic Powers and Forbidden Methods doc
- "Visible Powers and Cover" section (21 lines) — moved to Sanctioned Psyker class
- "Psyker and Blank Interaction" section (43 lines) — split between Blank class and Sanctioned Psyker class

### Add to Sanctioned Psyker class (04-complete-classes-v0.1.md)
- New Minor Advance: **Disciplined Casting** — trade Cover step-down to avoid Heat/witnesses from Visible powers
- New Minor Advance: **Null Adaptation** — reduced Difficulty step-up when operating near Blanks

### Expand Blank class (04-complete-classes-v0.1.md)
- Expand **Absence** core ability with edge case rules (Mastery, Protection, Cut the Thread, Soulless Collapse interaction)

### Add to Exorcist class (04-complete-classes-v0.1.md)
- Add clock interaction note referencing Possession clock

### Keep as-is
- Warp Trace clock (psychic docs + GM Toolkit)
- Possession clock (psychic docs + GM Toolkit)
- Mind-Scrape scenario (mission doc)
- Authority Protection (confirmed intentional)
