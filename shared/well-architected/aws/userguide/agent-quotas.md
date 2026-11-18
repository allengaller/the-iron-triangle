<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-quotas.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# AWS Well-Architected Agent Quotas and limits

AWS Well-Architected Agent is in preview release and is subject to change.


## Access and entitlements

AWS WA Agent access and entitlements depend on your AWS Support plan tier.

| Support tier | Access | Max profiles | Max applications per profile |
| --- | --- | --- | --- |
| Developer | No | — | — |
| Business | No | — | — |
| Business+ | Yes | 2 | 7 |
| Enterprise On-Ramp | Yes | 10 | 30 |
| Enterprise Support | Yes | 10 | 30 |
| Unified Operations | Yes | 10 | 30 |

## Quotas and limits

| Resource | Default limit | Notes |
| --- | --- | --- |
| Accounts per profile | 100 | Maximum AWS accounts that a single profile can analyze. |
| Goals per profile | 10 | Maximum active business goals per profile. |
| Profile hosting Regions | 3 | Profiles can be hosted in US East (N. Virginia), US East (Ohio), or US West (Oregon). |
| Scannable Regions | All commercial | AWS WA Agent can scan resources in any commercial AWS Region, regardless of where the profile is hosted. |
| Recommendations per generation run | 30 | Maximum recommendations produced per scheduled or manual generation run. There is no limit on total stored recommendations. Future runs can add new recommendations. |
| Architecture reviews per day | 5 | Maximum architecture review generations per day, per profile. Reviews can be run consecutively without cooldown while quota remains. |
| Scheduled recommendation generation cooldown | 7 days (1 week) | Minimum time between scheduled recommendation generation runs for the same profile. |
| Maximum .zip file upload size | 25 MB | Maximum compressed size of an uploaded .zip file for architecture reviews. |
| Maximum Amazon S3 folder size | 100 MB | Maximum total size of an Amazon S3 folder referenced for architecture reviews. |
| Maximum individual file size (Amazon S3 folder) | 1 MB | Maximum size of each individual file in an Amazon S3 folder referenced for architecture reviews. |

## Unsupported resource types

AWS WA Agent does not analyze the CloudFormation resource types in the following table. If your application
 uses these resource types, AWS WA Agent does not retrieve their configuration data and does not include
 them in resource-level recommendations.

For more information about specifying the services and resource types your application uses,
 see [Updating application context](./agent-update-app-context.html).

