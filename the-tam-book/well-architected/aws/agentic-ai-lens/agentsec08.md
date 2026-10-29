<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec08.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Secure agent inputs and outputs

Agents process inputs from users, tools, and other agents, and
 they generate outputs for downstream systems, memory stores, and
 end users. Without proper validation, adversarial inputs such as
 prompt injection can influence agent behavior, and agent outputs
 can inadvertently disclose sensitive information or generate
 harmful content. Multi-layer validation at both the input and
 output boundaries helps verify that agents operate safely within
 their intended scope.

## Capability intent

- Every agent input surface (direct user messages, tool
 outputs, inter-agent messages, retrieved external content,
 and memory reads) has validation appropriate to its risk
 profile, with no input reaching the agent's reasoning
 process unchecked.
- Indirect prompt injection through retrieved documents, web
 pages, and API responses is treated as a first-class risk
 and filtered with the same rigor applied to direct user
 inputs.
- Agent outputs are inspected for personally identifiable
 information (PII), credentials, and other sensitive data on
 every outbound path (user responses, inter-agent messages,
 memory writes, and audit logs), with consistent masking or
 blocking applied at each boundary.
- Validation strictness is calibrated to the likelihood and
 impact of each risk scenario rather than applied uniformly,
 and telemetry on confidence scores, blocked content, and
 false-positive rates drives continual tuning.
- Filtering and guardrail decisions are logged with enough
 context to support compliance auditing, to detect systemic
 data leakage patterns, and to feed periodic re-optimization
 of denied topics, sample prompts, and filter thresholds.

## Common issues to watch for

- Input and output boundaries receive uneven defense, with
 rigorous checks on user inputs but little coverage for tool
 outputs, retrieved external content, inter-agent messages,
 and memory reads, leaving the most commonly targeted vectors
 unprotected.
- Guardrails are treated as a one-time configuration rather
 than a tuning loop, so denied topic definitions, filter
 thresholds, and assessment modes decay as attack patterns
 and data classifications change.
- Guardrail and filtering decisions are not captured with
 enough context to tell when validation is degrading or which
 categories need retuning, so quality issues stay invisible
 until an incident surfaces them.
- Sensitive information controls lean on the model to
 self-censor rather than on enforced output filtering, so PII
 and credentials pulled in from tool outputs or retrieved
 documents flow through whenever the model repeats them.
- Filter rules are either overly broad, which erodes user
 trust and pushes teams to weaken or disable them, or overly
 narrow, which leaves gaps. Neither side has a feedback loop
 against annotated outcomes to calibrate strictness by risk
 scenario.

###### Best practices

- [AGENTSEC08-BP01 Multi-layer input validation and prompt injection defense](./agentsec08-bp01.html)
- [AGENTSEC08-BP02 Output filtering for sensitive information](./agentsec08-bp02.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec08.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
