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
  "confidence": 0.1171,
  "content_id": "c_e1e7572fc152",
  "creator_id": "Joseph",
  "guess": "unsure",
  "label": "not built yet",
  "model_score": 0.1171,
  "style_score": null
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

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



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
