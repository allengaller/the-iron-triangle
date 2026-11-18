<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-7-1.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best Practice 7.1 – Understand your SAP user categories and access mechanisms

The types of users accessing your SAP system will determine the security controls you
 need to apply. By examining each use case, you can develop a strategy. This should include
 how you manage identities, authentication, tooling and mechanisms to support those
 requirements.

**Suggestion 7.1.1 Understand data access permissions and permitted
 actions**

SAP systems often contain highly sensitive business data. As you define your user
 types, understand the data access permissions. (For example, an administrative database user
 does not have the fine-grained controls of an application user, and therefore may be more
 critical.) Also refer to [Security]: [Best Practice 5.2 -
 Classify the data within your SAP workloads](./best-practice-5-2.html).

Consider the following questions in relation to your SAP system access:

- Do the actions taken by an administrative or service user need to be traceable to
 a uniquely identifiable individual?
- At which layer of the application will the access be granted?
- Can you restrict access to a subset of functionality via permissions?
- Can you restrict access to a subset of functionality via other controls, for
 example exposing only certain services?
- Is there a requirement to audit the actions taken?

**Suggestion 7.1.2 – Understand the network and/or location from which
 users will access the SAP systems**

Network and/or location often contributes to the security risk profile and may
 determine whether the user is considered trusted or untrusted. Typically, this is coupled
 with the controls to prevent unauthorized access (refer to [Best Practice 6.1 - Ensure that security and auditing are built into the SAP network
 design](./best-practice-6-1.html)).

This can influence your design. For example, an untrusted internet user or device may
 require additional factors of authentication to access your SAP workload, when compared
 with a trusted user from your corporate network.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-7-1.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
