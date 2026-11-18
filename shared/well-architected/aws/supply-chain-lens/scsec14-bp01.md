<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec14-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# SCSEC14-BP01 Implement comprehensive code and dependency integrity validation

Maintaining the integrity of application code and dependencies is
 critical for helping to prevent supply chain attacks that target
 software components. Organizations should implement code signing
 to verify authenticity and help prevent tampering with application
 components. Automated scanning of dependencies for known
 vulnerabilities should be integrated into development workflows to
 identify security issues before deployment. Establishing trusted
 repositories for approved components and implementing integrity
 verification during build and deployment processes creates
 multiple layers of protection against compromised software in the
 supply chain.

**Desired outcome:** Verified and
 secure code and dependencies throughout the supply chain
 application lifecycle.

**Benefits of establishing this best
 practice:** Reduced risk of compromised applications and
 improved overall security of the supply chain environment.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

Use code signing to verify the authenticity and integrity of
 code, involving digitally signing the code with a cryptographic
 key to validate it has not been tampered with. Use tools like
 AWS CodeArtifact to manage and securely store dependencies,
 making sure only approved and verified dependencies are used in
 applications, while regularly scanning dependencies for known
 vulnerabilities using automated security scanning tools.

### Implementation steps

1. Implement code signing processes to digitally sign all
 application code and components, supporting authenticity
 and helping to prevent tampering throughout the
 development and deployment lifecycle.
2. Establish secure dependency management using trusted
 repositories and automated scanning tools to identify and
 remediate vulnerabilities in third-party components before
 deployment.
3. Implement strict access controls and audit logs in source
 control systems to track changes and make sure only
 authorized personnel can modify code and dependencies.
4. Integrate automated security checks into CI/CD pipelines
 to validate code and dependency integrity during build and
 deployment processes, helping to prevent compromised
 components from reaching production.
5. Deploy runtime protection measures and monitoring tools to
 detect and respond to unauthorized changes or suspicious
 activities in real-time during application execution.
6. Establish comprehensive monitoring and logging systems to
 maintain visibility into code and dependency integrity
 across the entire application lifecycle and supply chain
 environment.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec14-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
