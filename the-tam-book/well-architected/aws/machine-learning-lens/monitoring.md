<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/monitoring.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Monitoring

The model monitoring system must capture data, compare that data to the training set,
 define rules to detect issues, and send alerts. This process repeats on a defined schedule, when
 initiated by an event, or when initiated by human intervention. The issues detected in the
 monitoring phase include: data quality, model quality, bias drift, and feature attribution
 drift.

![Chart displaying model monitoring main components](/images/wellarchitected/latest/machine-learning-lens/images/key-components-monitor-phase.png)

*Figure 17: Post-deployment monitoring main components*

Figure 17 lists key components of monitoring, including:

- **Model explainability:** Monitoring system uses
 *explainability* to evaluate the soundness of the model and if the
 predictions can be trusted.
- **Detect drift:** Monitoring system detects data and concept
 drifts, initiates an alert, and sends it to the alarm manager system. Data drift is
 significant changes to the data distribution compared to the data used for training. Concept
 drift is when the properties of the target variables change. Data drift can result in model
 performance degradation.
- **Model update pipeline:** If the alarm manager identifies
 violations, it launches the model update pipeline for a re-train. This can be seen in Figure
 18. The *Data prepare*, *CI/CD/CT*, and
 *Feature* pipelines will also be active during this process.

![ML lifecycle with model update, retrain, and batch or real-time inference pipelines](/images/wellarchitected/latest/machine-learning-lens/images/ml-lifecycle-model-update-inference-pipelines.png)

*Figure 18: ML lifecycle with model update, retrain, and batch or real-time inference pipelines*

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/monitoring.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
