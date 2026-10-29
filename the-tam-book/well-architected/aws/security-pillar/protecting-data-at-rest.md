<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-data-at-rest.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Protecting data at rest

*Data at rest* represents any data that you persist in non-volatile
 storage for any duration in your workload. This includes block storage, object storage,
 databases, archives, IoT devices, and any other storage medium on which data is persisted.
 Protecting your data at rest reduces the risk of unauthorized access, when encryption and
 appropriate access controls are implemented.

Encryption and tokenization are two important but distinct data protection schemes.

*Tokenization* is a process that allows you to define a token to
 represent an otherwise sensitive piece of information (for example, a token to represent a
 customer’s credit card number). A token must be meaningless on its own, and must not be
 derived from the data it is tokenizing–therefore, a cryptographic digest is not usable as a
 token. By carefully planning your tokenization approach, you can provide additional protection
 for your content, and you can ensure that you meet your compliance requirements. For example,
 you can reduce the compliance scope of a credit card processing system if you leverage a token
 instead of a credit card number.

*Encryption* is a way of transforming content in a manner that makes it
 unreadable without a secret key necessary to decrypt the content back into plaintext. Both
 tokenization and encryption can be used to secure and protect information as appropriate.
 Further, masking is a technique that allows part of a piece of data to be redacted to a point
 where the remaining data is not considered sensitive. For example, PCI-DSS allows the last
 four digits of a card number to be retained outside the compliance scope boundary for
 indexing.

**Audit the use of encryption keys:** Ensure that you
 understand and audit the use of encryption keys to validate that the access control mechanisms
 on the keys are appropriately implemented. For example, any AWS service using an AWS KMS key
 logs each use in AWS CloudTrail. You can then query AWS CloudTrail, by using a tool such as Amazon CloudWatch Logs
 Insights, to ensure that all uses of your keys are valid.

###### Best practices

- [SEC08-BP01 Implement secure key management](./sec_protect_data_rest_key_mgmt.html)
- [SEC08-BP02 Enforce encryption at rest](./sec_protect_data_rest_encrypt.html)
- [SEC08-BP03 Automate data at rest protection](./sec_protect_data_rest_automate_protection.html)
- [SEC08-BP04 Enforce access control](./sec_protect_data_rest_access_control.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-data-at-rest.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
