# Playtest 9 — Post-Playtest Analysis

**Seed:** 42  
**Date:** 2026-05-08  
**Mission:** The Saint with the Wrong Shadow  
**Cell:** 4 PCs (Kael Mourn, Seren Vale, Lys Thane, Pyra Voss)  
**Patron:** Inquisitor Vael Draven (Ordo Hereticus, Puritan/Containment)

---

## Mission Narrative Summary

The cell entered Hive Olymra's Chapel of Saint Septima's Ashes under Administratum audit cover, investigating the "miracle" of Sella Vorn — a dead hab-worker whose corpse refused to decay and whose shadow moved independently.

**Operation 1 (Enter the Shrine):** The cell established cover and observed the miracle. Kael found black glass residue in Sella's wound and confirmed the shadow bends toward prayer, not light. Lys got Frater Loam's cooperation but triggered an Ecclesiarchy complaint. Seren mapped the entire plaza. Pyra's Witch-Sight failed but the shadow noticed her — Warp Trace 1/6, Wrong Shadow Awakens advanced to 2/6.

**Operation 2 (Follow the Dead Woman's Life):** Seren captured a cult lookout. Kael found black dust and a transit chit in Sella's dormitory. Lys couldn't trace the chit. Pyra's Veil of Unnotice failed — the cult hunter spotted her, Enemy Awareness rose to 2. Kael couldn't reach Mira — she fled.

**Operation 3 (Break the Choir):** Lys's cover was blown at the cult meeting — Cale recognized her. Heat rose to 3. Kael couldn't break the captured lookout. Pyra's Witch-Sight was blocked by the shadow's wards. Only Seren's tactical planning succeeded — she mapped the chapel perfectly.

**Operation 4 (Decide the Miracle):** The mass vigil. Everything went wrong. Lys was caught disrupting the rite. Seren was overwhelmed by enforcers. Kael couldn't reach Mira — the cult used her blood. The Wrong Shadow Awakens clock filled. Pyra's Hexagrammic Rebuke failed. Sella's corpse sat up and spoke: *"I am the saint you wanted."* Heat spiked to 6. Kael used the Excruciator Protocol (forbidden method) to extract the Noctilith Tear, taking Minor Mind and Corruption Fallout.

**Final State:** Heat 6 (Hunted), Enemy Awareness 2, Patron Notice 2, Warp Trace 5/6. Wrong Shadow Awakens clock FULL. The shadow spoke publicly. The relic was extracted but at terrible cost. Partial failure.

---

## What Worked Well

### 1. Core Roll Mechanic — Difficulty Removal Creates Real Tension
The Lex Ecclesiastica-style difficulty system (remove highest dice after rolling) worked exactly as intended throughout. The probability table in the GM Toolkit proved accurate in practice:
- **3D10 Risky** rolls produced a roughly even split between failure and success — tense but fair
- **2D10 Dangerous** rolls were brutal: Lys's cult infiltration (2D10 Dangerous) and Kael's Mira rescue (2D10 Dangerous) both produced automatic critical failures because all dice were removed. This is the #1 friction pattern identified in previous playtests, and it showed up again here.
- **4D10 Safe** rolls (Seren's tactical planning) produced clean successes, which felt right for a prepared character with position

The system correctly rewards preparation and punishes reckless action. Seren's CRIT_SUCCESS on Safe (10,9,2) vs Lys's CRIT_FAIL on Dangerous (empty pool) is exactly the spread the math predicts.

### 2. Protection System — Visible and Meaningful
Protection absorption was clearly visible in the log:
- Pyra's Corruption Protection 1 absorbed 1 stress on every psychic use (5 times across the mission)
- Seren's Body Protection 2 absorbed 2 stress from the enforcer fight
- Kael's Mind Protection 1 absorbed 1 stress on multiple Mind hits

This is working as designed: Protection is a buffer that makes characters survivable without making them invincible. Pyra took 10 Corruption total but would have taken 15 without her Protection 1 — that's 5 free stress absorbed, which is significant.

### 3. "Never Hide the Core Clue" — Investigation Kept Moving
When Kael failed his Investigate+Heresy roll on the blind pilgrim, the core clue (shadow bends toward prayer) was still delivered through observation. The investigation never stalled. This rule is essential and worked perfectly.

### 4. Fallout System — Creates Story, Not Dead Ends
Three characters triggered Minor Fallout:
- **Kael:** Mind Minor (hears Sella whisper his name) + Corruption Minor (shadow lags behind him)
- **Pyra:** Corruption Minor (her shadow lags behind her for one scene)

These are narrative consequences that will drive future sessions. Kael hearing Sella's voice is *exactly* the kind of haunting detail that makes the game's horror work. Pyra's shadow lagging is a visible mark that other characters can notice.

### 5. Heat System — Thresholds Create Escalation
Heat moved from 2 → 3 → 4 → 6 across the mission, with each threshold creating pressure:
- **Heat 3:** Patron Liability triggered ("someone asks why the cell is making noise")
- **Heat 6:** The Hunted threshold — the enemy is actively working against the cell

The Heat 3 move (rolled 10: Patron Liability) was particularly good — it didn't punish the players directly but added institutional pressure that will compound.

### 6. Warp Trace Clock — Psyker Tension
Warp Trace advanced from 0 → 5/6 across the mission. Every psychic use advanced it, including *failed* rolls. This creates the correct tension: using powers feeds the very thing you're trying to contain. At 5/6, the next psychic use will trigger the Warp Trace consequence (daemons can track the cell, warp rift opens, etc.). This is excellent design.

### 7. Clock System — Temporal Pressure
The Wrong Shadow Awakens clock (1→2→4→5→6) created escalating urgency. When it filled at the worst possible moment (during the mass vigil), the consequence felt earned — the cell had been warned, they tried to stop it, but the clock ran out. This is exactly how clocks should work.

### 8. End-of-Operation Checklists — Structured Consequences
The 10-question checklist at the end of each Operation ensured systematic consequence tracking. Questions 6-9 (enemy learning, faction intervention, evidence, Red Lines) were particularly useful for tracking the cascading effects of player actions.

---

## Friction Points & Rules Issues

### 1. CRITICAL: 2D10 Dangerous = Automatic Critical Failure (Recurring Issue)

**What happened:** Lys's cult infiltration roll was 2D10 Dangerous. Both dice were removed, leaving an empty pool = automatic CRIT_FAIL. Kael's Mira rescue was also 2D10 Dangerous = automatic CRIT_FAIL.

**Why it's a problem:** This is the #1 friction pattern identified in Playtest 2 and still present. When a character has only Skill+Domain (2D10) and faces Dangerous difficulty, they *cannot succeed*. Not "unlikely to succeed" — literally impossible. The highest remaining die is 0, which is treated as CRIT_FAIL.

**The math:** 2D10 Dangerous removes both dice → empty pool → result = 1 (Critical Failure). This happens 100% of the time.

**Proposed fix (from skill doc):** Scale Difficulty removal to pool size:
- Pool ≤ 3: Dangerous removes 1 die (not 2)
- Pool ≥ 4: Dangerous removes 2 dice

This would make 2D10 Dangerous leave 1 die (a coin flip) instead of 0 dice (automatic failure). The current rule makes it impossible for an unassisted character with only 2 dice to succeed at anything Dangerous, which contradicts the design principle that "competent acolytes" should be able to attempt difficult things.

**Impact on this playtest:** Lys's cult infiltration and Kael's Mira rescue were both automatic failures. These were dramatic moments, but they weren't *choices* — they were mathematical certainties. A player who knows the math will never attempt a 2D10 Dangerous roll, which removes agency.

### 2. HIGH: Psyker Corruption — Now Tied to Warp Trace

**What happened:** Pyra used psychic powers 5 times across the mission, accumulating 10 Corruption stress. Her Corruption Protection 1 absorbed 5 of that, but she still ended at 10 with Minor Fallout.

**Design response (implemented):** The between-Operation grounding amount is now tied to the **Warp Trace** clock:

| Warp Trace | Corruption Cleared | Condition |
|---|---|---|
| 0–2 | D6 | The Warp is quiet. Grounding is easier. |
| 3–4 | D3 | The trace is significant. The Warp presses back. |
| 5–6 | D3 on a Risky roll | The trace is a beacon. On a failure, clear nothing. On a 1, take D3 Corruption. |

**Why this is the right design:** The Warp Trace clock already tracks "how much occult residue the cell has left in the area." Tying recovery to it creates a direct, intuitive feedback loop:
- Use powers sparingly → low trace → easy recovery (D6)
- Use powers heavily → high trace → hard recovery (D3 with a roll, or impossible without warded space)
- The thing that makes powers dangerous (Warp Trace) also makes recovery harder

This is better than a flat D3 because it makes the psyker's choices matter across Operations, not just within them. A psyker who burns bright at Warp Trace 5 can still ground, but they need a warded space and a successful roll — the Warp is actively resisting.

**Impact on replay (Pyra's trace across Playtest 9):**
- After Op 1: Warp Trace 1 → ground D6 (would clear her 1 Corruption entirely)
- After Op 2: Warp Trace 2 → ground D6 (would clear her 1 Corruption entirely)  
- After Op 3: Warp Trace 3 → ground D3 (would clear 3 of her 5 Corruption)
- Entering Op 4: Corruption at 2 instead of 5
- After Op 4: Warp Trace 5 → must roll Risky to clear D3

Instead of ending at 10 Corruption with Minor Fallout, Pyra would have ended at ~4-7 depending on rolls — well below Fallout threshold. But if she'd rolled badly at Warp Trace 5, she might have cleared nothing and carried all of it forward. The stakes are real, and they're tied to the same clock that tracks the Warp's attention.

### 3. MEDIUM: Cover Degradation — Now Fiction-Driven with Foreshadowing

**What happened:** Lys started with D8 Cover (Chartist vessel factor) but her Cover was burned when Cale recognized her — a GM-driven narrative event rather than a player-driven mechanical spend.

**Design response (implemented):** Cover degradation is now explicitly fiction-driven with foreshadowing:
- When Cover is used, the GM names the strain ("the candle seller looks at your papers a beat too long")
- When Cover steps down, it's connected to the fiction ("your identity has been noticed")
- When Cover is at D3, the player is warned
- The GM should never burn Cover by fiat — the player chooses to spend it or keep using it despite warnings

**Why this works:** The degradation feels inevitable rather than arbitrary. Players see the cracks forming and make real choices about when to push and when to pull back. Cover is a story, not a mechanic.

**Impact on replay:** Lys's D8 Cover would have degraded gradually: D8 (first use, clerk copies her seal) → D6 (second use, clerk gives her a second look) → D3 (third use, warned it's thin) → burned (fourth use, or player chooses to stop). The player sees it coming and decides when to spend it.

### 4. MEDIUM: Enemy Awareness Didn't Escalate Enough

**What happened:** Enemy Awareness went from 1→2 over the entire mission. It never reached the thresholds for conditional ambushes (4+) or enemy strikes (7).

**Why it's a problem:** The cult was actively hunting the cell from Operation 2 onward, but Enemy Awareness stayed at 2 ("Someone is investigating"). The cult's response (sending a hunter, tightening security) was handled through fiction and Heat moves rather than through the Enemy Awareness ladder.

**This may be by design** — Enemy Awareness is supposed to be hard to raise and hard to lower. But it means the conditional ambush system (which triggers at EA 4+) was never tested. The mission would need a more aggressive enemy or more cell mistakes to push EA high enough.

**Impact on this playtest:** The conditional ambush system was not exercised. This is a gap in the playtest coverage.

### 5. LOW: Requisition System — Barely Used

**What happened:** The cell requisitioned a warded containment case (mentioned in the extraction scene) but the Requisition system wasn't formally exercised. No rolls were made for Requisitions, no burdens were tracked.

**Why it's a problem:** The Requisition system is a major subsystem (doc 09 is 38KB) but it was barely touched in this playtest. The mission includes 8 Requisition opportunities but the simulation only used one.

**Proposed fix:** Integrate Requisition rolls more tightly into the Operation structure. Each Operation should have at least one mandatory Requisition decision (spend a Boon, requisition gear, or accept a burden).

**Impact on this playtest:** The Requisition system was not stress-tested. This is a coverage gap.

### 6. LOW: Brutal Tag — Not Exercised

**What happened:** No enemy in this mission had the Brutal tag. The Brutal tag (which makes player counter-attacks use `max(d1, d2)` instead of sum) was validated in Playtest 6b but not tested here.

**Why it's a problem:** The Brutal tag is a key mechanic for making certain enemies dangerous in combat. Without testing it, we don't know if the `max(d1, d2)` math feels right at the table.

**Impact on this playtest:** Combat was present but not against Brutal enemies. Another coverage gap.

---

## Player Motivation Analysis

### Kael Mourn (Tragic) — ⚠️ Partially Served

**Goal:** Prove redemption is real, push into moral danger for truth, protect others from learning his past.

**What worked:** Kael's arc was the strongest in the mission. He found the core clue, interrogated witnesses, and made the hard choice to use the Excruciator Protocol (forbidden method) to extract the relic. His Minor Mind and Corruption Fallout ("hears Sella whisper," "shadow lags") are exactly the kind of haunting consequences that drive a tragic arc forward.

**What didn't work:** Kael's personal secret (the cult he betrayed believes he died) was never tested. The cult in this mission was the Choir of the Last Candle, not Kael's old cult, so his Forbidden Edge (Former Cultist) didn't create the paranoia it should have. His Domain (Heresy) was useful but his personal history didn't intersect with the mission.

**Verdict:** The tragic arc worked mechanically (stress, Fallout, forbidden choices) but not personally (his specific backstory didn't matter). Future missions should connect to character backstories more directly.

### Seren Vale (Winner) — ✅ Well Served

**Goal:** Efficiency, survival, protection stacking, authority use, minimize casualties.

**What worked:** Seren was the most successful character in the mission. She captured the cult lookout, mapped the plaza, planned the tactical approach (CRIT_SUCCESS), and took only 2 Body stress total. Her Body Protection 2 and Mind Protection 1 made her the most resilient character. She played exactly to her strengths: preparation, positioning, and controlled violence.

**What didn't work:** Seren's "Winner" motivation was tested but not *challenged*. She succeeded at most of her rolls. A true test of the Winner archetype would require situations where efficiency conflicts with morality (e.g., "you can save the mission but a civilian dies"). The mission didn't create enough of these trade-offs for her.

**Verdict:** The Winner archetype is well-served by the core mechanics (Protection, Mastery, tactical positioning). But the system needs more "efficiency vs. humanity" dilemmas to really test this archetype.

### Lys Thane (Combo-Seeker) — ⚠️ Frustrated

**Goal:** Find optimal solutions, use Cover creatively, exploit tag interactions, maximize effect for minimum cost.

**What worked:** Lys's D8 Cover was a good build choice. Her Ghost Protocol ability (Cover doesn't step down on 8+) was never triggered because she didn't roll 8+ on Cover spends — but the *potential* was there. Her infiltration of the cult meeting was exactly the kind of high-risk, high-reward play a combo-seeker would attempt.

**What didn't work:** Lys failed most of her rolls (Skulk+Underworld FAIL, Procure+Underworld FAIL, Deceive+Heresy CRIT_FAIL, Skulk+Underworld CRIT_FAIL). Her Cover was burned by GM fiat rather than by her own choices. The combo-seeker wants to find the *one perfect move* that makes everything work, but the dice didn't give her that opportunity. She ended with 10 stress (4 Shadow, 6 Body) and no Fallout — she paid costs but didn't get the big payoff.

**Verdict:** The combo-seeker archetype needs at least one moment where the clever build pays off big. In this playtest, Lys paid costs without getting the reward. This is partly bad luck (seed 42 was unlucky for her) and partly a system issue (2D10 Dangerous is impossible). The archetype would shine in a mission with more opportunities for creative problem-solving and fewer forced Dangerous rolls.

### Pyra Voss (Wildcard) — ✅ Well Served (Painfully)

**Goal:** Use powers to help the cell, take Corruption for effect, create interesting chaos.

**What worked:** Pyra's arc was the most dramatic. She used psychic powers 5 times, accumulated 10 Corruption, triggered Minor Fallout, and her final Hexagrammic Rebuke failure was the climactic moment of the mission. The Warp Trace clock (0→5/6) created exactly the right tension: every use fed the shadow. Her daemon-scar connection to the shadow was a great fictional hook.

**What didn't work:** Pyra failed 4 out of 5 psychic rolls. Her Witch-Sight failed twice, her Veil failed, and her Hexagrammic Rebuke failed. She was the primary engine of the mission's disaster arc, but she didn't *choose* to fail — the dice failed her. The Wildcard archetype should create chaos through *choices*, not through *bad luck*.

**Verdict:** The psyker mechanics work well (Warp Trace, Corruption costs, Protection absorption) but the Wildcard archetype needs more *meaningful choices* about when to use powers. The current system makes psychic use a binary "use it and risk Corruption" decision. Adding more nuance (e.g., "use it subtly for less effect but less cost" vs. "use it openly for more effect but more cost") would give the Wildcard more agency.

---

## Overall Design Health

### System Readiness: **Playtest-Ready with Known Issues**

The core loop (roll → difficulty → stress → fallout → clocks) is solid and produced a compelling, dramatic mission. The 4-Operation structure worked well, with each Operation escalating tension. The end-of-operation checklists ensured systematic consequence tracking.

**Strengths confirmed:**
- Difficulty removal creates real tension without eliminating competence
- Protection is visible and meaningful
- "Never hide the core clue" keeps investigation moving
- Fallout creates story, not dead ends
- Heat thresholds create escalation
- Warp Trace creates psyker-specific tension
- Clocks create temporal pressure

**Issues requiring attention:**
1. **2D10 Dangerous = automatic failure** — This is the #1 recurring issue. It removes player agency and contradicts the "competent acolytes" design principle. Needs a fix before table play.
2. **Psyker Corruption has no mid-mission pressure valve** — The spiral is intentional but needs a way to clear stress between Operations.
3. **Cover degradation should be player-driven, not GM-driven** — Players should choose to spend Cover, not have it burned by narrative fiat.
4. **Enemy Awareness didn't escalate enough** — The conditional ambush system wasn't tested. Needs a mission with a more aggressive enemy.
5. **Requisition system was underused** — Needs tighter integration into Operation structure.
6. **Brutal tag wasn't tested** — Needs combat against Brutal enemies.

### Recommended Next Steps

1. **~~Fix 2D10 Dangerous~~** — ✅ **Implemented as GM guidance.** Rather than changing the math, the GM now explicitly warns players before impossible rolls and offers alternatives (stack advantage, change approach, accept cost, spend resource). This preserves the "Dangerous = really dangerous" feel while keeping player agency.

2. **~~Psyker Corruption relief valve~~** — ✅ **Implemented as between-Operation grounding.** Psykers can now clear D3 Corruption between Operations through grounding (meditation, rites, ally help). Scene-based Refresh still exists for larger clears. Exorcist allies can perform Litany of Grounding. The Corruption spiral is still real, but the psyker has agency to manage it.

3. **~~Cover degradation player-driven~~** — ✅ **Implemented as fiction-driven foreshadowing.** Cover degradation now follows the fiction with explicit foreshadowing at each step. GM names the strain, connects step-downs to the fiction, warns at D3, and never burns Cover by fiat.

4. **Design a combat-heavy mission** — Test Brutal tag, conditional ambushes, and Enemy Awareness escalation. This mission was investigation-heavy; the combat subsystems need their own stress test.

5. **Integrate Requisitions more tightly** — Make at least one Requisition decision mandatory per Operation. The system is too large to leave optional.

6. **Connect character backstories to missions** — Kael's Former Cultist edge should create paranoia about *this* mission's cult, not just future ones. Personal stakes make the mechanics matter.

### Seed Analysis

Seed 42 was **adversarial but not unfair**. The roll distribution:
- **Seren:** 3/4 successes (75%) — she was the star
- **Kael:** 2/5 successes (40%) — mixed, as expected for a tragic character
- **Lys:** 0/4 successes (0%) — very unlucky, but the 2D10 Dangerous issue compounded this
- **Pyra:** 1/5 successes (20%) — the disaster arc was driven by bad luck

The 0% success rate for Lys is a seed issue, not a system issue. But the 2D10 Dangerous problem means that even with better luck, she would have faced automatic failures on key rolls. **This is the fix that matters most.**

---

*Playtest 9 of Dark Heresy Spire. Seed 42. Partial failure. The wrong shadow spoke. The cell survived. The Patron is watching.*
