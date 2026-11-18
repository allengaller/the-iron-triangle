<!-- source: https://help.aliyun.com/zh/well-architected/intelligent-account-asking-mcp-scheme -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2981948 -->

# 智能问账MCP方案

传统模式下需要搭建企业云成本管理平台或者使用本地脚本对云成本进行洞察。使用LLM的能力可以降低云成本洞察门槛。


传统模式下需要搭建企业云成本管理平台或者使用本地脚本对云成本进行洞察。使用LLM的能力可以降低云成本洞察门槛。

# 方案概述

![智能问账MCP方案](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286108571/p1006262.jpg)

随着企业云上业务的不断扩展，传统的成本管理方式已难以满足现代企业的需求。单纯依赖产品账单和地域账单等基础维度进行成本分析，已经无法全面反映企业真实的资源使用情况和业务价值。为了更精准地实现成本管控，企业往往面临多云账单管理、定制化趋势分析等更加个性化的需求。这种智能化的成本自助分析能力，不仅能够帮助企业更清晰地洞察资源消耗与业务产出的关系，还能为优化资源配置和提升运营效率提供有力支持。

本文档介绍了一种通过MaxCompute结合AI技术在云上实现的自助成本分析方案。借助AI技术，企业可以显著降低对账单自主分析的人力成本。通过LLM用户只需使用简单的自然语言指令即可完成复杂的成本分析任务。例如，用户可以通过提问“过去一个月在哪些财务单元的云服务开销最高？”或“哪个月份的云资源使用量最大？”来获取所需的信息。这种智能化的成本分析工具不仅提高了效率，还使得非技术背景的员工也能轻松掌握成本管理的关键数据，从而更好地支持企业的决策制定和业务优化。

# 方案优势

### 基于原始数据自助分析

通过直接对接云平台的原始账单数据，为企业提供了高度灵活的自助分析能力。企业可以根据自身业务特点，自由组合分析维度，例如按团队、项目、环境（开发/测试/生产）、资源类型等进行多维拆解。

### 无需研发人员搭建成本平台

本技术方案采用开箱即用的设计理念，企业无需投入研发团队即可快速上手，大幅降低了技术门槛和人力成本。

### 对账单处理灵活度高

通过自然语言即可生成账单分析的SQL语言，可以根据企业自身需要自行配置promt，引导大模型根据企业需求分析。

# 客户场景

## 分析云计算成本数据与业务数据趋势

#### 场景描述

云资源的费用趋势与业务数据的趋势存在一定的关联性，如果出现不符合预期的费用趋势，说明在产品使用上出现异常

#### 适用客户

- 需要精细化成本管理的企业

## 分析多云成本数据

#### 场景描述

企业需要聚合多个平台上的账单数据按照统一的财务视角进行分析

#### 适用客户

- 使用多个云服务商的企业

# 方案架构

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286108571/p1007305.png)

大模型并不擅长对海量数据进行直接处理，但是他擅长理解自然语言，可以把自然语言转译为机器可理解的代码语言。该方案的核心解决思路在于利用MaxCompute的强大计算能力来处理海量账单数据，并结合大语言模型（LLM）将用户的自然语言查询转化为MaxCompute能够理解和执行的SQL语句，从而实现对账单数据的深度分析和智能查询。

# 产品费用及名词

## 产品费用

