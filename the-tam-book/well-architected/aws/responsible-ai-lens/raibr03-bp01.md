<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr03-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# RAIBR03-BP01 Identify the likelihood of each potential harm

Establish a risk rating methodology that considers the likelihood of
 the event occurring. The risk likelihood indicates the probability
 of a harmful event occurring when the system is deployed for the use
 case.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation considerations

1. Create a standardized likelihood scale with clear definitions.
 For example, establish ranges from *almost
 certain* (95%+ probability) to *highly
 unlikely* (less than 5% probability). Include
 specific frequency ranges for each category to maintain
 consistent evaluation.
2. Document likelihood assessments with supporting evidence. For
 example, consider a content moderation system where historical
 data shows harmful content detection failures occur in 15% of
 edge cases, placing this risk in the
 *unlikely* category. Include rationale for
 each assessment.

## Resources

**Related documents:**

- [Learn
 how to assess the risk of AI systems](https://aws.amazon.com/blogs/machine-learning/learn-how-to-assess-risk-of-ai-systems/)
- [NIST
 Risk Management Framework](https://csrc.nist.gov/projects/risk-management/about-rmf)
- [Responsible
 AI in the generative era](https://www.amazon.science/blog/responsible-ai-in-the-generative-era)
- [ISO/IEC
 42001:2023](https://www.iso.org/standard/42001) A.5.2 AI system impact assessment process

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr03-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
