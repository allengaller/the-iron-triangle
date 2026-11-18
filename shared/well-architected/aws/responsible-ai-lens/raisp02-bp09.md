<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp02-bp09.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# RAISP02-BP09 Design your core AI system to handle input variations

Design your system to be more resilient by building in the ability
 to handle input variations and edge cases that could cause it to
 fail or behave unpredictably. This means incorporating techniques
 like data augmentation that creates variations of your training
 examples, adversarial training that tests your system against
 challenging inputs, and exposure to diverse input formats, styles,
 and edge cases during the development process. The robustness
 techniques you choose should directly support your release criteria,
 assisting your system to perform consistently even when users
 interact with it in unexpected ways.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation considerations

1. Review your release criteria to identify expected input
 variations and how your data might change in real use, from
 variations like lighting changes in images to text typos or
 paraphrasing.
2. Create a data augmentation pipeline (automated system to
 modify training data) that generates different versions of
 your inputs. Use both simple transformations like rotations or
 text swaps, and advanced generative methods to create diverse
 examples.
3. Include robustness techniques during training by adding
 controlled noise (small random changes) to your data and using
 optimization objectives that assist your model to learn to
 ignore minor input differences.
4. Design for continuous monitoring and updating to adapt the
 system to new data, evolving environments, and unforeseen
 issues, verifying its continued robustness.
5. Refer to the Dataset Planning focus area for details on data
 related best practices for designing robust AI system.

## Resources

**Related documents:**

- [Clarify
 Semantic Robustness Evaluation](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-semantic-robustness-evaluation.html)
- [ISO/IEC
 42001:2023 A.6.1.2 Objectives for responsible development of
 AI system](https://www.iso.org/standard/42001)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp02-bp09.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
