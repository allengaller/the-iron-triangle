<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec06-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCSEC06 BP02 Strengthen SAML federation to reduce security risks

To help prevent an opportunity for SAML assertions to be misused
 when using Certificate Based Authentication by incorrectly
 associating with Active Directory user security objects, strong
 mapping should be used.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

Use strong mapping between SAML IdP and Active Directory. You
 can use certificate-based authentication (CBA) with Amazon WorkSpaces, which you can use to remove the user password
 prompt when using a SAML 2.0 identity provider. To establish a
 strong mapping between Active Directory users and SAML
 assertions, ObjectSid must be configured within the SAML
 assertion. CBA will fail if the attribute does not match the
 Active Directory security identifier (SID) for the user in the
 `SAML_Subject NameID`. For more detail, see
 [Certificate-based
 authentication](https://docs.aws.amazon.com/workspaces/latest/adminguide/certificate-based-authentication.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec06-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
