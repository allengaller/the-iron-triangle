<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-iam.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Identity and access management

Identity and access management are key parts of an information
 security program, ensuring that only authorized and authenticated
 users and components are able to access your resources, and only
 in a manner that you intend. For example, you should define
 principals (that is, accounts, users, roles, and services that can
 perform actions in your account), build out policies aligned
 with these principals, and implement strong credential management.
 These privilege-management elements form the core of
 authentication and authorization.

In AWS, privilege management is primarily supported by the AWS
 Identity and Access Management (IAM) service, which allows you
 to control user and programmatic access to AWS services and
 resources. You should apply granular policies, which assign permissions to a user, group, role, or resource. You also
 have the ability to require strong password practices, such as
 complexity level, avoiding re-use, and enforcing multi-factor
 authentication (MFA). You can use federation with your existing
 directory service. For workloads that require systems to have
 access to AWS, IAM allows for secure access through roles, instance
 profiles, identity federation, and temporary credentials.

The following questions focus on these considerations for
 security.

There are two types of identities you need to manage when approaching
 operating secure AWS workloads. Understanding the type of identity you need to
 manage and grant access helps you verify the right identities have access to the
 right resources under the right conditions.

Human Identities: Your administrators, developers, operators, and end users
 require an identity to access your AWS environments and applications. These are
 members of your organization, or external users with whom you collaborate, and who
 interact with your AWS resources via a web browser, client application, or
 interactive command line tools.

Machine Identities: Your service applications, operational tools, and
 workloads require an identity to make requests to AWS services, for example, to
 read data. These identities include machines running in your AWS environment
 such as Amazon EC2 instances or AWS Lambda functions. You may also manage machine
 identities for external parties who need access. Additionally, you may also have
 machines outside of AWS that need access to your AWS environment.

Credentials must not be shared between any user or system. User access should be granted
 using a least-privilege approach with best practices including password requirements and MFA
 enforced. Programmatic access, including API calls to AWS services, should be performed
 using temporary and limited-privilege credentials, such as those issued by the
 AWS Security Token Service.

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access? | To | By |
| --- | --- | --- |
| IAM | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use. For the AWS CLI, see [Login for AWS local development](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html) in the *AWS Command Line Interface User Guide*.For AWS SDKs, see [Login for AWS local development](https://docs.aws.amazon.com/sdkref/latest/guide/access-login.html) in the *AWS SDKs and Tools Reference Guide*. |
| Workforce identity (Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use. For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) in the *AWS Command Line Interface User Guide*.For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*. |
| IAM | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions in [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the *IAM User Guide*. |
| IAM | (Not recommended)Use long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use. For the AWS CLI, see [Authenticating using IAM user credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html) in the *AWS Command Line Interface User Guide*.For AWS SDKs and tools, see [Authenticate using long-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html) in the *AWS SDKs and Tools Reference Guide*.For AWS APIs, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*. |

AWS provides resources that can help you with identity and access management. To help
 learn best practices, explore our hands-on labs on [managing credentials & authentication](https://wellarchitectedlabs.com/Security/Quest_Managing_Credentials_and_Authentication/README.html?ref=wellarchitected-wp), [controlling human access](https://wellarchitectedlabs.com/Security/Quest_Control_Human_Access/README.html?ref=wellarchitected-wp), and [controlling programmatic access](https://wellarchitectedlabs.com/Security/Quest_Control_Programmatic_Access/README.html?ref=wellarchitected-wp).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-iam.html（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
