# allen-writes Examples

## Example 1: Diátaxis Type Annotation

**Input**: "帮我写一章关于 TAM 起源的内容"

**Output**: First line of the generated file:
```markdown
<!-- Diátaxis: Explanation -->
# 第 1 章　TAM 的起源与演进
```

## Example 2: How-to Guide Structure

**Input**: "写一个服务计划的模板"

**Output structure**:
```markdown
<!-- Diátaxis: How-to -->
# 如何制定服务计划

## 目标
在客户签约后 60 天内完成首版服务计划。

## 前置条件
- 已完成客户技术档案初稿
- 已与客户接口人确认例会节奏

## 步骤
1. **现状盘点**：收集系统清单、SLA、故障史
2. **目标对齐**：与客户确认年度业务目标
3. **动作设计**：列出季度服务动作与交付物
4. **双方签认**：客户接口人签字确认
5. **纳入跟踪**：在服务月会上跟踪执行

## 验收标准
- [ ] 服务计划已与客户共同签署
- [ ] 计划项按期完成率 > 80%

## 常见错误
- 范围无界：未明确"不覆盖什么"
- 目标空话：写成"做好服务工作"式描述
```

## Example 3: AI Slop Removal

**Input**: "润色以下段落：
> In today's rapidly evolving world of cloud computing, it's important to note that TAMs play a crucial role in ensuring customer success."

**Output**:
> TAM 对客户系统稳定性的影响是量化的：专属 TAM 客户的故障恢复时间平均缩短 40%。

## Example 4: Terminology Consistency Check

**Input**: "检查以下术语是否统一：
- 技术客户经理
- TAM (Technical Account Manager)
- Technical Account Manager (TAM)"

**Output**:
- ❌ "技术客户经理" — 缺少英文对照
- ✅ "TAM（Technical Account Manager，技术客户经理）" — 首次出现格式正确
- ✅ "TAM" — 后续引用正确
