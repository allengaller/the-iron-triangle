# Diátaxis 重构 TODO 清单

> 基于 Diátaxis 框架对 the-tam-book 进行文档类型梳理与结构优化的任务清单。
> 优先级：P0（阻塞性）> P1（高）> P2（中）> P3（低）

---

## P0 — 基础设施（必须先完成）

### ✅ DONE — 将 Diátaxis 要义沉淀到 AGENTS.md
- **涉及文件**：`the-tam-book/AGENTS.md`
- **已完成动作**：
  - [x] 增加「Diátaxis 文档类型约定」章节
  - [x] 定义四种类型（Tutorial / How-to / Reference / Explanation）及其适用章节
  - [x] 增加类型标注格式（`<!-- Diátaxis: Explanation -->`）
  - [x] 增加自检清单分类约定（学习效果清单 vs 执行检查清单）
  - [x] 模板引用格式统一为"模板 01"（两位数字补零）

---

### [ ] P0-2 — 为全书 28 章 + 附录标注 Diátaxis 类型
- **涉及文件**：`manuscript/` 目录下全部 `.md` 文件
- **具体动作**：
  - [ ] 每章首行增加类型标注注释（`<!-- Diátaxis: {Type} -->`）
  - [ ] 在 `manuscript/00-outline.md` 中增加类型标注列
  - [ ] 创建 `manuscript/DIATAXIS-MAP.md` 作为类型总览
- **验收标准**：
  - 所有章节文件首行均有类型标注
  - 同一章节内不混合两种以上类型（当前混合的标注为"待拆分"）

| 章节 | 当前类型判断 | 目标类型 | 混合问题 | 优先级 |
|------|------------|----------|----------|--------|
| ch01 | Explanation | Explanation | 无 | P1 |
| ch02 | Reference+How-to | Reference | 归属判断三问混入 | P1 |
| ch03 | Explanation | Explanation | 无 | P3 |
| ch04 | Explanation | Explanation | 无 | P3 |
| ch05 | 四类型混合 | Explanation + How-to（拆分） | 分级标准+训练方法混入 | P0 |
| ch06 | 四类型混合 | Explanation + How-to（拆分） | 同上 | P1 |
| ch07 | 四类型混合 | Explanation + How-to（拆分） | 同上 | P1 |
| ch08 | How-to + Reference | How-to（分级标准拆出） | 分级标准+五维框架混入 | P1 |
| ch09 | How-to + Reference | How-to（分级标准拆出） | 分级标准混入 | P1 |
| ch10 | How-to | How-to | 仅分级标准需拆出 | P2 |
| ch11-ch15 | 待评估 | — | — | P2 |
| ch16-ch28 | 待评估 | — | — | P2 |
| appx-a | Reference | Reference | 无 | P3 |
| appx-b | Reference+How-to | Reference（关键步骤拆出） | B.2/B.3 混入 How-to | P1 |

---

## P1 — 结构拆分（影响阅读体验）

### [ ] P1-1 — 按 Diátaxis 拆分"内涵篇"统一结构（ch05-ch10）
- **涉及文件**：`manuscript/ch05.md` ~ `manuscript/ch10.md`
- **问题描述**：当前统一结构「能力定义 → 核心技能 → 分级标准 → 训练方法 → 自检清单」强制混合了 Explanation / How-to / Reference / Tutorial 四种类型
- **拆分方案**：
  ```
  当前：第 5 章　技术纵深（Explanation+How-to+Reference+Tutorial 混合）
  
  拆分为：
  ├── 第 5 章　技术纵深（Explanation）
  │     └─ 能力定义 + 核心概念 + 常见误区
  ├── 第 5+ 章　技术纵深实战（How-to）← 新增
  │     └─ 架构评审 + 容量规划 + 可用性评审 + 版本管理
  └── 附录 X：技术纵深分级标准（Reference）← 新增或合并至 appx-g
  
  训练方法（Tutorial）迁移至：附录 Y：六维能力训练教程
  ```
- **验收标准**：
  - 每章只保留单一 Diátaxis 类型
  - 被拆出的内容在新位置完整保留，不丢失信息
  - 原章节增加「拆分说明」注释，指向新位置

### [ ] P1-2 — 将"分级标准"从各章提取合并为独立 Reference
- **涉及文件**：`manuscript/ch05.md` ~ `manuscript/ch10.md` + `manuscript/appx-g.md`
- **具体动作**：
  - [ ] 提取 ch05 L1-L5 分级标准 → 合并至 appx-g 或新建 `appx-standards.md`
  - [ ] 提取 ch06 L1-L5 分级标准 → 同上
  - [ ] 提取 ch07 L1-L5 分级标准 → 同上
  - [ ] 提取 ch08 L1-L5 分级标准 → 同上
  - [ ] 提取 ch09 L1-L5 分级标准 → 同上
  - [ ] 提取 ch10 L1-L5 分级标准 → 同上
- **验收标准**：
  - 分级标准在独立附录中完整呈现
  - 原章节只保留"如何判定自己处于哪一级"的 How-to 描述
  - 独立附录支持跨维度对比（横向查看六维各级别要求）

### [ ] P1-3 — ch02 边界对照表与归属判断分离
- **涉及文件**：`manuscript/ch02-role-boundary-map.md`
- **问题**：六对边界对照表（Reference）与归属判断三问（How-to）混合
- **方案**：
  - Reference 部分（2.1-2.3）：保留在 ch02
  - How-to 部分（2.4-2.5）：迁移至 ch13（内部协同）或新增"接缝处理指南"
- **验收标准**：ch02 只保留"是什么"（Reference），不保留"怎么做"（How-to）

