<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/questions-4.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Questions

Employ version control for source code, data, and ML artifacts
 to ensure traceability and reliability of production ML
 deployments. Version control and traceability may be required by
 applicable regulatory frameworks, if for example models are
 deployed in support of medical devices.

Data science in healthcare often depends on open-source
 libraries for data processing, model development, training, and
 hosting. Establish a process to review the privacy and license
 agreements for all software and ML libraries needed throughout
 the ML lifecycle. Verify that these agreements comply with your
 organization’s legal, privacy, and security requirements.

Many ML workflows do not require identified health data.
 Applying ML to deidentified data is one way to develop
 AI-powered applications without compromising privacy or data
 security. Cloud services like the
 [Amazon Comprehend Medical DetectPHI API](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-phi.html) can streamline
 generating deidentified datasets.

Statistical models trained on real-world health data are
 susceptible to biases. Health data may inadvertently be
 collected from populations of individuals with similar
 characteristics, such as median household income, social
 determinants of health, and access to care. Care setting and
 health insurance coverage may also impart biases. For example,
 treatment cohorts may exhibit higher household income because
 such individuals may have greater access to advanced care.

Trained models may be misleading if biases are not quantified
 and mitigated. Also, models may be inaccurate when trained on
 biased data and applied to settings with different
 distributions. Examine data distributions and
 [perform
 analyses](https://aws.amazon.com/sagemaker/clarify/) to quantify and mitigate biases before training
 models.

Health data is often complex, and subject to temporal variations
 in quality and concept expression. Model performance may degrade
 over time due to data quality, model quality, and concept drift.
 Create a baseline for data quality, and
 [automate
 monitoring performance](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html) in production. Automate alerts for
 changes in data quality or distributions, such as age deciles
 and prevalence of relevant chronic diseases.
 [SageMaker AI
 Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/) provides an end-to-end framework model
 monitoring and lifecycle management.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/questions-4.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
