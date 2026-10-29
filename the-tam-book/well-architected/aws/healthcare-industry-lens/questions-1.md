<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/questions-1.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Questions

Leverage thought leadership organizations to understand emerging
 trends, and use the capabilities of your customers’ systems.
 Many EHR and clinical systems have interoperability APIs. Older
 standards, like HL7 v2, are most prevalent. However, more modern
 standards can reduce the complexity of integration and enable
 new use-cases.

Older source systems may share data, but not support writes
 through interoperability APIs. Understand what interoperability
 is needed to enable your use-cases, and then how to achieve it
 in practice. Determine the importance of unidirectional transfer
 (sending data in only one direction between systems) or
 bidirectional transfer (exchanging data between two systems), as
 they will have different requirements and use cases. Custom
 integration work, or support from AWS Partner Network (APN)
 partners or ISVs, may be required to achieve bidirectional
 interoperability.

Work with your customer to understand what vocabularies they
 employ and how you can link to standards. Where possible,
 leverage modern standards that provide semantic
 interoperability, such as Consolidated-Clinical Document
 Architecture (C-CDA). AI-based services, like
 [Amazon Comprehend Medical](https://aws.amazon.com/comprehend/medical/), can link concepts to standard
 ontologies in cases that deterministic linking is not possible.

Use end-to-end encryption of health data exchanged over the
 network. Older standards, like the Minimum Lower Layer Protocol
 (MLLP) used with HL7 v2, may not natively support TLS. In such
 cases, protect data with a VPN tunnel or additional encryption
 solution. For MLLP interfaces that support TLS, use certificates
 for authentication and encryption. Security groups can be used
 to protect integration endpoints to only allow traffic from
 specific IP addresses. Within AWS, simplify encrypted
 communication between instances by using Amazon EC2 instances that
 support offloading encryption to Nitro System hardware.

Restrict access to integration endpoints to allow-listed IP
 addresses and through secure VPN tunnels when possible.
 Employ
 [AWS WAF](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html) to protect RESTful APIs, and the suite of
 [AWS security
 services](https://aws.amazon.com/security/) to add additional security measures.

Some use-cases require large historical datasets, like training
 machine learning models. Exchanging large datasets may place an
 unacceptable load on the integration APIs of source systems.
 Quantify how much data you must exchange across the phases of an
 interoperability project. If necessary, perform an initial
 exchange of records in bulk format (for example, by using
 [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/)), and then use on-going real-time
 integration methods for updates.

Use Network Load Balancer to route HL7 v2 traffic to your
 integration endpoints. Network Load Balancer can also monitor
 the health of your integration endpoints and only route traffic
 to healthy targets. Deploy your integration services in multiple
 Availability Zones and enable multiple Availability Zones for
 the load balancer to increase fault tolerance. APIs hosted by
 API Gateway are automatically resilient by using multiple
 Availability Zones in the deployed Region.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/questions-1.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
