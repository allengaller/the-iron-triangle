<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-6-3.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best Practice 6.3 – Protect the database and the application

Security vigilance is imperative at the database and application layers, as a
 malicious actor gaining access at even a read-only level could compromise the security of
 critical business data. In all cases, follow the standard SAP best practices for database
 access protection and application security. These apply to both on-premises and
 cloud-based installations, and there are guidelines for each supported underlying database
 for SAP systems.

**Suggestion 6.3.1 Follow SAP guidance on database security for your
 chosen database**

Refer to the following for appropriate guidelines:

| Database | Documentation |
| --- | --- |
| SAP HANA | AWS Documentation: [AWS SAP HANA Security](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-security.html)SAP Documentation: [SAP HANA Security Guide](https://help.sap.com/viewer/b3ee5778bc2e4a089d3299b82ec762a7/latest)SAP Documentation: [SAP HANA Administration Guide](http://help.sap.com/hana/SAP_HANA_Administration_Guide_en.pdf)SAP Note: [2159014 - FAQ: SAP HANA Security](https://launchpad.support.sap.com/#/notes/2159014) [Requires SAP Portal Access] |
| SAP ASE | SAP Documentation: [Security Administration in SAP ASE](https://help.sap.com/viewer/2705a3b1e3df4514ab089cfedf87750d/LATEST/en-US/a90b1f6cbc2b10148e32ab3706191414.html) |
| IBM Db2 | (Consult SAP or Vendor documentation for guidance) |
| Oracle | SAP Documentation: [SAP Database Guide - Oracle](https://help.sap.com/viewer/3ef1b95cacbf4f77a066797285371bb9/LATEST/en-US/4717849f6e8a21c3e10000000a114a6b.html) |
| Microsoft SQL Server | SAP Note: [3019299 - Security Audit Questions or Security Customization in NetWeaver and SQL Server systems](https://launchpad.support.sap.com/#/notes/3019299) [Requires SAP Portal Access] |
| SAP MaxDB | SAP Documentation: [SAP MaxDB Security Guide](https://help.sap.com/viewer/b255f72263a84a48b22eb41f4d381dda/latest) |

**Suggestion 6.3.2 – Follow SAP guidance on application
 security**

For SAP NetWeaver-based solutions, prescriptive guidance can be found in the SAP
 NetWeaver Security Guide.

- SAP Documentation: [ABAP Platform Security Guide](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4aaf6fd65e233893e10000000a42189c.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-6-3.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
