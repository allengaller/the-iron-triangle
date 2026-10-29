<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.dt.5-utilize-incremental-metrics-computation.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# [QA.DT.5] Utilize incremental metrics computation

**Category:** OPTIONAL

Incremental metrics computation allows teams to efficiently
 monitor and maintain data quality without needing to recompute
 metrics on the entire dataset every time data is updated. Use
 this method to significantly reduce computational resources
 and time spent on data quality testing, allowing for more
 agile and responsive data management practices.

Start by identifying the specific data quality metrics that
 are essential for your system. This could include metrics
 related to accuracy, completeness, timeliness, and
 consistency. Depending on your dataset's size and complexity,
 select a tool or framework that supports incremental
 computation. Some modern data processing tools, such
 as [Apache
 Spark](https://spark.apache.org/)
 and [Deequ](https://github.com/awslabs/deequ),
 provide built-in support for incremental computations.

Segment your data into logical partitions, often based on
 time, such as daily or hourly partitions. As new data is
 added, it becomes a new partition. Automate the computation
 process by setting up triggers that initiate the metric
 computation whenever new data is added or an existing
 partition is updated.

Continuously monitor the updated metrics to help ensure they reflect the true state
 of your data. Periodically validate the results of the incremental metrics computation
 against a full computation to ensure accuracy. As you get more familiar with the process,
 look for ways to optimize the computation to save even more on computational resources.
 This could involve refining your partitions or improving the computation logic.

**Related information:**

- [Deequ
 stateful metrics computation](https://github.com/awslabs/deequ/blob/master/src/main/scala/com/amazon/deequ/examples/algebraic_states_example.md)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.dt.5-utilize-incremental-metrics-computation.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
