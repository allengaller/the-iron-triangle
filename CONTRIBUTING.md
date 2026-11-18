# 贡献指南

本页只给路由与自检命令。贡献的门槛与体例定义在书内，不在这里重复。

## 三类贡献，三个入口

| 想改什么 | 入口 | 体例定义 |
| --- | --- | --- |
| 勘误：错字、错误引用、过期数据 | [勘误 Issue](.github/ISSUE_TEMPLATE/errata.md) | [TAM 附录 E](books/the-tam-book/appx-e-contribution-guide.md) |
| 案例：真实项目改写为脱敏案例 | [案例 Issue](.github/ISSUE_TEMPLATE/case.md) | [TAM 附录 E](books/the-tam-book/appx-e-contribution-guide.md) |
| 工具：门禁、构建、检查脚本 | 直接提 PR | [shared/tooling/README.md](shared/tooling/README.md) |

先 Issue 后 PR。口径没对齐就动笔，PR 会被退回。

## 动笔前必须过的四条

1. **脱敏是硬门槛。** 客户名、机构代号、数字、时间线一律虚构化；锚事件结构，不锚客户身份。
2. **数字带口径。** 百分比、倍数、金额、时限须标〔标准〕〔监管〕〔厂商〕〔经验值〕〔建议值〕〔案例虚构值〕之一。
3. **一处定义，三书引用。** 同一口径只在定义方写一次，其余书链接过去。不要在不拥有该事实源的书里就地改数。
4. **改目录先改 outline。** 章号是所有交叉引用的锚，先改 `00-outline.md`（BTE 为 `plan-outline.md`），再让章节文件与它对齐。

## 提交前在仓库根跑

```bash
python3 shared/tooling/content_gate.py --book all --strict
python3 shared/tooling/gen_metadata.py --check
python3 shared/tooling/xref_check.py && python3 shared/tooling/xref_check2.py
python3 shared/tooling/link_check.py
```

四条全绿才算可合并。改了文件数或标题，先跑 `gen_metadata.py --write` 与 `--index`，再跑 `--check`。

CI（`.github/workflows/quality-gate.yml`）会重跑同一组命令；本地跳过等于把返工推给下一次提交。

## 许可

提交贡献即视为同意按对应部分的许可发布：书稿内容 CC BY-NC-SA 4.0，工具代码 MIT。范围与全文见 [LICENSE](LICENSE)。

案例类贡献默认以机构代号匿名化署名，以保护来源。
