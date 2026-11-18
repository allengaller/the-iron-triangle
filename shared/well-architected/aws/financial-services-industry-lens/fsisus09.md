<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus09.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# FSISUS09: How do you optimize areas of your code that use the most resources?

Analyze and optimize your code's efficiency to improve resource utilization.

## FSISUS09-BP01 Monitor and optimize areas of code that are the most compute resource-intensive

### Prescriptive guidance

- Use [CodeGuru](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html) and [Amazon Q Developer](https://aws.amazon.com/q/developer/) to optimize your code's efficiency.
- If possible, choose the most efficient OS and programming languages to run your
 code.
- Remove unnecessary code such as modules that perform sorting or formatting.
- Optimize generative AI model inference code using efficient model
 architectures.
- Implement model distillation to create smaller, task-specific generative AI
 models.
- Use specialized instances like EC2 Inferentia for generative AI workloads.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus09.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
