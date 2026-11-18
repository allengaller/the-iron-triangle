<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dsperf02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Software dependency validation

Third-party software components introduce sovereignty risks that
 standard security scanning doesn't detect. Export controls can block
 the delivery of updates. Copyleft licensing can create unintended
 source-code disclosure obligations. A critical dependency maintained
 by contributors in a single jurisdiction becomes a continuity risk
 if that jurisdiction faces trade restrictions. These concerns
 require evaluation criteria that go beyond vulnerability scanning to
 assess sovereignty-specific risks before components are deployed.

This capability covers the validation of third-party software
 components (open source libraries, commercial SDKs, and proprietary
 middleware) against sovereignty-specific criteria including export
 control, licensing, maintainer jurisdiction, and supply chain
 continuity.

## Capability intent

- Third-party components are evaluated against
 sovereignty-specific criteria (export controls, licensing
 obligations, maintainer jurisdiction, update availability)
 before they enter the approved dependency list.
- The software bill of materials stays current and shows which
 third-party components are deployed and what risks they carry.
- Components subject to export controls or restrictive licensing
 are identified and managed with explicit acceptance of the
 constraints they impose.
- Supply chain continuity risk is assessed for critical
 dependencies, with mitigation plans for components where
 update availability depends on a single jurisdiction.
- Validation is integrated into the development lifecycle so
 that new dependencies are assessed before they reach
 production, not discovered during compliance reviews.

## Common issues to watch for

- Vulnerability scanning treated as sufficient dependency
 governance, which overlooks sovereignty-specific risks that
 scanners do not evaluate, such as export controls, licensing
 obligations, and maintainer jurisdiction.
- Software bill of materials that captures direct dependencies
 but not transitive ones, so sovereignty risks stay hidden in
 the dependency tree.
- Export control assessments conducted at initial adoption but
 not revisited when geopolitical conditions or component
 classification changes.
- Critical dependencies with single-jurisdiction maintainers
 identified as a risk but without mitigation plans (forking,
 alternative sourcing, or contribution) that would maintain
 update availability if that jurisdiction becomes restricted.
- Dependency validation that exists as a policy but isn't
 enforced in pipelines, so unapproved components reach
 production through developer workstations or alternative
 deployment paths.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/digital-sovereignty-lens/dsperf02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
