<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raimon02-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# RAIMON02-BP01 Create feedback loops to apply monitoring results to system improvement

Translate monitoring results, incident patterns, and performance
 trends into actionable system improvements and risk mitigation
 enhancements. Implement regular review cycles that analyze
 monitoring data across multiple time horizons, identifying both
 immediate optimization opportunities and longer-term improvement
 strategies based on usage patterns and performance drift. Update
 system components based on monitoring insights, including refining
 guardrails, adjusting model parameters, updating training data, and
 modifying deployment strategies. Track the effectiveness of
 monitoring-driven improvements by validating that changes address
 identified issues without introducing new problems or degrading
 system performance in other areas.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation considerations

1. Establish regular monitoring review cycles: daily checks for
 immediate issues, weekly trend analysis, and monthly pattern
 reviews. Example: Review ML model accuracy daily, analyze
 feature drift patterns weekly, evaluate system performance
 trends monthly.
2. Create an improvement action framework to categorize
 monitoring insights into quick fixes, medium-term adjustments,
 and long-term enhancements.
3. Build an automated alert-to-action pipeline that connects
 monitoring alerts to specific improvement workflows. Example:
 Configure Amazon SageMaker AI Model Monitor to capture incoming
 data and detect changes in model feature distributions or
 prediction patterns. Set up Amazon EventBridge to
 automatically initiate SageMaker AI Pipeline for model retraining
 when Model Monitor detects data drift beyond defined
 thresholds.
4. Implement validation checks to measure improvement
 effectiveness. Example: Compare model metrics pre and
 post-retraining, monitor downstream impacts, and validate that
 automated improvements maintain model quality standards.

## Resources

**Related documents:**

- [Automate
 model retraining with Amazon SageMaker AI Pipelines when drift is
 detected](https://aws.amazon.com/blogs/machine-learning/automate-model-retraining-with-amazon-sagemaker-pipelines-when-drift-is-detected/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raimon02-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
