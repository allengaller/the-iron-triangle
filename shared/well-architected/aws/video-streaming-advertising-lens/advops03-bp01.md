<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops03-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVOPS03-BP01 Create runbooks for the most common operational events and incidents that can impact your advertising workload

Develop structured procedures to manage operational events and
 incidents in your advertising workloads. Runbooks provide
 step-by-step procedures for well-understood, routine operations,
 while playbooks guide your response to incidents with less
 predictable outcomes. These documented procedures assist teams
 to respond consistently and effectively, reducing human error
 and improving operational resilience.

## Implementation guidance

1. Use automation for predictable operational responses:
Implement auto scaling and load balancing using AWS services to handle common traffic patterns:
Configure Amazon EC2 Auto Scaling groups with appropriate
 scaling policies based on advertising traffic patterns.Set up Elastic Load Balancing to distribute traffic across
 healthy instances.Implement predictive scaling based on historical data for
 cyclical advertising campaigns.Configure scheduled scaling for planned high-traffic
 events like product launches or holiday promotions.For scenarios where auto scaling may not be sufficient:
Create runbooks for requesting additional EC2
 capacity through ODCRs before anticipated
 high-traffic events.Implement AWS Systems Manager automation documents
 to execute common scaling procedures.Use AWS Auto Scaling for predictive scaling based
 on historical data patterns.Configure CloudWatch alarms to trigger automated
 responses for common capacity issues.
2. Create purpose-built runbooks and playbooks for different
 advertising scenarios:
Infrastructure capacity runbooks:
Document procedures for submitting on-demand
 capacity requests (ODCRs) for anticipated
 high-traffic eventsCreate step-by-step guides for scaling resources
 up or down based on traffic patternsEstablish processes for capacity planning before
 major advertising campaignsDefine monitoring thresholds that trigger capacity
 management proceduresAd fraud incident playbooks:
Document investigation procedures for detected
 fraud patterns (bot traffic, click fraud,
 impression fraud)Establish clear escalation paths for high-impact
 fraud incidents with defined severity levelsCreate detailed workflows for fraud investigation
 and mitigation, including evidence collectionDefine recovery procedures to restore normal
 operations after fraud mitigationDocument procedures for `ads.txt` and `sellers.json`
 verification and maintenanceImplement AWS Marketplace solutions like HUMAN for
 automated fraud detection and preventionCreate operational workflows for real-time fraud
 detection using Amazon SageMaker AI ML modelsBrand safety incident playbooks:
Document procedures for content moderation
 escalations and violationsEstablish workflows for emergency ad creative
 approval and rejectionCreate processes for brand safety incident
 response, including stakeholder communicationDefine procedures for implementing emergency
 blocking rules in ad serving systemsImplement content moderation workflows using
 Amazon Rekognition for image/video analysis and
 Amazon Comprehend for text analysisCreate escalation procedures for high-risk content
 identification with automated alerts via Amazon
 EventBridgeDocument processes for regular updates to content
 moderation models in SageMaker AIMeasurement anomaly runbooks:
Document step-by-step procedures for investigating
 common measurement discrepanciesEstablish workflows for cross- data reconciliation
 and validationCreate processes for measurement system
 recalibration and data correctionDefine verification steps to confirm resolution of
 measurement issuesAI measurement system playbooks:
Document operational procedures for AI model
 training, validation, and deploymentCreate monitoring workflows for detecting model
 drift and performance degradationEstablish human oversight processes for AI-based
 measurement systemsDocument recovery procedures for AI system
 failuresImplement continuous improvement workflows using
 AWS Step Functions to orchestrate model retrainingCreate operational procedures for managing model
 versions and deployments
3. Implement continuous improvement for runbooks and playbooks:
Review and update documentation after each incident or
 significant operational eventConduct regular simulation exercises to validate
 playbook effectivenessIncorporate lessons learned into revised proceduresTrack key metrics on playbook execution efficiency and
 outcome effectiveness

## Key AWS services

- Amazon EC2 Auto Scaling
- Elastic Load Balancing
- AWS Systems Manager
- Amazon CloudWatch
- AWS Auto Scaling
- Amazon SageMaker AI
- Amazon Rekognition
- Amazon Comprehend
- AWS Lambda
- AWS Step Functions
- Amazon EventBridge
- Amazon Route 53
- AWS Marketplace solutions (like HUMAN)

## Resources

- [OPS07-BP03 Use runbooks to perform procedures](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_runbooks.html)
- [Use playbooks](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_playbooks.html)
- [AWS Marketplace: HUMAN Fraud Protection Solutions](https://aws.amazon.com/marketplace/seller-profile?id=22586a6c-27be-426c-b655-bb9783786286)
- [How HUMAN Advertising Intelligence Solutions Help Protect Against Ad Fraud in the Ad Tech Industry](https://aws.amazon.com/blogs/apn/how-human-advertising-intelligence-solutions-help-protect-against-ad-fraud-in-the-ad-tech-industry/)
- [Content Moderation Using Machine Learning on AWS](https://aws.amazon.com/blogs/machine-learning/utilize-aws-ai-services-to-automate-content-moderation-and-compliance/)
- [Guidance for Content Moderation on AWS](https://aws.amazon.com/solutions/guidance/content-moderation-on-aws/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops03-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
