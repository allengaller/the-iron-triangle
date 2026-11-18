<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Choosing a system configuration

Teams test different candidate configurations of their system,
 including different versions of components or models during
 development using validation sets to determine which performs
 best. Different versions can come from different component
 choices, hyperparameters, training settings, or model
 architectures. Teams set up controlled comparisons between
 versions on the same validation data, then use paired statistical
 tests to determine if one version is statistically better than the
 other based on release criteria. Evaluation sets stay separate
 from component selection to avoid biasing final performance
 measurements and release decisions.

###### Best practices

- [RAISP04-BP01 Use paired tests to choose from candidate designs](./raisp04-bp01.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
