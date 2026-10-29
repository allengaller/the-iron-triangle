<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp01-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# RAIDP01-BP04 Identify potential overlaps between datasets

Check for unintended data overlap between your training, evaluation,
 and auxiliary datasets. Ideally, evaluation datasets will contain
 entirely new examples that your system has never encountered during
 training, as testing on previously seen data can result in
 overconfidence in your system capabilities due to overfitting or
 memorization. Verify that you do not include public benchmarks used
 for evaluation in training data, particularly when using foundation
 models where training data provenance may be unclear. Document
 unavoidable overlaps and assess their potential impact on evaluation
 validity.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation considerations

1. Define what it means for the content of training and
 evaluation datasets to be too similar. For example, if you are
 building a bird classifier, you may not want the evaluation
 dataset to contain an image of a flock of birds and the
 training dataset to contain a sub-image from the flock image,
 even if the sub-image is contrast enhanced.
2. Define what risk there might be, if any, of having auxiliary
 and evaluation datasets overlap. For example, you may not want
 a RAG system to be tested using queries that exactly match the
 text of FAQs in the RAG document library.
3. Using your definitions of similarity, scan for unwanted
 similarities between your training, evaluation, and auxiliary
 data, and estimate the degree of overlap between each dataset.
4. If there are overlaps you cannot remove, estimate the impact
 on release criteria, adjusting release criteria as necessary.
5. Track changes in overlaps as your datasets evolve by setting
 up automated systems to flag similarities when you add or
 update data.

## Resources

**Related documents:**

- [Duplicate
 Detection with GenAI](https://arxiv.org/abs/2406.15483)
- [Prepare ML Data with Amazon SageMaker AI Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html)
- [An Analysis of Dataset Overlap on Winograd-Style Tasks](https://arxiv.org/pdf/2011.04767)
- [A Large-scale Comprehensive Dataset and Copy-overlap Aware Evaluation Protocol for Segment-level Video Copy Detection](https://arxiv.org/pdf/2203.02654)
- [Data Augmentation for Conflict and Duplicate Detection in Software
 Engineering Sentence Pairs](https://arxiv.org/pdf/2305.09608)
- [Towards Scalable Generation of Realistic Test Data for Duplicate
 Detection](https://arxiv.org/pdf/2312.17324)
- [What
 is Overfitting?](https://aws.amazon.com/what-is/overfitting/)
- [ISO/IEC
 42001:2023](https://www.iso.org/standard/42001) A.4.3 Data Resources

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp01-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
