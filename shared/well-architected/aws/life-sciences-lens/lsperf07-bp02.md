<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf07-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# LSPERF07-BP02 Design a compliant-by-design infrastructure

Design a computing architecture that addresses both performance and
 regulatory requirements through technical controls built directly
 into the infrastructure. Implement segregated computing environments
 with appropriate data controls between GxP and non-GxP workloads,
 deploy immutable infrastructure techniques that enhance both
 security and compliance, and use containerization with validated
 base images to accelerate deployment while maintaining regulatory
 integrity. Establish infrastructure templates with pre-validated
 components, automated audit trail generation, and built-in data
 integrity mechanisms that minimize the performance overhead
 typically associated with compliance retrofitting, while verifying
 that computational workloads execute in appropriately validated
 environments based on their regulatory classification.

**Desired outcome:** Create a
 computing infrastructure that balances performance and adherence
 through built-in controls, proper isolation, and automated
 validation, enabling efficient scientific work without regulatory
 burden.

**Level of risk exposed if this best practice
 is not established:** Medium

## Implementation guidance

Design distinct computing environments with appropriate boundaries
 for different regulatory contexts. Isolation allows tailored
 controls while avoiding regulatory requirements from limiting
 innovation in research-focused areas.

Use infrastructure as code and immutable deployment patterns that
 enhance both security and regulatory adherence. Immutable
 approaches block configuration drift while creating inherently
 more auditable and consistent environments.

Create a library of pre-validated infrastructure components and
 patterns. Pre-validated components accelerate deployment while
 maintaining compliance-aligned assurance through already-verified
 building blocks.

Integrate mechanisms directly into the infrastructure rather than
 as external processes. Embedded controls reduce overhead while
 blocking continuous compliance-aligned assurance without manual
 intervention.

Design infrastructure that maintains computational efficiency
 while meeting regulatory requirements. Performance-preserving
 approaches stop regulatory controls from becoming computational
 bottlenecks.

### Implementation steps

1. Design segregated domains with controlled data transfer
 between boundaries.
2. Implement immutable deployment with versioned infrastructure
 processes.
3. Build validated component library with pre-approved
 templates.
4. Deploy automated built-in audit trails and verification.
5. Optimize balance between controls and performance
 requirements.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf07-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
