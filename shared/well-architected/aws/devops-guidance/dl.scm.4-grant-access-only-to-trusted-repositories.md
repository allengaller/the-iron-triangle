<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.4-grant-access-only-to-trusted-repositories.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# [DL.SCM.4] Grant access only to trusted repositories

**Category:** FOUNDATIONAL

To maintain the security, integrity, and quality of your software, restrict the usage
 of untrusted source code and artifact repositories. Untrusted repositories present risks,
 including potentially introducing vulnerabilities into your software and leaking sensitive
 code or information. As a safer alternative, only use trusted repositories that offer
 secure, vetted libraries, and dependencies.

Implement policies that control where developers can publish
 code, to prevent accidental exposure or internal threats. This
 should apply to both artifact and source code repositories
 across the organization. Protect against internal threat
 actors or inadvertently sharing code to public or untrusted
 git repositories by limiting the allowed repositories that
 developers can publish code to. Hosting your own repositories
 might be advantageous depending on your needs, enabling
 complete control over available code. Methods such as
 pre-commit hooks for git repositories can be used to enforce
 these rules effectively.

By enforcing usage of trusted repositories, you ensure that
 only secure, vetted code components and artifacts are used,
 enhancing software lifecycle stability and security. It also
 minimizes the risk of sensitive information being leaked into
 untrusted repositories.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.4-grant-access-only-to-trusted-repositories.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
