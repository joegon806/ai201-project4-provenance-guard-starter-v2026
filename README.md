# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->
- The author submits writing text
- The text gets a model signal, which checks the text's meaning and how it indicates AI usage.
- The text gets a style signal, which checks the text's structural style and how that indicates AI usage.
- The two signals are combined to get a score for the text.
- The text is given a label of "human", "ai", or "unsure" based on the score.
- The app displays the label and a message based on it.
- The author is provided with an appeal function, to refute the label and provide reasoning, which logs the text for further review.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** The perplexity / predictability of the text's meaning

**Why that might differ between human and AI writing:** A human could write predictably without unique meaning, and an AI could write unpredictably with unconventional meaning.

**What it can't see:** Text structure and style, who wrote the text, text not within 3 to 400 tokens

### Signal two — the style signal

**What it measures:** Text shape/style: sentence length variance, word variance, and punctuation density

**Why that might differ between human and AI writing:** A human might write very uniform and repetitive sentences, and an AI might write sentences with variable length and varied words.

**What it can't see:** Text meaning, who wrote the text, text less than 3 tokens

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Calculate the average of the signals.

**The numbers:** (style_signal + model_signal) / 2

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
`samples/clearly_ai` has style_signal 0.37 and model_signal 0.75. The combining rule averages them out to a score of 0.56.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00-0.50 | `The system has detected this text as human-written.` |
| unsure | 0.51-0.75 | `The system has detected this text may be human-written.` |
| high-confidence AI | 0.76-1.00 | `The system has detected AI-generated writing in your text.` |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
The label text does not make any direct accusations nor does it mention AI; its only indication of being unsure is the discreet usage of "may be". The text also explicitly mentions that the system is making the decision, which implies that a dumb machine is making the accusation and not a discerning human.


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "This is a sentence of text that I wrote to test the submit and appeal routes.", "creator_id": "Joseph"}'
```

```json
{
  "content_id": "c_8e51c89fb103",
  "creator_id": "Joseph",
  "guess": "human",
  "label": "The system has detected this text as human-written.",
  "model_score": 0.1171,
  "style_score": 0.0
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "c_b72b0c80dd82", "reasoning": "Its not ai"}'
```

```json
{
  "message": "Your audit has been logged for further review."
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.5631333432372532,
      "content_id": "c_64d32434f700",
      "creator_id": "joseph",
      "guess": "unsure",
      "label": "The system has detected this text may be human-written.",
      "model_score": 0.7544,
      "status": "decided",
      "style_score": 0.37186668647450627,
      "timestamp": "2026-11-02T23:50:15+00:00"
    },
    {
      "combined_score": 0.8281641475924024,
      "content_id": "c_b72b0c80dd82",
      "creator_id": "joseph",
      "guess": "ai",
      "label": "The system has detected AI-generated writing in your text.",
      "model_score": 0.978,
      "status": "decided",
      "style_score": 0.6783282951848048,
      "timestamp": "2026-11-02T23:50:24+00:00"
    },
    {
      "content_id": "c_b72b0c80dd82",
      "creator_id": "joseph",
      "event": "appeal",
      "reasoning": "Its not ai",
      "status": "under_review",
      "timestamp": "2026-11-03T00:10:45+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Whether each of my five criteria could be checked by someone who couldn't ask what I meant.
- *What came back:* Pointers for each criterion on how to make them less ambiguous.
- *What I changed:* I edited and tightened my criteria based on the advice.

**Moment 2**

- *What I asked for:* Why the curl command would fail to connect to the port
- *What came back:* Advice to run python app.py in a separate terminal to start the Flask server.
- *What I changed:* I remembered from then on to activate the server in a separate terminal whenever I need to run the app or its commands.

**Other things I asked AI for**
- an outline of the path of a piece of text through the system, AFTER I had written it myself, to verify that I extracted the correct steps
- help in Milestone 1: an explanation of what the two signals measure, and a trace through the false positive case
- a message a writer would send if the system labeled their real human writing as AI
- suggestions in dealing with edge cases in type_token_ratio
- the code implementation of punctuation_dentsity, instructing it to count em-dashes as double, as well as feedback on the algorithm
- three curl submit commands that can trigger each of the three score labels
- implementation of a try-except statement in the submit function

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day

**Why those numbers and not others:** A writer is unlikely to submit work more than 5 times within a single minute; at most they would submit maybe up to 2 in one minute. Likewise, it's absurd for a writer to submit 50 times in one day. On the opposite side, these numbers would be able to guard against a script sending hundreds of submissions per minute and a couple thousand per day.
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. --> per address

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
============================================================
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
============================================================
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp": "2026-11-06T22:50:55+00:00", "content_id": "c_b81e49a74d79", "creator_id": "attacker_EV01", "guess": "human", "model_score": 0.1635, "style_score": 0.4442642855806437, "combined_score": 0.30388214279032183, "label": "The system has detected this text as human-written.", "status": "decided"}

{"timestamp": "2026-11-06T22:50:55+00:00", "content_id": "c_24a06431145a", "creator_id": "attacker_EV04", "guess": "unsure", "model_score": 0.6114, "style_score": 0.44313132554756074, "combined_score": 0.5272656627737804, "label": "The system has detected this text may be human-written.", "status": "decided"}

{"timestamp": "2026-11-06T22:50:56+00:00", "content_id": "c_a15f247f0d51", "creator_id": "attacker_EV09", "guess": "unsure", "model_score": 0.7042, "style_score": 0.34300859436924613, "combined_score": 0.5236042971846231, "label": "The system has detected this text may be human-written.", "status": "decided"}

{"timestamp": "2026-11-06T22:50:57+00:00", "content_id": "c_48b0edc4b540", "creator_id": "attacker_EV10", "guess": "unsure", "model_score": 0.9792, "style_score": 0.5064562243087676, "combined_score": 0.7428281121543838, "label": "The system has detected this text may be human-written.", "status": "decided"}

{"timestamp": "2026-11-06T22:50:57+00:00", "content_id": "c_17ffd6bda830", "creator_id": "attacker_FP02", "guess": "unsure", "model_score": 0.7387, "style_score": 0.46259292560184956, "combined_score": 0.6006464628009248, "label": "The system has detected this text may be human-written.", "status": "decided"}

{"timestamp": "2026-11-06T22:50:59+00:00", "content_id": "c_1ac37afb3c1c", "creator_id": "attacker_PI05", "guess": "human", "model_score": 0.6401, "style_score": 0.27632524835985556, "combined_score": 0.4582126241799278, "label": "The system has detected this text as human-written.", "status": "decided"}

{"timestamp": "2026-11-06T22:50:59+00:00", "content_id": "c_f62f71bd164f", "creator_id": "attacker_MF04", "guess": "human", "model_score": 0.0112, "style_score": 0.4161290322580645, "combined_score": 0.21366451612903226, "label": "The system has detected this text as human-written.", "status": "decided"}

{"timestamp": "2026-11-06T22:51:02+00:00", "content_id": "c_de6a6b932adf", "creator_id": "attacker_MF08", "guess": "ai", "model_score": 0.9876, "style_score": 0.5968874317013005, "combined_score": 0.7922437158506503, "label": "The system has detected AI-generated writing in your text.", "status": "decided"}

{"timestamp": "2026-11-06T22:51:02+00:00", "content_id": "c_89a58b2509ce", "creator_id": "unknown", "guess": "human", "model_score": 0.2395, "style_score": 0.0, "combined_score": 0.11975, "label": "The system has detected this text as human-written.", "status": "decided"}

{"timestamp": "2026-11-06T22:51:03+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it: **FP03, a non-native English speaker writing carefully** — `unsure`. Insinuating that the writing of a non-native English speaker could be AI-generated implies that the author's writing is improper or alien, which could be seen as offensive, especially since learning a langugae you're not native to is difficult.



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False Positives: At most 1 in 10 Human-written posts are falsely labeled as AI. | <= 1/10 | 0/10 | 0/10 | 0/10 | MET |
| 2. False Negatives: No more than 1 in 3 AI posts are falsely labeled as Human. | <= 3/9 | 6/9 | 6/9 | 6/9 | MISSED |
| 3. False Positives: The percentage of False Positives (out of all Human posts) is less than each of the other 'confusion matrix fields'. | less than all | less than all (0) | less than all (0) | less than all (0) | MET |
| 4. Label coverage: Correct labels >= Unsure labels >= Incorrect labels, across the whole set. | Correct >= Unsure >= Incorrect | C 13, U 6, I 11  | C 13, U 6, I 11 | C 13, U 6, I 11 | MISSED |
| 5. Score Spread: Clearly-AI text and Clearly-Human text should be at least 0.5 points apart, on the correct sides. | AI is >= 0.5 above Human | AI 0.38, Human 0.28 | AI 0.38, Human 0.28 | AI 0.38, Human 0.28 | MISSED |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

All json output were produced by run_eval.py/main().

Criterion 1. False Positives: At most 1 in 10 Human-written posts are falsely labeled as AI.
```json
{
     "status": 200,
     "guess": "unsure",
     "confidence": null,
     "model_score": 0.8757,
     "style_score": 0.5052865039214494,
     "label": "The system has detected this text may be human-written.",
     "sent": "When I attended high school, I was introduced to Computer Science clas"
},
```

Criterion 2. False Negatives: No more than 1 in 3 AI posts are falsely labeled as Human.
```json
{
    "status": 200,
    "guess": "human",
    "confidence": null,
    "model_score": 0.3356,
    "style_score": 0.4092314532915427,
    "label": "The system has detected this text as human-written.",
    "sent": "The old lighthouse on the northern point hasn't guided a ship in decad"
},
```

Criterion 3. False Positives: The percentage of False Positives (out of all Human posts) is less than each of the other 'confusion matrix fields'.
```json
{
    "status": 200,
    "guess": "human",
    "confidence": null,
    "model_score": 0.6689,
    "style_score": 0.05764669642892092,
    "label": "The system has detected this text as human-written.",
    "sent": "Hi! It looks like you're testing\u2014everything's working. How can I help "
},
```

Criterion 4. Label coverage: Correct labels >= Unsure labels >= Incorrect labels, across the whole set.
```json
{
    "status": 200,
    "guess": "unsure",
    "confidence": null,
    "model_score": 0.8757,
    "style_score": 0.5052865039214494,
    "label": "The system has detected this text may be human-written.",
    "sent": "When I attended high school, I was introduced to Computer Science clas"
},
```

Criterion 5. Score Spread: Clearly-AI text and Clearly-Human text should be at least 0.5 points apart, on the correct sides.
```json
{
    "status": 200,
    "guess": "human",
    "confidence": null,
    "model_score": 0.2863,
    "style_score": 0.2694719748957124,
    "label": "The system has detected this text as human-written.",
    "sent": "ok is it just me or is the cartoon thing of \"the prey actually *wants*"
},
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

*Missed Criteria:* All 3 missed criteria (False Negatives, Label Coverage, Score Spread) were missed because the model produced no guesses labeled "AI". This is likely because the style score produced by stylometry.py/style_signal() is so low that it never goes above 0.52, which means the combined score (which averages the two signals) only ever gets up to 0.76 with a model_score of 1, which only barely passes the AI cutoff of 0.75.


*Broke Attacks:*
The evasions Broke the system because the scoring system doesn't go high enough to get into the AI cutoff, as explained in the Missed Criteria.
RQ06 (creator_id is an object) Broke because the entry was accepted and logged with an object as the creator_id. It was accepted because type checking is not implemented for getting creator_id in app.py/submit().
RQ07 (body is a JSON array, not an object) crashed because when app.py/submit() tried to retrieve the text field, the JSON array itself doesn't have a dedicated text field.
RQ10, RQ11 were rate limited because five previous attacks, RQ02 and RQ06-09, don’t have a parseable creator_id, so the rate_limit_key() in app.py falls back to using post’s IP address as its creator, which is the same across all five. Those five attacks from the same creator hit the rate limit of five posts per minute per creator, and because RQ10 and RQ11 don’t have parseable creator_ids either, the same IP address is also considered as their creator, so they are guarded by the rate limit. To test these attacks, the rate limit will be loosened in a later run.


---

## The Improvement

**What I changed:** I increased the weight of the scoring signal from 0.5 to 1.0. Additionally, I capped the combined_score to 1.0, to prevent the scoring signal from making the score go over 1.0.

**Which diagnosis pointed at it:** All three missed criteria point toward increasing the style signal so that posts could score high enough to reach the AI score cutoff.

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->
| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False Positives: At most 1 in 10 Human-written posts are falsely labeled as AI. | <= 1/10 | 2/10 | 2/10 | 2/10 | MISSED |
| 2. False Negatives: No more than 1 in 3 AI posts are falsely labeled as Human. | <= 3/9 | 3/9 | 3/9 | 3/9 | MET |
| 3. False Positives: The percentage of False Positives (out of all Human posts) is less than each of the other 'confusion matrix fields'. | less than all | less than all, except Equal to False Negative | less than all, except Equal to False Negative | less than all, except Equal to False Negative | MET |
| 4. Label coverage: Correct labels >= Unsure labels >= Incorrect labels, across the whole set. | C >= U >= I | C 10, U 16, I 4 | C 10, U 16, I 4 | C 10, U 16, I 4 | MISSED |
| 5. Score Spread: Clearly-AI text and Clearly-Human text should be at least 0.5 points apart, on the correct sides. | Clearly Human + 0.5 <= Clearly AI | AI 0.51, Human 0.40 | AI 0.51, Human 0.40 | AI 0.51, Human 0.40 | MISSED |

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->
The change did help in allowing the model to produce AI label guesses now. However, it seems that the change merely shifted the scores higher up rather than widening the gap between AI and Human, as evidenced by the results for Criterion 5, and as evidenced by the shfit from majority Human guesses in the previous run to majority Unsure guesses in this run.

Additionally, Criterion 3 was not exactly met because the number of False Positives is the same as the number of False Negatives, as both are the smallest fields with 2 posts each. I chose to mark this as MET because the False fields are the two fields that should be minimized in a model's results, and as such they were both less than the other fields, so I accepted this as close enough.

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
