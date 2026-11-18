<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf02-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# LSPERF02-BP03 Elastic data processing pipelines

Design data processing architectures that automatically scale to
 accommodate both predictable and unexpected processing demands.
 Implement event-driven pipelines that efficiently handle
 high-velocity instrument data streams while maintaining strict
 controls over clinical data flows, providing consistent performance
 during peak research periods without compromising security or
 regulatory requirements.

**Desired outcome:** Implement an
 adaptive data processing architecture that automatically scales to
 meet varying workload demands while maintaining strict security and
 audit controls for each data type, particularly clinical
 information.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation guidance

To effectively manage high-velocity data processing, implement
 event-driven architectures that respond to data events in
 real-time, enabling efficient handling of instrument data streams.
 Maintain separate processing flows for different data types,
 applying appropriate controls to clinical data while optimizing
 research workloads.

Use managed AWS services like AWS Lambda, Amazon SQS, and Amazon Kinesis that automatically scale to match processing needs without
 manual intervention. Implement throttling mechanisms to protect
 downstream systems from being overwhelmed during peak research
 periods. Set up comprehensive monitoring to track performance and
 automatically adjust resources based on observed patterns, while
 maintaining regulatory guardrails to verify that automatic scaling
 doesn't compromise security requirements.

Regularly conduct load testing to verify that your architecture
 can scale as expected under stress, validating the system's
 ability to handle varying data volumes while maintaining
 performance and regulatory standards.

### Implementation steps

1. Deploy Amazon Kinesis for high-velocity data streaming.
2. Implement AWS Lambda for event-driven data processing
 and auto scaling data processing.
3. Use AWS Step Functions to orchestrate workflows.
4. Configure Amazon MSK for reliable clinical data pipelines.
5. Implement AWS Auto Scaling for predictable research peaks.

## Resources

**Related tools:**

- [Amazon Kinesis](https://aws.amazon.com/kinesis/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon MSK
 (Managed Streaming for Apache Kafka)](https://aws.amazon.com/msk/)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf02-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