### [ ] P1-4 — appx-b 运营规范与流程速查分离
- **涉及文件**：`manuscript/appx-b-tam-process-system.md`
- **问题**：B.2/B.3 混入大量 How-to 内容，破坏了 Reference 的速查定位
- **方案**：
  - Reference 部分（B.1 流程地图）：保留在 appx-b
  - How-to 部分（B.2 逐项速查的"关键步骤"、B.3 运营规范）：
    - B.2"关键步骤"提取为"重保立项操作指南"等独立 How-to
    - B.3 运营规范提取为独立 `HOW-TO.md` 或合并至 ch08
- **验收标准**：appx-b 只保留流程定义、触发条件、交付物等 Reference 信息

---

## P2 — 内容重组（提升可用性）

### [ ] P2-1 — 将训练方法提取为 Tutorial 独立内容
- **涉及文件**：`manuscript/ch05.md` ~ `manuscript/ch10.md`
- **问题描述**：训练方法（影子评审、back-of-envelope、一页纸报告等）是宝贵的 Tutorial 素材，但散落在各章中
- **方案**：
  - 新增「附录 Y：六维能力训练教程」
  - 按能力维度分节，每节包含：
    - 训练目标（达成什么能力级别）
    - 前置条件（需要什么基础）
    - 分步操作（具体训练步骤）
    - 验证标准（如何判断训练达标）
    - 常见错误
  - 原章节训练方法节保留简要说明，指向附录 Y
- **验收标准**：
  - 附录 Y 包含所有六维的训练教程
  - 每篇 Tutorial 读者能按步骤完成并获得可见成果

### [ ] P2-2 — 自检清单分类：学习效果 vs 执行检查
- **涉及文件**：`manuscript/ch01.md` ~ `manuscript/ch28.md`
- **当前问题**：所有自检清单都是同一格式，未区分类型
- **分类方案**：

| 章节类型 | 清单类型 | 示例 |
|----------|----------|------|
| Explanation | 学习效果清单 | "能用自己的话解释 TAM 三次跃迁的驱动力" |
| How-to | 执行检查清单 | "服务计划已与客户共同签署" |
| Reference | 不适用或简化 | "已查阅术语表中 X 的定义" |
| Tutorial | 训练验证清单 | "已完成一次影子评审并收到反馈" |

- **验收标准**：
  - 每章自检清单标题明确标注类型（"学习效果清单"或"执行检查清单"）
  - Explanation 章的清单项改为"能/会/理解"句式
  - How-to 章的清单项保持"已/完成/确认"句式

### [ ] P2-3 — 模板引用格式统一
- **涉及文件**：全书
- **当前问题**：存在"模板01""模板 1""模板01"等多种变体
- **统一方案**：
  - 所有模板引用统一为"模板 01"（空格分隔，两位数字补零）
  - 搜索替换：正则 `模板s*0?(d+)` → `模板 ${String(Number($1)).padStart(2, '0')}`
- **涉及模板**：模板 01-19（当前 templates/ 目录下 19 个模板）
- **验收标准**：
  - 全书中"模板"引用格式统一为"模板 XX"
  - 无"模板01""模板 1"等变体

---

## P3 — 细节打磨（长期维护）

### [ ] P3-1 — 术语书写统一规范落地
- **涉及文件**：`manuscript/appx-a-glossary.md` + 全书
- **规范内容**：
  - **首次出现**：中文全称 + 英文全称 + 缩写，例"技术客户经理（Technical Account Manager，TAM）"
  - **后续引用**：可单独使用中文或缩写
  - **禁止**：首次出现只写缩写、中英文顺序颠倒
- **检查动作**：
  - [ ] 抽查 ch01-ch05 术语首次出现格式
  - [ ] 抽查 appx-a 定义与正文引用一致性
  - [ ] 修正不符合规范的术语出现

### [ ] P3-2 — 编号前缀歧义消解
- **涉及文件**：全书
- **当前状态**：A.8 已给出速查表，但正文中仍有无语境的"P1"引用
- **动作**：
  - [ ] 全局搜索"P1""P2""P3""P4""P5"，检查是否带语境限定词
  - [ ] 修正无语境引用为带语境形式（"故障 P1""流程 P5"）

### [ ] P3-3 — 创建 `manuscript/DIATAXIS-MAP.md` 类型总览
- **涉及文件**：`manuscript/DIATAXIS-MAP.md`（新增）
- **内容**：
  - 全书章节 Diátaxis 类型总览表
  - 每种类型对应的章节列表
  - 混合类型章节的拆分状态跟踪
  - 与目录文件 `00-outline.md` 的联动方式

---

## 执行顺序建议

```
Phase 1（本周）：P0-2 + P1-1 + P1-2
  └─ 先完成类型标注，再拆分 ch05-ch10 结构

Phase 2（下周）：P1-3 + P1-4 + P2-1
  └─ 完成 appx-b 和 ch02 的分离，开始训练教程整理

Phase 3（第三周）：P2-2 + P2-3 + P3-1
  └─ 清单分类、模板格式、术语规范

Phase 4（持续）：P3-2 + P3-3
  └─ 细节检查，长期维护
```

---

## 快速查询

### 当前最严重的问题章节（混合类型）
1. **ch05-ch10（内涵六维）**：统一结构强制混合四种类型，需按 Diátaxis 拆分
2. **ch02（边界图谱）**：Reference 与 How-to 混合
3. **appx-b（流程规范）**：Reference 与 How-to 混合

### 已符合 Diátaxis 的章节（无需改动）
- `ch01-tam-origin-evolution.md` — Explanation ✅
- `appx-a-glossary.md` — Reference ✅

### 待评估的章节（需要逐一阅读判断）
- ch11-ch28（外延篇 + 专项篇）
- appx-c ~ appx-v（其余附录）
