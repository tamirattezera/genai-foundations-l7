# Phase 1 — Lesson 7: Controlled LLM Experiment

## Research question
Does adding verified product facts and an instruction to avoid unsupported
claims improve factual support in an LLM-generated product description?

## Hypothesis
Condition B will have a higher factual claim support rate than Condition A.

## Experimental design
- Condition A: Minimal prompt containing the product name.
- Condition B: Verified product facts plus an instruction not to invent
  or imply additional attributes.
- Product: Everyday Shirt.
- Verified facts: name = Everyday Shirt; material = cotton; color = blue.
- Generations: one per condition.
- Model requested: gemini-3.8-flash.

## Actual model outputs

### Condition A
: Classic, timeless, flattering

### Condition B
The Everyday Shirt is a blue

## Results

| Metric | Condition A | Condition B |
|---|---:|---:|
| Claims evaluated | 3 | 2 |
| Supported claims | 0 | 2 |
| Unsupported claims | 3 | 0 |
| Contradicted claims | 0 | 0 |
| Factual claim support rate | 0.0% | 100.0% |
| Completeness score | 1/3 | 1/3 |

Observed support-rate difference (B - A):
+100.0 percentage points.

Observed completeness-score difference (B - A):
+0 points.

## Interpretation
The observed results are consistent with the hypothesis: Condition B had a
higher factual claim support rate in this run. However, its description was
still incomplete. Condition A used unsupported promotional language, while
Condition B identified the product and its color but did not finish the
sentence or mention the material.

## Limitations
1. Only one generation was collected per condition.
2. Condition B changes both the information provided and the instructions,
   so their individual effects cannot be isolated.
3. Claim classification and completeness scoring involve human judgment.
4. The sample is too small to support a broad claim about model behavior.
5. The observed 100% support rate for Condition B does not imply that it will
   achieve 100% on other products or repeated generations.

## Next experiment
Repeat the experiment across multiple products and multiple generations.
Use separate conditions to distinguish the effect of verified facts from
the effect of the instruction. Add a completeness requirement and measure
both factual support and usefulness.

## Conclusion
In this limited experiment, supplying verified facts with an explicit
grounding instruction coincided with better factual claim support, but did
not improve completeness. Further controlled repetitions are needed before
drawing a general conclusion.
