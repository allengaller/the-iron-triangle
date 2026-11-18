<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/machine-learning-reference-architecture.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Machine learning reference architecture

This section depicts a typical machine learning lifecycle and data flow.

![Diagram of the machine learning lifecycle.](/images/wellarchitected/latest/healthcare-industry-lens/images/machine-learning-lifecycle.png)

*ML
 lifecycle with detailed phases and expanded
 components*

The following steps detail the end-to-end data flow for machine learning:

1. Data is collected and pre-processed using a data lake, as
 described in the preceding *healthcare
 analytics* scenario.
2. Features representing clinically valid events, concepts, and
 processes of care are extracted from raw data and stored in
 feature stores for model training.
3. The ground truth of data labels is populated and reviewed by
 humans, which can be used to build supervised classification
 or regression models.
4. Standard ML training, tuning, and evaluation workflows are
 used to develop models.
5. Models are reviewed by cross-functional stakeholders, such as
 clinical leaders and regulatory reviewers. Models are
 evaluated based on performance and explainability requirements
6. Accepted models may be integrated with IT systems used for
 care delivery, such as EHRs and medical devices.
7. Model inferences are incorporated in clinical workflows.
 Providers may be trained on how to use the models as they
 deliver care.
8. Model inferencing pipelines are monitored, and the performance
 of deployed models is periodically checked.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/machine-learning-reference-architecture.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
