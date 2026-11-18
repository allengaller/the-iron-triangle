<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr02-bp05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# RAIBR02-BP05 Identify potential harmful events impacting safety

System outputs (content or actions) might create unintended impacts
 on the health or well-being of individuals, groups, society or the
 environment and can be misused in ways that could cause harm. Unsafe
 inputs can create harmful system responses. Understanding safety
 harms requires examining both immediate harms and downstream effects
 across different stakeholder groups, while considering how safety
 violations might cascade through system operations and user
 interactions.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation considerations

1. Consider if inputs could request content that the system is not
 designed to handle. For example, in medical advice use cases,
 can generated content present improper self-treatment
 recommendations or cause psychological distress through
 insensitive delivery? Consider both direct and indirect harm
 potential.
2. Consider input handling safety concerns and response protocols.
 For example, AI chatbots may need systems to detect crisis
 signals in user inputs and provide appropriate responses while
 avoiding harmful advice.
3. Consider physical, psychological, and environmental impacts. For
 example, could an incorrect instruction to a smart home system
 create a safety hazard?

## Resources

**Related documents:**

- [Amazon
 Bedrock Guardrails enhances generative AI application safety
 with new capabilities](https://aws.amazon.com/blogs/aws/amazon-bedrock-guardrails-enhances-generative-ai-application-safety-with-new-capabilities/)
- [Measuring
 and Mitigating Toxicity in LLMs](https://github.com/aws-samples/measuring-and-mitigating-toxicity-in-llms?tab=readme-ov-file#measuring-and-mitigating-toxicity-in-llms)
- [ISO/IEC
 42001:2023](https://www.iso.org/standard/42001) A.5.4 Assessing AI system impact on
 individuals or groups of individuals
- [ISO/IEC
 42001:2023](https://www.iso.org/standard/42001) A.5.5 Assessing societal impacts of AI
 systems

**Related video:**

- [AWS re:Invent 2024 - Responsible AI: From theory to practice with
 AWS (AIM210)](https://www.youtube.com/watch?v=SCXw2xuoF6o)

**Related tools:**

- [Amazon
 Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr02-bp05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
