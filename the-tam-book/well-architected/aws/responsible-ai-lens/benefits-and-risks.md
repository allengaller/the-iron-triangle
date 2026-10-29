<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/benefits-and-risks.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Benefits and risks

The benefits and risks focus area assists you to characterize the potential benefits
 and inherent risks of the use case, using only minimal assumptions
 about the AI solution given in the Use Case focus area. In general,
 the depth of analysis devoted to potential benefits and inherent
 risks should align with the breadth and complexity of the use case,
 and the potential scale of deployment. Iteration is expected.
 Additionally, since use cases are often defined by working backwards
 from desired benefits, risks may require more effort to explore than
 benefits.

Technically, benefits and risks can be assessed similarly. Both are
 based on the likelihood and impact of system interactions, where a
 system interaction typically involves a sequence of input and output
 pairs, which can be considered as *events* in the
 interaction. A helpful interaction has a positive impact on a
 stakeholder, while a harmful interaction has a negative impact on a
 stakeholder.

The result of an interaction can be the compounding effect of
 multiple events. To estimate benefits, you identify examples of
 helpful interactions, categorize the examples into benefits, and
 then use your knowledge of your business to estimate the value of
 each benefit. Assessing risk is trickier, because there is usually
 less information available about harmful interactions. As a result,
 you first identify categories of potential harmful interactions,
 qualitatively estimate the likelihood and impact severity of each
 harmful interaction category, and map the qualitative estimates to a
 risk level. In most cases, benefits and risks should be assessed for
 each stakeholder group.

Note that the risk posed by the AI system implementation when
 applied to the use case is referred to as residual risk. This is
 computed in [Monitoring](./monitoring.html), as part of the process of
 deciding whether the AI system is ready for release.

###### Focus areas

- [Characterize benefits](./raibr01.html)
- [Harmful events](./raibr02.html)
- [Assess risks](./raibr03.html)
- [Mitigate risks](./raibr04.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/benefits-and-risks.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
