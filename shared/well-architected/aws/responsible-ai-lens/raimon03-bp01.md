<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raimon03-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# RAIMON03-BP01 Establish mechanisms for honoring stakeholder obligations

Consider how to honor obligations you many have to upstream
 stakeholders (such as people who contributed content to an
 evaluation or training dataset) and downstream stakeholders (such as
 workflows that have taken dependencies on your AI system).

**Level of risk exposed if this best
 practice is not established:** High

## Implementation considerations

1. Review your dataset registry to decide the correct way to
 handle each dataset, for example should it be kept for re-use,
 kept as a required record, or deleted.
2. Review logs and customer agreements to identify potential
 downstream dependents and determine a decommissioning strategy
 that provides appropriate notice.

## Resources

**Related tools:**

- [Overview
 of the decommissioning process](https://docs.aws.amazon.com/controltower/latest/userguide/decommissioning-process-overview.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raimon03-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