| 产品名称 | 产品说明 | 产品费用 |
| --- | --- | --- |
| Maxcompute | [云原生大数据计算服务 MaxCompute](https://help.aliyun.com/zh/maxcompute/user-guide/what-is-maxcompute)是一种快速、完全托管的TB/PB级数据仓库解决方案。MaxCompute向用户提供了完善的数据导入方案以及多种经典的分布式计算模型，能够更快速的解决用户海量数据计算问题，有效降低企业成本，并保障数据安全。 | 收费，详情参见[计费概述](https://help.aliyun.com/zh/maxcompute/overview-31)。 |
| Function AI | [Function AI](https://help.aliyun.com/zh/functioncompute/what-is-a-serverless-development-platform)是基于函数计算构建的一站式应用开发及应用生命周期管理平台。该平台提供了开箱即用的近百款热门应用模板，场景覆盖人工智能、Web开发框架、文件处理、Web应用以及音视频处理等。只需简单配置即可一键部署应用，快速验证业务逻辑，同时，所有模板均支持二次开发，开发者可基于模板代码灵活扩展功能、集成自定义逻辑，满足个性化需求，实现从“模板到生产环境”的无缝衔接，大幅降低开发门槛并提升效率。 | 收费，详情参见[计费说明](https://help.aliyun.com/zh/functioncompute/what-is-a-serverless-development-platform#8495e55060qp6)。 |
| 百炼 | [阿里云的大模型服务平台百炼](https://help.aliyun.com/zh/model-studio/what-is-model-studio)是一站式的大模型开发及应用构建平台。不论是开发者还是业务人员，都能深入参与大模型应用的设计和构建。您可以通过简单的界面操作，在5分钟内开发出一款大模型应用，或在几小时内训练出一个专属模型，从而将更多精力专注于应用创新。 | 收费，详情参见[计费说明](https://help.aliyun.com/zh/model-studio/models) |

## 名词解释

| 名称 | 说明 |
| --- | --- |
| MCP | Model Context Protocol是一个开放协议，它标准化了应用程序向 LLM 提供上下文的方式。可以将 MCP 视为 AI 应用的 USB-C 端口。正如 USB-C 提供了一种标准化的方式将您的设备连接到各种外围设备和配件一样，MCP 提供了一种标准化的方式将 AI 模型连接到不同的数据源和工具。 |

# 安全性

## Function AI的服务角色

可信云服务可以通过RAM角色扮演的方式访问其他云服务的资源。可信实体为阿里云服务的RAM角色，包括普通服务角色和服务关联角色。本文介绍Function AI的服务关联角色。关于服务关联角色的更多信息，请参见[服务关联角色](https://help.aliyun.com/zh/ram/user-guide/service-linked-roles#concept-2448621)。

# 注意事项

### 大模型幻觉

大型语言模型在生成文本时产生与事实不符或逻辑不一致的内容，即使输入的提示信息是正确的。这种现象通常是由于模型在训练过程中学习到了一些错误的模式或信息，或者在推理过程中出现了偏差。大模型幻觉可能导致生成的回答不可靠，甚至包含错误的事实或误导性的信息。因此，在使用大模型时，需要特别注意验证生成内容的准确性和可靠性。建议在大模型生成SQL之后，人为check SQL内容是否符合预期。

# 实施步骤

## 实施时长

在实施准备工作完成的情况下，本方案实施预计时长：2小时。

## 操作步骤

### 云资源账单投递

**实时账单投递**

前往成本管理--成本分析--更多分析工具

![](https://intranetproxy.alipay.com/skylark/lark/0/2025/png/83756392/1739244248221-60123f87-a3b1-441b-b1f1-ea0a17d544fa.png)

按照页面指引打开账单投递功能，投递配置完成之后可以根据企业要求订阅合适的账单数据

![](https://intranetproxy.alipay.com/skylark/lark/0/2025/png/83756392/1739253094074-9667da6a-0e06-4dfe-8c96-59a045032f2e.png)

![](https://intranetproxy.alipay.com/skylark/lark/0/2025/png/83756392/1739253106268-20508478-8815-42b9-ad7b-0b2ae5f3ca9a.png)

配置完成之后，可以前往[maxcompute](https://maxcompute.console.aliyun.com/cn-shanghai/project-list/managed)，系统自动在maxcompute中创建一个新的项目cost_mgt_xxxx。

**离线账单投递**

前往[maxcompute](https://maxcompute.console.aliyun.com/cn-shanghai/project-list/managed)--数据传输--数据上传，将本地已经下载的离线账单上传

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286108571/p1006691.png)

在设置目标表时建议在cost_mgt_xxxx项目中新建一个表，点击“上传数据”。

注意：离线账单数据为了保证长数字格式不自动转变，会塞入一些特殊字符（tab），增加LLM生成SQL的复杂度，导致查询结果出现误差。建议在本地清洗完成之后再上传。

### MCP开发

MCP的主要作用是完成对ODPS的操作封装，让LLM可以自主调用ODPS的操作。考虑到MCP可以覆盖更多场景，可以使用函数计算FC- Function AI来部署MCP server。

前往[Function AI](https://functionai.console.aliyun.com/explore)-项目-创建MCP![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286108571/p1006719.png)

选择函数部署的region以及函数名称，选择“SSE协议”（如果是本地开发代码可以选择“STDIO协议”），运行环境选择python 3.10，仓库可以选择默认。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286108571/p1006723.png)

在函数计算WebIDE main.py文件中贴入以下代码，实现对MaxCompute获取表头（get_table）和执行SQL（execute_sql）

```
from dotenv import load_dotenv from mcp.server.fastmcp import FastMCP from starlette.applications import Starlette from starlette.applications import Starlette from starlette.routing import Mount from odps import ODPS from odps.accounts import StsAccount import json import os load_dotenv() account = StsAccount( os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'), os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), os.getenv('ALIBABA_CLOUD_SECURITY_TOKEN'), ) project = os.environ.get('project') tableName = os.environ.get('table') endpoint = os.environ.get('endpoint') o = ODPS( account=account, project=project, endpoint=endpoint ) mcp = FastMCP("aliyun-bss-mcp") @mcp.tool() async def execute_sql(sql: str,) -> str: """ 用于执行sql语句 Args: sql: sql内容 """ with o.execute_sql(sql, hints={'odps.sql.submit.mode': 'script'}).open_reader() as reader: columns = [col.name for col in reader._schema.columns] data = [] for record in reader: data.append(record.values) result = { "columns": columns, "data": data } return json.dumps(result, ensure_ascii=False, indent=2) @mcp.tool() async def get_table() -> str: """ 用于查看MaxCompute内部表、视图、外部表、聚簇表或Transactional表的信息 """ table = o.get_table(tableName) columns = [] for col in table.schema.columns: columns.append({ 'name': col.name, 'type': col.type.name if hasattr(col.type, 'name') else str(col.type), 'comment': col.comment or '' }) # 转换为 JSON 字符串 columns_json = json.dumps(columns, ensure_ascii=False, indent=2) return columns_json app = Starlette( routes=[ Mount('/', app=mcp.sse_app()), ] )
```

进入配置，为当前实例创建一个函数角色。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1286108571/p1006728.png)

前往[MaxCompute项目](https://maxcompute.console.aliyun.com/cn-shanghai/project-list/managed)中为当前函数角色ODPS tabel权限，避免因为角色缺少对应table权限而报错。可以在对应项目--角色权限--成本管理中添加对应的RAM角色。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286108571/p1006769.png)

同时需要在函数计算的服务变量中根据maxcompute的配置信息，完成endpoint、project、table的配置，确保函数计算可以找到对应table

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286108571/p1006774.png)

完成之后，点击部署按钮。

### Agent搭建

基于百炼搭建Agent，实现大模型对MCP的调用场景。

前往[百炼-MCP管理](https://bailian.console.aliyun.com/tab=app#/mcp-manage/custom)点击创建MCP，选择使用脚本部署

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286108571/p1006925.png)

安装方式使用http，在MCP服务配置里面输入以下脚本

```
{ "mcpServers": { "aliyun-bss-mcp": { "type": "sse", "url": "从函数计算FC获取SSE地址" } } }
```

前往[应用管理](https://bailian.console.aliyun.com/tab=app?tab=app#/app-center)点击创建应用，选择智能体应用

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286108571/p1006929.png)

在配置页面，选择适合自己的模型，比如千问3-Coder-Plus，在技能--MCP服务中可以添加刚创建的MCP服务

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0286108571/p1006933.png)

在提示词中输入以下内容

```
你是一个精通MaxCompute SQL以及阿里云资源账单的专家 请使用SQL的技能回答我关于云资源账单相关的问题 要求： 1、使用中文回答 表名：xxxx 通用场景（适用于月度汇总、成本聚合、折扣分析）： 第一步：通过“get_table”查询表名为${表名}的信息，找到每一列的字段信息 第二步：使用“execute_sql”执行“SELECT * FROM {table.name} LIMIT 2”进行采样数据 第三步：根据我的要求生成相应的SQL指令 第四步:通过“execute_sql”执行SQL指令 特殊场景-优惠信息 无优惠的产品判断逻辑：优惠后金额=官网价 特殊场景-预算测算 如果某个月账单不存在，就执行预算测算的逻辑，提取前6个月的费用数据，采用月增长率法的方式来测算单个产品的预算情况。 特殊场景-异常消费 高额消费：应付金额&gt;10000 异常折扣：优惠后金额/官网价&gt;0.9 异常欠费：欠费金额&gt;10000
```

在右侧文本对话框中即可体验当前的智能问账的效果

---

> 原页面：https://help.aliyun.com/zh/well-architected/intelligent-account-asking-mcp-scheme（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
