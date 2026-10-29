<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-13-3.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best Practice 13.3 – Select architectures which allow for independent scaling of systems or components

SAP systems and components should have the flexibility to scale without being
 constrained. This might be accomplished within the allocated hardware or by using
 horizontal scaling of some components. Consider which architectures allow for this scaling
 and evaluate any associated trade-offs.

**Suggestion 13.3.1 – Consider cross-system or cross-component
 performance impact**

Isolate individual systems or components (for example, Central Services, application
 servers, and database) to avoid negative performance impact between components. Deploying
 multiple smaller instance sizes can provide options for instance reuse, workload-based
 scaling, and capacity on-demand. There are exceptions when trying to optimize the use of
 resources for cost reasons. Refer to the cost pillar for more details.

**Suggestion 13.3.2 – Consider capacity flexibility for peak
 performance**

By selecting architectures which allow for scaling of components, such as the
 application servers, it will be possible to adapt your capacity to match with performance
 requirements. This allows your SAP systems to scale for exceptional demand including month
 end processing or seasonal peaks.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-13-3.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
