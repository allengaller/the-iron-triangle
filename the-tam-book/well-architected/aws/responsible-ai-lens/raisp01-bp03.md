<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp01-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# RAISP01-BP03 Check if design choices have introduced new risks

Review how design decisions affect the risk profile, determining
 whether additional assessment criteria must be incorporated into the
 testing framework.

For example, choosing to use a third-party component instead of
 building your own solution might introduce new risk considerations.
 When you identify new risks or changes in risk likelihood, decide if
 you need to update your release criteria to properly test for these
 issues before release.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation considerations

1. Review the AI system document, design decisions and tradeoffs
 for each component.
2. Determine if the design decisions result in new risks or
 updates to already identified risks in terms of severity and
 likelihood.
3. Update the risk assessment accordingly.
4. Review the release criteria and determine if the release
 criteria sufficiently covers the identified risks.
5. Update the release criteria accordingly.

## Resources

**Related documents:**

- [ISO/IEC
 42001:2023 A.6.2.3 Documentation of AI system design and
 development](https://www.iso.org/standard/42001)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp01-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
