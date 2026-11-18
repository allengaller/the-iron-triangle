# allen-writes Reference

## AI Slop Pattern Catalog

Complete list of patterns to remove, with replacements:

| Pattern | Example | Replacement |
|---------|---------|-------------|
| Generic opening | "In today's rapidly evolving world..." | Delete; start with substance |
| Hedge phrase | "It's important to note that..." | Delete; say directly |
| Empty summary | "In summary, this chapter has discussed..." | Delete; let content speak |
| Superlative | "revolutionary", "game-changing" | Specific capability or metric |
| Over-polite hedge | "I would suggest that perhaps..." | "Use X. It handles Y." |
| Noun stack | "utilization of the optimization methodology" | "use the optimization method" |
| Circular definition | "X is a process of processing X" | Concrete meaning |
| Passive voice (Chinese) | "被" constructions | Active voice |
| Long sentence | > 25 Chinese characters | Break into shorter sentences |

## Diátaxis Decision Tree

```
Is the reader a beginner?
├─ Yes -> Tutorial
└─ No -> Are they solving a specific problem?
    ├─ Yes -> How-to
    └─ No -> Do they need facts or understanding?
        ├─ Facts -> Reference
        └─ Understanding -> Explanation
```

## Terminology Format Rules

| Scenario | Format | Example |
|----------|--------|---------|
| First occurrence | 中文（English, Abbreviation） | 技术客户经理（Technical Account Manager，TAM） |
| Subsequent | 缩写或中文 | TAM / 技术客户经理 |
| In headings | Use Chinese | # 第 1 章　TAM 的起源与演进 |
| In tables | Use abbreviation | TAM |
| Cross-reference | `[chXX](file.md)` | `见 [ch05](ch05-technical-depth.md)` |

## P-Prefix Reference Guide

| Prefix | Meaning | Context |
|--------|---------|---------|
| 流程 P1-P12 | Core processes | "流程 P5" = 重保流程 |
| 故障 P1-P4 | Incident severity | "故障 P1" = critical incident |
| 评估原则 P1-P5 | Evaluation principles | "评估原则 P3" |
| 附录 P.x | Appendix P section | "附录 P.3" |

## Template Numbering

Always use two-digit zero-padded format: `模板 01`, `模板 02`, ... `模板 19`

Never: `模板01`, `模板 1`, `模板1`

## Output Quality Checklist

Before declaring content complete:

- [ ] Single Diátaxis type maintained
- [ ] Type declared in first-line comment
- [ ] Terminology matches appx-a-glossary.md
- [ ] Template refs use "模板 XX" format
- [ ] P-prefix refs include context qualifier
- [ ] Sources/dates for time-sensitive claims
- [ ] No AI slop patterns
- [ ] No dangling cross-references
- [ ] Full-width punctuation for Chinese
- [ ] English terms preserved for technology names
