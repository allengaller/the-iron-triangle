<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/change-management.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Change management

HPC workloads often consist of software packages with complex
 dependencies. Managing software and dependencies, with specific
 versioning requirements, across many users, can be complex.
 Consider the following best practices when building out your
 architecture.

## HPCREL02-BP01 Install software packages in a shared location to simplify multi-user, multi-resource software requirements management

Installing software packages on shared storage, such as Amazon Elastic File System (EFS), allows users
 across compute environments and clusters access the same versioned set of packages.
 Dependencies can also be installed using a custom AMI, or using a post-install script, such
 as configured with [AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/custom-bootstrap-actions-v3.html).

### Implementation guidance

Install software in shared location for multi-user or multi-resource environments.
 Single resource environments can use a custom AMI or separate Amazon Elastic Block Store (Amazon EBS) volume,
 and multi-resource environments can use shared storage, such as Amazon Elastic File System (Amazon EFS).

## HPCREL02-BP02 Use package managers to simplify software dependency management when possible

Managing HPC applications can potentially be simplified with
 package managers, such as Spack, SBGrid, and EasyBuild. AWS
 hosts a Spack binary cache for fast installation of commonly
 used HPC packages and applications. Leveraging a package manager
 simplifies dependency management for system admins while
 providing exact versioning per user requirements.

### Implementation guidance

Consider a package manager to simplify software dependencies.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/change-management.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
