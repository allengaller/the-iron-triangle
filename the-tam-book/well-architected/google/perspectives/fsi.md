<!-- source: https://docs.cloud.google.com/architecture/framework/perspectives/fsi -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Well-Architected Framework: Financial services (FS) perspective

This document in the
[Google Cloud Well-Architected Framework](/architecture/framework) 
describes principles and recommendations to help you to design, build, and
manage financial services (FS) applications in Google Cloud that meet
your operational, security, reliability, cost, and performance goals.

The target audience for this document includes decision makers, architects,
administrators, developers, and operators who design, build, deploy, and
maintain FS workloads in Google Cloud. Examples of FS organizations that
could benefit from this guidance include banks, payment infrastructure players,
insurance providers, and capital market operators.

FS organizations have specific considerations, particularly for architecture
and resilience. These considerations are primarily driven by regulatory, risk,
and performance requirements. This document provides high-level guidance that's
based on design considerations that we've observed across a wide range of FS
customers globally. Whether your workloads are fully in the cloud or
transitioning to hybrid or multi-cloud deployments, the guidance in this
document helps you design workloads on Google Cloud to meet your
regulatory requirements and diverse risk perspectives. The guidance might not
address the unique challenges of every organization. It provides a foundation
that addresses many of the primary regulatory requirements of FS organizations.

A primary challenge in designing cloud workloads involves aligning cloud
deployments with on-premises environments, especially when you aim for
consistent approaches to security, reliability, and resilience. Cloud services
create opportunities to fundamentally rethink your architecture in order to
reduce management overhead, optimize cost, enhance security, and improve
reliability and resilience.

The following pages describe principles and recommendations that are specific to
FS workloads for each pillar of the Well-Architected Framework:

- [FS perspective: Operational excellence](/architecture/framework/perspectives/fsi/operational-excellence)
- [FS perspective: Security](/architecture/framework/perspectives/fsi/security)
- [FS perspective: Reliability](/architecture/framework/perspectives/fsi/reliability)
- [FS perspective: Cost optimization](/architecture/framework/perspectives/fsi/cost-optimization)
- [FS perspective: Performance optimization](/architecture/framework/perspectives/fsi/performance-optimization)

## Contributors

Authors:
 [Gino Pelliccia](https://www.linkedin.com/in/gino-pelliccia-13637025) | Principal Architect[Alex Stepney](https://www.linkedin.com/in/alexstepney/) | Lead Principal Architect[Phil Bryan](https://www.linkedin.com/in/philbry) | EMEA FSI Lead Principal Architect[Stathis Onasoglou](https://www.linkedin.com/in/stathisonasoglou) | EMEA FSI Principal Architect[Sam Moss](https://www.linkedin.com/in/samuel-moss-643780105) | EMEA FinOps Professional Services Lead

Other contributors:
 [Daniel Lees](https://www.linkedin.com/in/daniellees) | Cloud Security Architect[Danielle Fisla](https://www.linkedin.com/in/danielle-fisla-7132192) | US FS Portfolio Lead, PSO[Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist[Henry Cheng](https://www.linkedin.com/in/tohenryc) | Principal Architect[John Bacon](https://www.linkedin.com/in/johnbac/) | Partner Solutions Architect[Jose Andrade](https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist[Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer[Laura Hyatt](https://www.linkedin.com/in/laura-hyatt) | Customer Engineer, FSI[Michael Yang](https://www.linkedin.com/in/chengxiyang) | Industry Solutions AI Consulting Lead, FSI[Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist[Omar Saenz](https://www.linkedin.com/in/omarsaenz) | EMEA Partner Engineer, Security[Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework[Steve McGhee](https://www.linkedin.com/in/stevemcghee) | Reliability Advocate[Tarun Sharma](https://www.linkedin.com/in/tarun27in) | Principal ArchitectYuriy Babenko | Customer Engineer, FSI

---

> 原页面：https://docs.cloud.google.com/architecture/framework/perspectives/fsi（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
