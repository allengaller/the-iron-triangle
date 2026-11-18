<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus08.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# FSISUS08: How do you optimize your resource usage?

Review and optimize your resource usage by implementing either a pub/sub or pull
 mechanism instead of relying on a polling approach.

## FSISUS08-BP01 Use event-driven architecture

Implement either a pub/sub or pull mechanism instead of using a polling approach.

### Prescriptive guidance

- Implement event-driven architecture where possible to avoid idling of resources
 running and waiting for state changes.
- If event-driven architecture is not possible, modify the capacity of individual
 components to prevent idling downstream resources waiting for input.
- Avoid polling APIs or queues, instead have components and services subscribe to
 events or be notified of changes to reduce the idling of resources.
- Implement auto scaling and serverless architectures for generative AI
 workloads.
- Use managed generative AI services like Amazon Bedrock to optimize resource
 utilization.
- Apply model optimization techniques like quantization and pruning.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus08.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
