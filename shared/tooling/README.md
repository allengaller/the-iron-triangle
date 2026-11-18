# shared/tooling/ — 门禁脚本与构建资源

三书的工具与构建资源合并于此（2026-11-18），书根只留 md。脚本按 `__file__` 定位仓库根，**一律在仓库根执行**，与当前目录无关。

## 内容门禁与审计（TAM 书）

| 文件 | 用途 |
| --- | --- |
| `content_gate.py` | 内容门禁：体裁、结构、八项厚度指标 |
| `claim_audit.py` | 数字断言的口径标注检查 |
| `similarity_audit.py` | 跨文件同构与文本重合审计 |
| `gen_metadata.py` | 从磁盘计算元数据回填 META 标记；`--index` 重建 `99-index.md` |
| `xref_check.py` | 章、附录、模板的交叉引用与编号校验 |
| `xref_check2.py` | 节号级引用校验 |
| `audit-crossrefs.py` | 全仓交叉引用审计（含跨书） |
| `merge_landing.py` `renumber_remap.py` `crossbook_remap.py` | 历史脚本：一次性迁移已完成，仅留档 |

```bash
python3 shared/tooling/content_gate.py --strict     # 体裁与结构破损
python3 shared/tooling/content_gate.py --report     # 内容厚度台账 → shared/review/the-tam-book/
python3 shared/tooling/claim_audit.py               # 数值断言出处
python3 shared/tooling/similarity_audit.py --report # 跨文件同构 → shared/review/the-tam-book/
python3 shared/tooling/gen_metadata.py --check      # 元数据漂移
python3 shared/tooling/xref_check.py && python3 shared/tooling/xref_check2.py  # 交叉引用
```

六命令的口径、阈值与盲区见 [`shared/governance/QUALITY-GATE.md`](../governance/QUALITY-GATE.md)。改书稿结构或重命名文件后，先跑 `gen_metadata.py --index` 重建索引，再跑其余五条。

## 阅读站构建（TAM 书）

| 文件 | 用途 |
| --- | --- |
| `build_web.py` | 构建静态阅读站到 `shared/dist/site/`，站外文件压平到 `ext/` |
| `reader.css` `reader.js` | 阅读站样式与交互 |
| `cover.html` | 阅读站封面页模板（原样拷贝为 `site/index.html`） |
| `template.html` | 阅读站页面模板，`{{ROOT}}` 等为运行时占位符 |
| `link_check.py` | 全仓相对链接校验（重构或大规模改路径后必跑） |

```bash
python3 shared/tooling/build_web.py     # 站点产物 → shared/dist/site/
python3 shared/tooling/link_check.py    # 全仓链接校验
```

## BTE 书构建与发布

| 文件 | 用途 |
| --- | --- |
| `build.sh` | 构建 HTML、EPUB、PDF 三件产物到 `shared/dist/` |
| `release.sh` | 调 `build.sh` 并打发布包 zip 到 `shared/dist/` |
| `make_cover.py` | 生成封面图（Pillow + macOS 字体，输出落在本目录） |
| `metadata.yaml` | pandoc 元数据（标题、作者、版本） |
| `style.css` | HTML／PDF 样式 |
| `header.html` | pandoc `--include-in-header` 片段 |
| `cover.png` | 封面图（1600×2400，由 `make_cover.py` 生成，出库） |

```bash
bash shared/tooling/build.sh     # HTML / EPUB / PDF
bash shared/tooling/release.sh   # 发布包 zip
```

依赖：`pandoc` 3.x、`weasyprint`（PDF）、Python 3 + Pillow（封面）、macOS 字体 Songti SC／PingFang SC（封面）。

输入：BTE 书根 `*.md` 与 `shared/00-*.md` 卷首公用篇；`build.sh` 的 `FILES` 显式列出全部输入，按「front-matter → 公用篇 → 导读 → 章节 → 附录 → 结语」拼接。改公用篇等于三书同时改，改完须重跑构建。

产物：

| 文件 | 说明 |
| --- | --- |
| `shared/dist/bte-book.html` | 单页 HTML，CSS 已内嵌 |
| `shared/dist/bte-book.epub` | EPUB 3，含封面、目录与分章 |
| `shared/dist/bte-book.pdf` | A4 PDF，目录带页码，章节分页 |
| `shared/dist/bte-book-v1.0.zip` | 发布包：三件产物 + 封面、元数据、README、CHANGELOG、发布说明、LICENSE |

发布包内的 README 与发布说明取自 `shared/review/the-bte-book/` 的 `release-readme.md` 与 `release-v1.0.md`；发布文档属归档，不入书根。

单独生成封面（在仓库根执行，输出落在本目录）：

```bash
python3 -I shared/tooling/make_cover.py
```

## 说明

- HTML 通过 `<base href="../">` 让章节链接指回仓库中的 Markdown 源文件。
- EPUB 是阅读版，跨书与公用卷链接可能指向仓库路径，不保证在阅读器内可跳转。
- PDF 由 WeasyPrint 生成，使用 A4 与中文字体；目录带页码，章节自动分页。
- 构建时的 `zh-CN` 翻译警告不影响输出。
- 发布前请按 [`shared/review/`](../review/README.md) 下的发布清单逐项检查。

## 版本

- v0.1（2026-11-03）：BTE 首版构建。HTML、EPUB、封面生成。
- v0.2（2026-11-18）：BTE 脚本与资源合并到 `tooling/`，输入改为书根扁平文件名。
- v0.3（2026-11-18）：三书工具合并到 `shared/tooling/`，产物统一到 `shared/dist/`，命令改在仓库根执行。
