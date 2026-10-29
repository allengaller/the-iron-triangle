<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel05-bp01.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# GENREL05-BP01 Load-balance inference requests across all regions of availability

Inference to a foundation model may be available over a local or
 large area of availability. Verify that you have resources
 available across that area to service inference requests
 reliably regardless of where they are coming from.

**Desired outcome:** When
 implemented, this best practice improves the reliability of your
 generative AI workload by creating a highly available
 environment for serving inference requests.

**Benefits of establishing this best
 practice:**
[Scale
 horizontally to increase aggregate workload availability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html)
 - Load-balanced inference requests across horizontally scaled
 infrastructure enable inference requests to be serviced evenly
 across a region of availability.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

Use load balancing and multi-Region deployment strategies to
 distribute inference requests across multiple AWS Regions and
 Availability Zones. This helps maintain consistent performance
 and availability in the face of regional disruptions or
 network issues. Consider using Amazon Bedrock's cross-Region
 inference profiles to route requests to the nearest available
 endpoint. For self-hosted models on Amazon SageMaker AI,
 implement a multi-AZ deployment with an Amazon SageMaker AI
 Inference Endpoint configured for auto-scaling to
 automatically distribute and scale traffic across Regions.

This strategy provides improved reliability, reduced risk of
 single points of failure, and better geographic coverage for
 global users. Potential trade-offs include increased network
 latency and operational complexity.

### Implementation steps

1. Configure Amazon Bedrock cross-Region inference profiles
 or deploy self-hosted models on Amazon SageMaker AI
 Inference Endpoints across multiple Availability Zones.
2. Set up an Amazon SageMaker AI Inference Endpoint with
 auto-scaling enabled to distribute traffic based on
 health and latency.
3. Implement health checks and automated failover to
 maintain availability.
4. Monitor performance metrics like latency, error rates,
 and throughput across Regions.

## Resources

**Related best practices:**

- [REL04-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_identify.html)
- [REL10-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html)

**Related documents:**

- [Supported Regions and models for inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)

**Related examples:**

- [Getting Started with cross-Region inference in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/getting-started-with-cross-region-inference-in-amazon-bedrock/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel05-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
