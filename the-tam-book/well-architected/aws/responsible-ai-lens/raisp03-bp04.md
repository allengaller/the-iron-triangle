<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp03-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# RAISP03-BP04 Implement output filtering to detect and block hallucinations

Build filtering mechanisms that automatically detect and block
 factually incorrect outputs, hallucinations, and misleading
 information before they reach users. These filters act as a final
 check to catch inaccuracies that your core AI system might generate.
 Use both automated reasoning checks and fact verification systems to
 validate outputs against known facts and logical consistency before
 delivery.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation considerations

1. Identify the specific types of veracity issues your system
 needs to filter based on your release criteria. Define what
 counts as hallucinations, factual errors, and misleading
 information for your use case.

For example, determine whether you need to catch mathematical
 errors, fabricated citations, invented statistics, or false
 historical claims.

1. Design your filtering strategy by deciding which verification
 methods to use and how they will work together. Plan whether
 you need automated reasoning checks, external fact
 verification, confidence scoring, or human review processes.
 Create a filtering architecture that can handle your expected
 output volume and response time requirements.
2. Implement your filtering mechanisms starting with automated
 reasoning checks that validate logical consistency,
 mathematical accuracy, and basic factual relationships. Add
 fact checking connections to reliable knowledge sources and
 databases. Build hallucination detection systems that can
 identify fabricated information patterns your system commonly
 generates.
3. Test your complete filtering system using known examples of
 your system's typical errors and hallucinations. Measure how
 effectively your filters catch different types of inaccuracies
 without blocking too many accurate outputs. Adjust detection
 thresholds and add new filtering rules based on what you
 discover during testing.

## Resources

**Related tools:**

- [Improve
 accuracy by adding Automated Reasoning checks in Amazon
 Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html)
- [Amazon
 Bedrock: Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/)
- [Amazon Comprehend Features](https://aws.amazon.com/comprehend/features/)
- [Amazon Kendra](https://aws.amazon.com/kendra/)
- [Amazon
 Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp03-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
