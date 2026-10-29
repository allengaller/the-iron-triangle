<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec08-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVSEC08-BP01 Create guardrails and controls to maintain brand safety and content moderation within your workload

Brand reputation protection can block brand association with
 inappropriate or otherwise harmful content. Having guardrails
 can maintain customer trust and potential business
 relationships while avoiding reputational damage and negative
 publicity.

## Implementation guidance

Consider implementing Amazon SageMaker AI, with the
 custom model development capability of SageMaker AI, you can
 build, train, and deploy custom machine learning models.
 Designing a guardrail for brand safety could allow you to
 develop a model that could detect inappropriate imagery in
 advertisements, classify text within content for sentiment and
 safety, and predict the likelihood of an ad placement being
 brand appropriate. With the real time inference capability of
 SageMaker AI, you can deploy your models deemed brand safe for
 real time content analysis, allowing for quick decision making
 for your solution.

Additionally, consider using AWS Config, to
 assess, audit, and evaluate resource configurations within
 your AWS environment. Config can track changes to underlying
 resources with your advertising solution to verify that
 security settings and access controls remain
 compliance-aligned for brand safety.

## Key AWS services

- AWS Config
- Amazon SageMaker AI

## Resources

- [Examples and More Information: Use Your Own Algorithm or Model](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-notebooks.html)
- [Compliance](https://docs.aws.amazon.com/config/latest/APIReference/API_Compliance.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec08-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
