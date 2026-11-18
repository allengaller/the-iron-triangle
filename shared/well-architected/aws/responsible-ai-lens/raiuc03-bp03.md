<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raiuc03-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# RAIUC03-BP03 Identify the type of AI required by your AI use case

Selecting the appropriate type of AI solution is a critical decision
 that fundamentally shapes your project's success and risk profile.
 Your choice of traditional ML, generative AI, or agentic AI must
 align with your specific use case requirements, data availability,
 and desired outcomes. The decision impacts everything from
 development complexity and resource requirements to explainability
 and risk management needs. A misaligned choice can lead to project
 failure, increased costs, or unmanageable risks, while the right
 selection creates a foundation for successful AI implementation that
 meets business objectives while maintaining appropriate controls.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation considerations

1. Determine if your use case primarily involves recognizing
 patterns in complex but pre-defined input data. If so, you may
 need traditional ML. Examples include fraud detection, demand
 forecasting, or quality control systems where patterns exist
 but are too complex for explicit rules.
2. Determine if your use case requires understanding widely
 varying inputs, including natural language, and creating
 new content or providing human-like responses. If so, you may
 need Generative AI. Examples include media creation, code
 generation, and advanced customer chatbots.
3. Determine if your use case requires breaking down high-level
 user objectives into workflows, and potentially reconfiguring
 the workflows depending on the results of intermediate tasks,
 as opposed to just responding to queries or making
 predictions. The use of a **natural
 language interface** for users to communicate these
 complex, high-level intents and receive updates is one of the
 primary characteristics of this approach. If so, you may need
 agentic AI. Examples include research and travel assistants.

## Resources

**Related documents:**

- [AWS AI Services](https://aws.amazon.com/machine-learning/ai-services/)
- [AWS Responsible AI](https://aws.amazon.com/machine-learning/responsible-ai/)
- [ISO/IEC
 42001:2023](https://www.iso.org/standard/42001) A.6.2.2 AI system requirements and
 specification
- [NIST
 Artificial Intelligence Risk Management Framework (NIST AI
 100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf): MAP2.1, MAP2.2, MAP2.3

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raiuc03-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
