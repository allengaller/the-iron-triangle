<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel04-bp02.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# GENREL04-BP02 Implement a model catalog

Model catalogs store and manage model versions. They act as a
 reliable store for models which may need to be deployed or rolled
 back at any time. They also facilitate decoupled deployment
 automation.

**Desired outcome:** When
 implemented, this best practice improves the reliability of your
 generative AI workload by helping to make sure the deployed model is
 the appropriate model for the given use case.

**Benefits of establishing this best
 practice:**
[Manage
 change through automation](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Implementing a model catalog
 helps to automate the process of deploying and rolling back model
 versions.

**Level of risk exposed if this best practice
 is not established:** Low

## Implementation guidance

Model catalogs provide a centralized location to review
 models, model versions, and model cards. Traditionally, model
 catalogs are meant to store model artifacts developed by
 customers. Foundation models are rarely developed from
 scratch, and as a result, foundation model catalogs should
 maintain first-party models, third-party models, and custom
 models developed from third-party models.

Consider implementing a model catalog for foundation models
 that records and tracks model access, model versions, and
 model card information. Maintain a model catalog in your
 environment to track available models. Model catalogs should
 provide a central location for model management, particularly
 if there is a need to roll back to a particular model or model
 version.

AI policy documents should provide clear details regarding the
 usage, maintenance, and updating of the model catalog. The AI
 policy document is intended to be the central authority for
 operational questions pertaining to AI workloads and
 supporting infrastructure. Keep this document up to date with
 the appropriate materials necessary to scale the usage of the
 model catalog throughout the organization.

### Implementation steps

1. Set up catalog structure:
Create model classification system (by type, purpose, and provider)Define model metadata schemaEstablish versioning conventionsDesign access control framework
2. Configure model tracking:
Record model lineage and dependenciesTrack model versions and updatesDocument model customizationsMaintain performance benchmarks
3. Implement model cards:
Define required model informationDocument model capabilities and limitationsRecord training data characteristicsSpecify intended use cases and constraintsInclude ethical considerations and biases
4. Establish model governance:
Create model approval workflowsDefine deployment proceduresSet up model monitoringImplement security controlsTrack model usage and access
5. Create maintenance procedures:
Define model update processEstablish deprecation policiesCreate archival proceduresSet up backup and recovery
6. Implement validation framework:
Create model testing proceduresDefine acceptance criteriaSet up performance benchmarkingEstablish quality gates

## Resources

**Related best practices:**

- [REL04-BP02](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_loosely_coupled_system.html)
- [REL07-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_autoscale_adapt.html)

**Related documents:**

- [Amazon Bedrock API Reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)
- [Amazon Bedrock Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html)
- [Find
 serverless models with the Amazon Bedrock model catalog](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/model-catalog.html)
- [Bring
 your own endpoint](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-bring-your-own-endpoint.html)

**Related examples:**

- [Amazon Bedrock Marketplace: Access over 100 foundation models in one
 place](https://aws.amazon.com/blogs/aws/amazon-bedrock-marketplace-access-over-100-foundation-models-in-one-place/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel04-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
