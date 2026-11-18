<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus07.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# FSISUS07: How do you optimize batch processing components for sustainability?

Because batch processing is often found within many workloads across financial systems,
 verify that the minimum number of resources are consumed by batching transactions together
 while meeting your customer SLA and system requirements.

## FSISUS07-BP01 Optimize your batch processing systems

Because batch processing is often found within many workloads across financial
 systems, verify that the minimum number of resources are consumed by batching transactions
 together while meeting your customer SLA and system requirements.

### Prescriptive guidance

- Queue up several requests together that don't require immediate processing.
- Increase serialization to flatten utilization across your pipeline.
- Modify the capacity of individual components to prevent idling resources
 waiting for input.
- Create buffers and establish rate limiting to smooth the consumption of
 external services.
- Use the most efficient available hardware and services to optimize your
 software.
- If possible, schedule jobs during times of day where carbon intensity for power
 is lowest.
- Use managed spot training for generative AI model training to utilize spare EC2
 capacity efficiently.
- Implement parameter-efficient fine-tuning (PEFT) techniques like LoRA to reduce
 computational requirements.
- Optimize generative AI batch inference jobs using serverless architectures.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus07.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