| Service | Unsupported resource types |
| --- | --- |
| `AWS::ACMPCA` | `AWS::ACMPCA::Certificate``AWS::ACMPCA::CertificateAuthorityActivation``AWS::ACMPCA::Permission` |
| `AWS::AmplifyUIBuilder` | `AWS::AmplifyUIBuilder::Component``AWS::AmplifyUIBuilder::Form``AWS::AmplifyUIBuilder::Theme` |
| `AWS::ApiGateway` | `AWS::ApiGateway::Account``AWS::ApiGateway::Method` |
| `AWS::ApiGatewayV2` | `AWS::ApiGatewayV2::IntegrationResponse``AWS::ApiGatewayV2::RouteResponse` |
| `AWS::AppConfig` | `AWS::AppConfig::Deployment``AWS::AppConfig::HostedConfigurationVersion` |
| `AWS::ApplicationAutoScaling` | `AWS::ApplicationAutoScaling::ScalableTarget``AWS::ApplicationAutoScaling::ScalingPolicy` |
| `AWS::AppStream` | `AWS::AppStream::AppBlock``AWS::AppStream::Application``AWS::AppStream::ApplicationEntitlementAssociation``AWS::AppStream::ApplicationFleetAssociation``AWS::AppStream::Entitlement` |
| `AWS::AppSync` | `AWS::AppSync::DomainNameApiAssociation` |
| `AWS::AppTest` | `AWS::AppTest::TestCase` |
| `AWS::AuditManager` | `AWS::AuditManager::Assessment` |
| `AWS::Bedrock` | `AWS::Bedrock::GuardrailVersion` |
| `AWS::BillingConductor` | `AWS::BillingConductor::BillingGroup``AWS::BillingConductor::CustomLineItem``AWS::BillingConductor::PricingPlan``AWS::BillingConductor::PricingRule` |
| `AWS::Cassandra` | `AWS::Cassandra::Keyspace``AWS::Cassandra::Type` |
| `AWS::CE` | `AWS::CE::AnomalyMonitor``AWS::CE::AnomalySubscription` |
| `AWS::CertificateManager` | `AWS::CertificateManager::Account` |
| `AWS::CloudFormation` | `AWS::CloudFormation::ModuleVersion``AWS::CloudFormation::Publisher``AWS::CloudFormation::ResourceDefaultVersion``AWS::CloudFormation::ResourceVersion` |
| `AWS::CloudFront` | `AWS::CloudFront::MonitoringSubscription` |
| `AWS::CloudTrail` | `AWS::CloudTrail::ResourcePolicy` |
| `AWS::Cognito` | `AWS::Cognito::LogDeliveryConfiguration``AWS::Cognito::ManagedLoginBranding``AWS::Cognito::UserPoolDomain``AWS::Cognito::UserPoolRiskConfigurationAttachment``AWS::Cognito::UserPoolUICustomizationAttachment``AWS::Cognito::UserPoolUserToGroupAttachment` |
| `AWS::Config` | `AWS::Config::OrganizationConformancePack` |
| `AWS::Connect` | `AWS::Connect::ContactFlowVersion``AWS::Connect::DataTableAttribute``AWS::Connect::DataTableRecord``AWS::Connect::InstanceStorageConfig``AWS::Connect::UserHierarchyStructure``AWS::Connect::ViewVersion` |
| `AWS::ControlTower` | `AWS::ControlTower::EnabledBaseline``AWS::ControlTower::EnabledControl` |
| `AWS::DataZone` | `AWS::DataZone::DataSource``AWS::DataZone::DomainUnit``AWS::DataZone::Environment``AWS::DataZone::EnvironmentActions``AWS::DataZone::FormType``AWS::DataZone::Owner``AWS::DataZone::PolicyGrant``AWS::DataZone::ProjectMembership``AWS::DataZone::ProjectProfile` |
| `AWS::Deadline` | `AWS::Deadline::QueueEnvironment` |
| `AWS::Detective` | `AWS::Detective::OrganizationAdmin` |
| `AWS::DeviceFarm` | `AWS::DeviceFarm::DevicePool``AWS::DeviceFarm::InstanceProfile``AWS::DeviceFarm::NetworkProfile``AWS::DeviceFarm::Project``AWS::DeviceFarm::TestGridProject``AWS::DeviceFarm::VPCEConfiguration` |
| `AWS::EC2` | `AWS::EC2::EnclaveCertificateIamRoleAssociation``AWS::EC2::GatewayRouteTableAssociation``AWS::EC2::VPCBlockPublicAccessOptions` |
| `AWS::ECS` | `AWS::ECS::ExpressGatewayService``AWS::ECS::PrimaryTaskSet``AWS::ECS::TaskSet` |
| `AWS::ElasticLoadBalancingV2` | `AWS::ElasticLoadBalancingV2::ListenerRule` |
| `AWS::EMR` | `AWS::EMR::Step` |
| `AWS::EventSchemas` | `AWS::EventSchemas::RegistryPolicy` |
| `AWS::Evidently` | `AWS::Evidently::Experiment``AWS::Evidently::Feature``AWS::Evidently::Launch``AWS::Evidently::Project``AWS::Evidently::Segment` |
| `AWS::FMS` | `AWS::FMS::NotificationChannel``AWS::FMS::Policy``AWS::FMS::ResourceSet` |
| `AWS::GlobalAccelerator` | `AWS::GlobalAccelerator::EndpointGroup` |
| `AWS::Glue` | `AWS::Glue::IdentityCenterConfiguration``AWS::Glue::SchemaVersionMetadata` |
| `AWS::IAM` | `AWS::IAM::GroupPolicy``AWS::IAM::RolePolicy``AWS::IAM::ServiceLinkedRole``AWS::IAM::UserPolicy` |
| `AWS::IdentityStore` | `AWS::IdentityStore::GroupMembership` |
| `AWS::Inspector` | `AWS::Inspector::AssessmentTarget``AWS::Inspector::AssessmentTemplate``AWS::Inspector::ResourceGroup` |
| `AWS::InspectorV2` | `AWS::InspectorV2::CisScanConfiguration` |
| `AWS::IoT` | `AWS::IoT::ThingType` |
| `AWS::IoTAnalytics` | `AWS::IoTAnalytics::Channel``AWS::IoTAnalytics::Dataset``AWS::IoTAnalytics::Datastore``AWS::IoTAnalytics::Pipeline` |
| `AWS::IoTEvents` | `AWS::IoTEvents::AlarmModel``AWS::IoTEvents::DetectorModel``AWS::IoTEvents::Input` |
| `AWS::IoTFleetWise` | `AWS::IoTFleetWise::Campaign``AWS::IoTFleetWise::DecoderManifest``AWS::IoTFleetWise::Fleet``AWS::IoTFleetWise::ModelManifest``AWS::IoTFleetWise::SignalCatalog``AWS::IoTFleetWise::StateTemplate``AWS::IoTFleetWise::Vehicle` |
| `AWS::IoTSiteWise` | `AWS::IoTSiteWise::Dashboard` |
| `AWS::Kinesis` | `AWS::Kinesis::ResourcePolicy` |
| `AWS::LakeFormation` | `AWS::LakeFormation::PrincipalPermissions``AWS::LakeFormation::TagAssociation` |
| `AWS::Lambda` | `AWS::Lambda::LayerVersion``AWS::Lambda::LayerVersionPermission` |
| `AWS::LicenseManager` | `AWS::LicenseManager::Grant``AWS::LicenseManager::License` |
| `AWS::Logs` | `AWS::Logs::AccountPolicy` |
| `AWS::LookoutVision` | `AWS::LookoutVision::Project` |
| `AWS::Macie` | `AWS::Macie::AllowList``AWS::Macie::CustomDataIdentifier``AWS::Macie::FindingsFilter` |
| `AWS::MediaConnect` | `AWS::MediaConnect::BridgeOutput``AWS::MediaConnect::BridgeSource` |
| `AWS::MediaLive` | `AWS::MediaLive::ChannelPlacementGroup``AWS::MediaLive::Cluster``AWS::MediaLive::Network``AWS::MediaLive::SdiSource` |
| `AWS::MediaPackageV2` | `AWS::MediaPackageV2::ChannelPolicy``AWS::MediaPackageV2::OriginEndpoint``AWS::MediaPackageV2::OriginEndpointPolicy` |
| `AWS::MediaTailor` | `AWS::MediaTailor::ChannelPolicy` |
| `AWS::NetworkFirewall` | `AWS::NetworkFirewall::LoggingConfiguration` |
| `AWS::Notifications` | `AWS::Notifications::ManagedNotificationAccountContactAssociation``AWS::Notifications::ManagedNotificationAdditionalChannelAssociation` |
| `AWS::ObservabilityAdmin` | `AWS::ObservabilityAdmin::OrganizationCentralizationRule``AWS::ObservabilityAdmin::OrganizationTelemetryRule``AWS::ObservabilityAdmin::TelemetryRule` |
| `AWS::ODB` | `AWS::ODB::CloudAutonomousVmCluster``AWS::ODB::CloudExadataInfrastructure``AWS::ODB::CloudVmCluster``AWS::ODB::OdbNetwork``AWS::ODB::OdbPeeringConnection` |
| `AWS::OpenSearchServerless` | `AWS::OpenSearchServerless::AccessPolicy``AWS::OpenSearchServerless::LifecyclePolicy``AWS::OpenSearchServerless::SecurityConfig``AWS::OpenSearchServerless::SecurityPolicy` |
| `AWS::OpenSearchService` | `AWS::OpenSearchService::Domain` |
| `AWS::Organizations` | `AWS::Organizations::Account``AWS::Organizations::OrganizationalUnit``AWS::Organizations::Policy``AWS::Organizations::ResourcePolicy` |
| `AWS::Panorama` | `AWS::Panorama::PackageVersion` |
| `AWS::PCAConnectorAD` | `AWS::PCAConnectorAD::TemplateGroupAccessControlEntry` |
| `AWS::QLDB` | `AWS::QLDB::Stream` |
| `AWS::QuickSight` | `AWS::QuickSight::Analysis``AWS::QuickSight::Dashboard``AWS::QuickSight::DataSet``AWS::QuickSight::DataSource``AWS::QuickSight::RefreshSchedule``AWS::QuickSight::Template``AWS::QuickSight::Theme``AWS::QuickSight::Topic``AWS::QuickSight::VPCConnection` |
| `AWS::Rbin` | `AWS::Rbin::Rule` |
| `AWS::RefactorSpaces` | `AWS::RefactorSpaces::Application``AWS::RefactorSpaces::Route``AWS::RefactorSpaces::Service` |
| `AWS::ResourceExplorer2` | `AWS::ResourceExplorer2::DefaultViewAssociation` |
| `AWS::RTBFabric` | `AWS::RTBFabric::InboundExternalLink``AWS::RTBFabric::Link``AWS::RTBFabric::OutboundExternalLink` |
| `AWS::S3` | `AWS::S3::AccessGrant``AWS::S3::AccessGrantsLocation``AWS::S3::MultiRegionAccessPointPolicy` |
| `AWS::S3ObjectLambda` | `AWS::S3ObjectLambda::AccessPointPolicy` |
| `AWS::S3Outposts` | `AWS::S3Outposts::AccessPoint``AWS::S3Outposts::Bucket``AWS::S3Outposts::BucketPolicy` |
| `AWS::S3Tables` | `AWS::S3Tables::Table``AWS::S3Tables::TablePolicy` |
| `AWS::SageMaker` | `AWS::SageMaker::Device``AWS::SageMaker::DeviceFleet` |
| `AWS::SecurityHub` | `AWS::SecurityHub::AggregatorV2``AWS::SecurityHub::AutomationRule``AWS::SecurityHub::AutomationRuleV2``AWS::SecurityHub::ConfigurationPolicy``AWS::SecurityHub::ConnectorV2``AWS::SecurityHub::DelegatedAdmin``AWS::SecurityHub::FindingAggregator``AWS::SecurityHub::Insight``AWS::SecurityHub::OrganizationConfiguration``AWS::SecurityHub::PolicyAssociation``AWS::SecurityHub::ProductSubscription``AWS::SecurityHub::SecurityControl``AWS::SecurityHub::Standard` |
| `AWS::SecurityLake` | `AWS::SecurityLake::AWSLogSource``AWS::SecurityLake::Subscriber``AWS::SecurityLake::SubscriberNotification` |
| `AWS::ServiceCatalog` | `AWS::ServiceCatalog::CloudFormationProvisionedProduct``AWS::ServiceCatalog::PortfolioProductAssociation``AWS::ServiceCatalog::ServiceActionAssociation``AWS::ServiceCatalog::TagOption``AWS::ServiceCatalog::TagOptionAssociation` |
| `AWS::SES` | `AWS::SES::VdmAttributes` |
| `AWS::Shield` | `AWS::Shield::DRTAccess``AWS::Shield::ProactiveEngagement``AWS::Shield::Protection``AWS::Shield::ProtectionGroup` |
| `AWS::SimSpaceWeaver` | `AWS::SimSpaceWeaver::Simulation` |
| `AWS::SNS` | `AWS::SNS::TopicInlinePolicy` |
| `AWS::SQS` | `AWS::SQS::QueueInlinePolicy` |
| `AWS::SSMContacts` | `AWS::SSMContacts::Rotation` |
| `AWS::SSO` | `AWS::SSO::Application``AWS::SSO::ApplicationAssignment``AWS::SSO::Assignment``AWS::SSO::InstanceAccessControlAttributeConfiguration``AWS::SSO::PermissionSet` |
| `AWS::Timestream` | `AWS::Timestream::Database``AWS::Timestream::ScheduledQuery``AWS::Timestream::Table` |
| `AWS::VoiceID` | `AWS::VoiceID::Domain` |
| `AWS::VpcLattice` | `AWS::VpcLattice::AuthPolicy``AWS::VpcLattice::ResourcePolicy``AWS::VpcLattice::Rule` |
| `AWS::WAFv2` | `AWS::WAFv2::IPSet``AWS::WAFv2::RegexPatternSet``AWS::WAFv2::RuleGroup``AWS::WAFv2::WebACL``AWS::WAFv2::WebACLAssociation` |
| `AWS::Wisdom` | `AWS::Wisdom::AIAgentVersion``AWS::Wisdom::AIGuardrailVersion``AWS::Wisdom::AIPromptVersion` |

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-quotas.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
