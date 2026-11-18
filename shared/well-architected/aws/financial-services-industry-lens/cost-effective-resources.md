<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/cost-effective-resources.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Cost-effective resources

Using the appropriate services, resources, and configurations for your workloads is key
 to cost savings. Consider the following when creating cost-effective resources:

You may employ internal guardrails (built using AWS Organization Service Control
 Policies) to allow a limited set of services to be provisioned to contain costs. If a workload
 requires services outside of the allow list, they need to centralized, created, and shared
 with an individual account, or created by an administrator.

Prefer managed generative AI services such as Amazon Bedrock or Amazon SageMaker AI JumpStart to minimize
 total cost of ownership by reducing the overhead of managing infrastructure, scaling, and
 updates. Where self-managed model hosting is required, benchmark deployments on AWS
 Graviton-based instances for price–performance gains and use Spot Instances for stateless
 batch jobs (for example, embeddings generation, evaluation, and model fine-tuning). Implement
 guardrails to prevent persistent provisioning of high-cost model endpoints.

###### Best practice questions

- [FSICOST07: Are you using all the available AWS credit and investment programs?](./fsicost07.html)
- [FSICOST08: Are you monitoring usage of Savings Plans regularly?](./fsicost08.html)
- [FSICOST09: Are you using the cost advantages of tiered storage?](./fsicost09.html)
- [FSICOST10: Do you use lower cost Regions to run less data-intensive or time-sensitive workloads?](./fsicost10.html)
- [FSICOST11: Do you use cost tradeoffs of various AWS pricing models in your workload design?](./fsicost11.html)
- [FSICOST12: Are you saving costs by adopting a set of modern microservice architectures?](./fsicost12.html)
- [FSICOST13: Do you use cloud services to accommodate consulting or testing of projects?](./fsicost13.html)
- [FSICOST14: How do you measure the cost of licensing third-party applications and software?](./fsicost14.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/cost-effective-resources.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
