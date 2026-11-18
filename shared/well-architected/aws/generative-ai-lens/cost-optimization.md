<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/cost-optimization.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Cost optimization

The cost optimization best practices introduced in this paper are
 represented by at least of one of the following principles:

- **Optimize model and inference
 selection:** Choose foundation models and inference
 approaches that align with your actual performance requirements
 and avoid over-provisioning. By carefully evaluating model size,
 accuracy needs, and inference paradigms, you can reduce
 operational costs while maintaining necessary quality levels.
 This principle helps you avoid paying for excess capacity or
 capabilities that don't deliver proportional business value.
- **Control resource consumption
 parameters:** Implement strict controls over the
 variables that directly affect usage costs in generative AI
 systems. By managing prompt lengths, response sizes, and vector
 dimensions, you can minimize token usage and storage
 requirements while meeting the required functionality. This
 approach allows you to maintain cost efficiency at the
 operational level while preserving essential system
 capabilities.
- **Design workflow boundaries:**
 Establish clear limits and exit conditions for generative AI
 processes to avoid runaway resource consumption. By implementing
 stopping conditions and monitoring execution patterns, you can
 avoid scenarios where workflows consume excessive resources or
 continue beyond their useful purpose. This helps you predict
 cost and avoid unexpected budget overruns.

###### Focus areas

- [Model selection and cost optimization](./gencost01.html)
- [Generative AI pricing model](./gencost02.html)
- [Cost-aware prompting](./gencost03.html)
- [Cost-informed vector stores](./gencost04.html)
- [Cost-informed agents](./gencost05.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/cost-optimization.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
