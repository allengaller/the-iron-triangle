<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Security foundations

Game studios require a unique security approach that protects both development
 environments and live player services. A robust AWS security strategy for game studios
 requires three interconnected components: a multi-account structure, strong authentication,
 and a clear authorization strategy using IAM policies. A multi-account AWS structure
 enables studios to separate different game projects, development stages, and tool
 environments. This gives studios more granular control for things like access to specific
 environments or services. Enabling strong authentication verifies team members can securely
 access development resources whether working in-studio or remotely, while maintaining strict
 controls over source code, game builds, and proprietary tools. Studios should also have a
 clear authorization strategy for granting permissions using the principle of least privilege
 with IAM permissions and roles. Use IAM roles to assign permissions between different
 development team roles, such as giving dev teams access to low-level AWS services while
 restricting artists and designers to specific asset management and build systems. This
 specialized approach verifies game studios can protect their intellectual property, maintain
 efficient development workflows, and scale their teams securely while giving developers the
 appropriate access to iterate quickly on their projects.

###### Best practices

- [GAMESEC01-BP01 Use roles and federated access, rather than the account root user, to perform actions on your AWS environment](./gamesec01-bp01-use-roles-and-federated-access-rather-than-the-account-root-user-to-perform-actions-on-your-aws-environment.html)
- [GAMESEC01-BP02 Use AWS Control Tower to quickly set up a multi-account environment on AWS](./gamesec01-bp02-use-aws-control-tower-to-quickly-set-up-a-multi-account-environment-on-aws.html)
- [GAMESEC01-BP03 Use least privilege role policies that are tailored to specific job functions](./gamesec01-bp03-use-least-privilege-role-policies-that-are-tailored-to-specific-job-functions.html)
- [GAMESEC01-BP04 Use roles and federated access policies together with account level access policies to grant access to your AWS resources](./gamesec01-bp04.html)
- [GAMESEC01-BP05 Use a central identity provider](./gamesec01-bp05.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
