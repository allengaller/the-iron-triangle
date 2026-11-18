<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr04-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# RAIBR04-BP01 Narrow the use case

Identify the minimum viable use case that still delivers meaningful
 business value while reducing complexity and associated risks.
 Narrow the use case to a specific domain, industry vertical,
 geography, or user segment rather than attempting to solve broad,
 general problems. Restrict the types of inputs your system accepts
 and the formats of outputs it generates.

**Level of risk exposed if this best practice
 is not established:** Medium

## Implementation considerations

1. Evaluate current scope and identify risk reduction
 opportunities. For example, an AI medical diagnosis system
 might focus on a specific condition type rather than general
 diagnostics or limit analysis to structured lab results rather
 than free-text notes.
2. Define specific boundaries for system application. As an
 example, a financial AI advisor might serve only retail
 investors within certain portfolio sizes, using standardized
 investment products rather than complex instruments. Consider
 expertise requirements.
3. Document input and output restrictions to control risk
 exposure. Consider a customer service AI that accepts only
 structured inputs rather than free-text queries, which
 improves response reliability. Include clear guidance on
 system limitations and context for appropriate use.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr04-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
