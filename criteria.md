# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.


All criteria are held across all three test trials.
---
## 1. False Positives: At most 1 in 10 Human-written posts are falsely labeled as AI.

<!-- Your criterion. It must name a number. -->



**Why this target:** Taken directly from the example criterion, labeling a real human's work as AI is costly for user retention, and I believe 1 false positive in 10 human posts is a good ratio cutoff for false positives such that users are not deterred from returning to the writing site.



---

## 2. False Negatives: No more than 1 in 3 AI posts are falsely labeled as Human.

<!-- Your criterion. -->



**Why this target:** On the opposite side, the model should have a high enough quality to correctly label the majority of AI posts. This metric is more lenient than the previous False Positives criterion, which is a more strict and higher-priority criterion.



---

## 3. False Positives: The percentage of False Positives (out of all Human posts) is less than each of the other 'confusion matrix fields'.
Unless one of the other fields is 0, in which case the False Positives should also be 0.
```
This field to check:
(All posts that are really Human, Labeled AI) / (All Real Human posts),
The other fields: 
(All posts that are really AI, Labeled AI) / (All Real AI posts),
(All posts that are really Human, Labeled Human) / (All Real Human posts),
(All posts that are really AI, Labeled Human) / (All Real AI posts),
(All posts that are really AI, Labeled Unsure) / (All Real AI posts),
(All posts that are really Human, Labeled Unsure) / (All Real Human posts)
```

<!-- Your criterion. -->



**Why this target:** Again, False Positives are the most offensive label, so the model must seek to minimize them above all other labels.



---

## 4. Label coverage: Correct labels >= Unsure labels >= Incorrect labels, across the whole set.

<!-- Your criterion. -->



**Why this target:** This is a basic quality test, checking that wrong labels are minimized, right labels are maximized, and unsure labels are more frequent than wrong labels but less than actual right labels.



---

## 5. Score Spread: Clearly-AI text and Clearly-Human text should be at least 0.5 points apart, on the correct sides.

<!-- Your criterion. -->



**Why this target:** The model recognize clealy human text and clearly AI text to be on two opposite sides of the scoring spectrum, which is ensured if they are at least half of the spectrum apart in distance.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
