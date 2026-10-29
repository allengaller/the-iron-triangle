<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf01.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Establish performance evaluation processes

Foundation models are built to perform sufficiently well on a wide variety of tasks. Their task-specific performance is tracked using leaderboards and other public metric tracking solutions. Strong performance in one task (for example, summarization) does not indicate strong performance in another task (such as question answering).

Task performance is evaluated using benchmarks built from ground truth data, and model performance against these test suites help when selecting a model for a workload. These new performance metrics expand classic performance considerations such as latency and throughput. Efficient model selection and customization requires careful consideration of the various performance requirements of a generative AI workload, which is informed by the business case.

###### Best practices

- [GENPERF01-BP01 Define a ground truth data set of prompts and responses](./genperf01-bp01.html)
- [GENPERF01-BP02 Collect performance metrics from generative AI workloads](./genperf01-bp02.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
