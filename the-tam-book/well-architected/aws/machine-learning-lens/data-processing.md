<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/data-processing.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Data processing

In ML workloads, the data (inputs and corresponding desired output)
 serves important functions including:

- Defining the goal of the system: the output representation and
 the relationship of each output to each input, by means of the
 input and output pairs.
- Training the algorithm that associates inputs to outputs.
- Measuring the performance of the model against changes in data
 distribution or data drift.
- Building a baseline dataset to capture data drift.

As shown in Figure 6, data processing consists of data collection
 and data preparation. Data preparation includes data preprocessing
 and feature engineering. It mainly uses data wrangling for
 interactive data analysis and data visualization for exploratory
 data analysis (EDA). EDA focuses on understanding data, sanity
 checks, and validation of data quality.

It is important to note that the same sequence of data processing
 steps that is applied to the training data needs to also be applied
 to the inference requests.

![Figure showing data processing components](/images/wellarchitected/latest/machine-learning-lens/images/data-processing-components.png)

*Figure 6: Data processing components*

###### Sub-phases

- [Data collection](./data-collection.html)
- [Data preparation](./data-preparation.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/data-processing.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
