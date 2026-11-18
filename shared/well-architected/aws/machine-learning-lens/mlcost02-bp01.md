<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost02-bp01.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# MLCOST02-BP01 Identify if machine learning is the right solution

Evaluating whether machine learning is the appropriate solution for
 your business problem is crucial for cost optimization. Not every
 problem requires ML solutions, and sometimes simpler approaches may
 be more effective and less costly. By thoroughly evaluating
 alternatives against ML approaches, you can make informed decisions
 that optimize both your technical resources and business outcomes.

**Desired outcome:** You identify
 whether machine learning is truly the optimal solution for your
 business problem by comparing it against simpler alternatives. You
 make informed decisions about resource allocation, understanding the
 cost implications of ML adoption including data preparation,
 storage, training, hosting, and maintenance. You validate your
 approach using tools like Amazon SageMaker AI Autopilot and Amazon SageMaker AI Clarify to verify that ML provides measurable benefits
 over alternative solutions.

**Common anti-patterns:**

- Jumping directly to ML solutions without evaluating simpler
 alternatives.
- Underestimating the total cost of implementing ML, including
 data preparation and maintenance.
- Failing to establish a baseline for comparison with existing or
 rules-based approaches.
- Overlooking specialized resource constraints such as data
 scientist availability or model time-to-market.

**Benefits of establishing this best
 practice:**

- Avoids unnecessary complexity and cost in solution design.
- Optimizes resource allocation based on actual business value.
- Reduces risk of project failure due to inappropriate technology
 selection.
- Provides quantifiable metrics for evaluating ML solution
 effectiveness.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation guidance

When considering machine learning for a business problem, start by
 thoroughly evaluating whether ML is truly necessary. Many problems
 can be effectively solved with simpler rule-based approaches that
 may be less expensive to develop and maintain. Machine learning
 requires significant investment in data preparation, specialized
 hardware, and ongoing maintenance that must be justified by the
 business value it delivers.

Begin by clearly articulating your problem and determining if it
 requires the adaptive learning capabilities that ML provides.
 Consider if the problem involves complex patterns that rules can't
 simply capture, or if it requires continuous adaptation to
 changing conditions. For example, fraud detection in financial
 transactions might benefit from ML due to constantly evolving
 fraudulent behaviors, while simple inventory management might be
 better served by a rules-based system.

Evaluate costs associated with an ML solution, including data
 preparation, storage, compute resources for training, potential
 data labeling, model hosting, and ongoing maintenance. Compare
 these costs against the business value gained from using ML versus
 alternative approaches. Remember that specialized resources like
 data scientists might be your most constrained resource, making
 their time allocation a critical consideration.

### Implementation steps

1. **Articulate your problem
 clearly**. Define the business problem you're
 trying to solve, the desired outcomes, and how success will
 be measured. Be specific about what decisions need to be
 made and what data is available to support those decisions.
2. **Identify your data
 sources**. Evaluate what data you already have,
 what data you need to collect, and whether the quality and
 quantity are sufficient for ML applications. Consider
 [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) to catalog and manage your data assets.
3. **Calculate comprehensive cost
 implications**. Consider the aspects of
 implementing an ML solution:
Data preparation and engineering costsData storage requirements and associated costs using
 [Amazon S3](https://aws.amazon.com/s3/) or other storage servicesModel training expenses on various hardware options in
 [Amazon SageMaker AI Model Training](https://aws.amazon.com/sagemaker/ai/train/)Data labeling costs if supervised learning is requiredPotential retraining costs due to model drift or biasModel hosting and inference costsOngoing maintenance and monitoring expenses
4. **Establish a baseline
 solution**. Evaluate how the problem is currently
 being solved or how it could be solved with a simpler
 approach. If a rules-based solution exists, use it as a
 baseline for comparison. For basic ML approaches, consider
 pre-built solutions from
 [AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning) or
 [Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/).
5. **Build and evaluate an ML
 prototype**. Use
 [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) or
 [Amazon SageMaker AI Autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html) to quickly develop an ML model.
 Compare the performance metrics of this solution against
 your baseline approach, including accuracy, inference time,
 and total cost of operation.
6. **Analyze model
 explainability**. Use
 [Amazon SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-fairness-and-explainability.html) to understand how your ML model
 makes decisions and evaluate if these explanations align
 with business expectations and requirements.
7. **Make a data-driven
 decision**. Based on your comparative analysis,
 determine if the ML approach demonstrates sufficient
 improvement over simpler solutions to justify the
 investment. Consider both quantitative metrics and
 qualitative factors like flexibility and scalability.
8. **Use no-code ML for rapid
 validation**. Use
 [SageMaker AI
 Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html) with natural language support to quickly
 validate whether ML approaches provide value over simpler
 solutions, reducing the time and cost of initial feasibility
 assessment. Export Canvas-generated models and code to
 notebooks for further customization and integration into
 production workflows.
9. **Use AI-powered code generation for
 rapid prototyping**. Use AI-powered development
 tools like
 [Amazon Q Developer](https://aws.amazon.com/q/developer/) and
 [Kiro](https://kiro.ai/) to quickly
 generate ML prototype code, automate data preprocessing
 scripts, and accelerate the validation process for
 determining if ML is the right solution.
10. **Assess hybrid approaches**.
 Consider whether combining rules-based systems with ML or
 generative AI could provide the optimal balance of cost,
 performance, and explainability for your specific use case.

## Resources

**Related documents:**

- [Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)
- [SageMaker AI
 autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html)
- [Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/)
- [Machine
 Learning solutions in AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning)
- [Cost
 Optimization Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- [What
 is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [What
 is Amazon Bedrock?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost02-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
