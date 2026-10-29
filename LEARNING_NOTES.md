# Generative AI Foundations — Learning Notes

**Learner:** Tamirat Tezera  
**Practical experiment:** Evaluating how prompt grounding affects factual support in generated product descriptions  
**Notebook:** [Google Colab — Controlled LLM Experiment](https://colab.research.google.com/drive/19fJ4D4EOrnqKvdbx_z6dZdIB1Zy7Xm7P?usp=sharing)

## 1. What Is Generative AI?

Generative Artificial Intelligence (GenAI) refers to AI systems that generate new content, such as text, images, audio, video, and code, based on patterns learned from training data.

A useful conceptual relationship is:

- **Artificial Intelligence (AI):** The broader field of building systems that perform tasks associated with intelligence.
- **Machine Learning (ML):** Methods that learn patterns from data.
- **Deep Learning (DL):** Machine learning based on multilayer neural networks.
- **Generative AI:** Systems designed to generate content; many modern GenAI systems use deep learning.

These categories overlap, but not every AI system is generative.

### Applications

Generative AI can support software development, education, research, content creation, customer support, document analysis, and product discovery.

Its output still requires evaluation, especially when factual accuracy, privacy, or safety matters.

## 2. How Large Language Models Work

Large Language Models (LLMs) generate text by predicting tokens based on preceding context and learned patterns.

- **Tokens:** Units of text processed by a model. A token can represent a word, part of a word, punctuation, or another text unit.
- **Context window:** The information the model can process within a request, including relevant instructions, conversation history, and supplied data.
- **Transformer architecture:** A neural-network architecture that uses mechanisms such as attention to model relationships between tokens.
- **Prompt:** The instructions and information provided to guide the model's response.
- **Output generation:** The model produces a sequence of tokens according to its learned patterns and generation settings.

An LLM is not automatically a reliable database or a reasoning system that verifies every statement against reality. Its outputs need to be checked against appropriate evidence.

## 3. Models, Prompting, and Generation Settings

Different models can vary in capability, latency, cost, context capacity, and output quality. Model selection should depend on the task rather than brand popularity alone.

Prompting can influence outputs through:

1. **Task clarity:** Clearly state what the model should produce.
2. **Context:** Supply relevant information needed for the task.
3. **Constraints:** Explain what the model must avoid or preserve.
4. **Output requirements:** Specify format, length, and expected structure.
5. **Evaluation:** Compare outputs against defined criteria rather than relying only on intuition.

Generation settings, such as output-token limits and supported sampling parameters, can also affect results. A fair model comparison should hold relevant settings constant and document any differences.

## 4. Hallucinations, Bias, and Limitations

A hallucination occurs when a model generates information that is false, unsupported, or presented with more certainty than the evidence warrants.

Potential causes and contributing factors include incomplete context, ambiguous prompts, gaps in learned information, and generation that is not grounded in reliable evidence.

Other limitations include:

- Bias inherited from training data or reinforced by system design.
- Outdated or incomplete information.
- Inconsistent responses to similar prompts.
- Difficulty distinguishing plausible wording from verified facts.
- Sensitivity to prompt wording and context.
- Privacy, security, and misuse risks.

Responsible use requires verification, appropriate human oversight, privacy protection, and clear communication about uncertainty. For higher-stakes applications, additional testing and safeguards are necessary.

## 5. GenAI Application Architecture

A typical GenAI application can be understood as a pipeline:

1. **User interface:** Collects the user's request.
2. **Application logic:** Validates the request and applies business rules.
3. **Context and data layer:** Retrieves relevant information, such as verified product facts.
4. **Model/API layer:** Sends the prompt and context to a model.
5. **Output processing:** Validates, structures, or filters the response.
6. **Evaluation and monitoring:** Measures quality, errors, cost, latency, and safety.

For example, an e-commerce application could generate product descriptions from a catalog. The catalog should remain the source of truth for product attributes; generated text should not silently invent specifications.

A reliable application does not treat a successful API response as proof that the content is correct.

## 6. Practical Experiment: Grounded vs. Ungrounded Prompting

### Research question

Does providing verified product facts and explicit instructions against unsupported claims improve the factual support of an LLM-generated product description?

### Hypothesis

The prompt containing verified facts and explicit constraints will produce a higher factual-support rate than a general prompt.

### Product facts

The fictional product was defined with three verified attributes:

- Name: Everyday Shirt
- Material: Cotton
- Color: Blue

### Experimental conditions

**Condition A — General prompt:** Asked the model to write a short product description without providing the verified attributes.

**Condition B — Grounded prompt:** Supplied the product name, material, and color, and instructed the model not to invent or imply additional attributes.

The same model and output-token limit were used for the comparison.

### Observed outputs

- **Condition A:** “Classic, timeless, flattering” (the saved output included a leading colon).
- **Condition B:** “The Everyday Shirt is a blue”

The outputs were evaluated at the claim level using three labels:

- **Supported:** Directly supported by the supplied facts.
- **Unsupported:** Not established by the supplied facts.
- **Contradicted:** Conflicts with the supplied facts.

### Results

| Metric | Condition A | Condition B |
|---|---:|---:|
| Supported claims | 0 | 2 |
| Unsupported claims | 3 | 0 |
| Contradicted claims | 0 | 0 |
| Factual-support rate | 0% | 100% |
| Completeness score | 1/3 | 1/3 |

The factual-support rate was calculated as:

**Supported claims ÷ (supported claims + unsupported claims + contradicted claims) × 100**

These percentages describe this particular trial and its manual claim labels. They are not general estimates of model performance.

The completeness score reflects the evaluation rubric used for this experiment. Condition B included the product name and color but omitted the material and produced an incomplete sentence.

### Interpretation

Condition B performed better on factual support in this single trial. This is consistent with the hypothesis, but it does not prove that grounded prompts will always perform better.

The experiment also demonstrates that factual support and completeness are separate quality dimensions. A response can avoid unsupported claims and still fail to provide all requested information or produce polished text.

### Limitations

1. Only one output was evaluated for each condition.
2. The prompts differed in both supplied information and explicit constraints, so their individual effects cannot be isolated.
3. Claim classification involved human judgment.
4. The evaluation used a small, fictional product dataset.
5. The results may not generalize to other products, prompts, models, or tasks.

A stronger follow-up would use multiple trials, separate the effects of context and constraints, define a more detailed rubric, and compare results across representative examples.

## 7. Responsible Experimentation and Development Environment

The experiment used Python and the Google GenAI SDK to send prompts to a language model and preserve its outputs for evaluation.

Important practices include:

- Keep API keys in environment variables or notebook secret stores.
- Never hardcode secrets into notebooks or publish them in outputs.
- Record the model name, prompt, relevant generation settings, and outputs.
- Separate raw observations from evaluation labels and interpretations.
- Avoid changing multiple experimental variables when trying to identify causation.
- Disclose limitations and avoid making claims stronger than the evidence supports.
- Monitor API usage and cost when repeating experiments.

## 8. Key Lessons

1. GenAI is useful for generating content, but generated content is not automatically verified.
2. Prompt quality includes both instructions and the evidence supplied to the model.
3. Grounding a response in verified information is a useful design strategy for factual tasks.
4. Factual support, completeness, relevance, and readability should be evaluated separately.
5. Controlled experiments require clear hypotheses, documented conditions, consistent evaluation criteria, and honest limitations.
6. One successful example is evidence about that example—not proof of a general rule.
7. In production applications, reliable data sources, validation, testing, and human oversight complement prompt engineering.

## Conclusion

This practical exercise connected LLM prompting with experimental design and application engineering. Rather than judging generated text only by how convincing it sounds, I evaluated whether its claims were supported by the available facts.

The main takeaway is that building useful GenAI applications requires more than obtaining a model response. It requires grounding, measurable evaluation, responsible handling of data and credentials, and transparent reporting of limitations.
