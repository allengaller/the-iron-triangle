<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-19-5.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best Practice 19.5 – Consider tiering options for live data

The primary driver of compute cost with SAP HANA is the amount of memory required.
 Therefore, the use of data offload and tiering options can drive the compute costs down.
 Although other databases might have tiering options, these have not been highlighted here.
 Consult with your database provider to understand the available options.

**Suggestion 19.5.1 – Evaluate dynamic tiering, extension nodes, and
 near-line storage (NLS) for SAP HANA OLAP-based workloads**

SAP HANA dynamic tiering is an optional add-on to the SAP HANA database to manage
 historical data. The purpose of dynamic tiering is to extend SAP HANA memory with a
 disk-centric columnar store (as opposed to SAP HANA’s in-memory store) for managing
 infrequently accessed data. Dynamic tiering can only be used for native SAP HANA use cases
 and not Business Warehouse (BW) on HANA or BW/4 HANA use cases

An SAP HANA extension node is a special purpose SAP HANA worker node that is
 specifically set up and reserved for storing warm data. An SAP HANA extension node allows
 you to store warm data for your SAP Business Warehouse (BW) or native SAP HANA analytics
 use cases. The total amount of data that can be stored on the SAP HANA extension node
 ranges from 1x to 2x of the total amount of memory of your extension node.

SAP BW Near-Line Storage (NLS) with SAP IQ allows you to store cold data outside of
 the BW on HANA or BW/4 HANA database. NLS moves the cold data from the HANA database to
 store on storage on the SAP IQ Server.

- AWS Documentation: [SAP Data
 Tiering](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-data-tiering.html)

**Suggestion 19.5.2 – Evaluate data aging and SAP HANA Native Storage
 Extension (NSE) for OLTP-based workloads**

Data aging helps free-up SAP HANA memory by storing less frequently accessed data in
 the disk area.

- AWS Documentation: [SAP Data
 Tiering](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-data-tiering.html)

**Suggestion 19.5.3 – Consider the use of data lakes for large volumes
 of analytical data**

When analyzing SAP and non-SAP data, S3-based data lakes provide a cost-effective
 option for data storage.

- AWS Documentation: [SAP OData
 connector for Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/sapodata.html)
- SAP on AWS Blog: [Building data lakes with SAP on AWS](https://aws.amazon.com/blogs/wsforsap/building-data-lakes-with-sap-on-aws/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-19-5.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
