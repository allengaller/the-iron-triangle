---
name: allen-writes
description: Unified writing skill for the-iron-triangle repository. Enforces Diátaxis document typing, agent-facing doc optimization, substantive development, pyramid expression, style rules, de-slopping, and multi-stage quality assurance. Use when writing or editing chapters, appendices, checklists, templates, or AGENTS.md for any of the three books (TAM / SA / BTE) or repo-level documents. Triggered by mentions of Diátaxis, writing style, AI slop, thin or overly concise content, terminology consistency, or when the user asks to write, draft, revise, or audit technical content in the-iron-triangle repository.
---

# allen-writes

配套文件：

| 文件 | 内容 |
| --- | --- |
| [examples.md](examples.md) | 逐体裁的写法示例与反例 |
| [reference.md](reference.md) | 21 条技术写作规则的完整清单 |
| [first-principles.md](first-principles.md) | 十个上游方法的第一性原理（2026-11-18 由便携版并入） |

## When to Activate

Activate when the user is working with content in `the-iron-triangle` repository and any of these apply:

- Writing, drafting, or editing a chapter or appendix
- Requesting structural or stylistic improvement of existing text
- Mentioning Diátaxis, document types, or content organization
- Asking to remove AI flavor, AI slop, or generic writing patterns
- Requesting terminology consistency checks across chapters
- Generating checklists, templates, or reference tables
- Reviewing or updating AGENTS.md, SKILL.md, or other agent-facing documents

## Phase 1: Determine Diátaxis Type

Every document must have exactly one type. Ask if unclear.

| Type | Purpose | Forbidden Content |
|------|---------|-------------------|
| **Tutorial** | Guide a beginner through hands-on steps to a visible outcome | Background theory, alternative methods |
| **How-to** | Solve a specific real-world problem | Conceptual explanation, historical context |
| **Reference** | Authoritative description of mechanisms, concepts, data | Opinions, steps, explanations of "why" |
| **Explanation** | Clarify background, design choices, and trade-offs | Commands, step-by-step procedures, reference data |

**Type declaration**: First line of every `.md` file must be:
```markdown
<!-- Diátaxis: {Explanation|How-to|Reference|Tutorial} -->
```

If a draft contains content for two or more types, split into separate files.

## Phase 2: Scaffold Structure

Based on the declared type, scaffold the document:

**Tutorial:**
- Prerequisites
- Step 1 -> Step N (each with expected outcome)
- Verification: How to know it worked
- Common errors and recovery

**How-to:**
- Goal statement
- Prerequisites
- Procedure (numbered, imperative voice)
- Expected result / validation
- Troubleshooting (if applicable)

**Reference:**
- Definition / scope
- Taxonomy / categories
- Attribute tables
- Cross-references to related entries

**Explanation:**
- Context / why it matters
- Core concept(s)
- Causal chain or mechanism
- Trade-offs and edge cases
- Common misconceptions

## Phase 3: Enforce Writing Style

### Active Voice
- Rewrite passive "被" constructions to active voice
- Exception: actor is genuinely unknown or irrelevant

### Sentence Length
- Chinese sentences > 25 characters: break them
- English sentences > 20 words: break them
- Short sentences reduce reading load; they do not justify thin content or insufficient length.

### Enumeration Punctuation
- An enumeration introduced by a count ("五项"、"六步"、"四条红线") must list that many items before its full stop. Never insert a 。 mid-list: 「五项：A、B、C。D、E。」 is a defect, not a stylistic choice — the reader stops at the 。 and loses the remaining items.
- The test is arithmetic, not punctuation counting: declared count vs actual items between the colon and the first full stop. Short of the declared count means the list was truncated.
- This is a `content_gate.py` block item (`broken_enums`). If it fires, fix the text; do not adjust the rule.

### Depth, Progression, and Pyramid Expression
- **Lead with the point**: State the section's conclusion in its first paragraph. Follow with grouped supporting points, then evidence, examples, and boundaries.
- **Build a pyramid**: Place one governing idea above two to four supporting points. Keep points at the same level comparable and distinct. Order them by time, structure, or importance.
- **Progress step by step**: Move from known to unknown and from simple to complex. Define terms before use. Do not skip causal or operational steps between a claim and its conclusion.
- **Develop every key point**: Explain the claim, why it holds, a concrete example or evidence, and its boundary or application. Do not replace an argument with a bare list or a string of aphorisms.
- **Expand with substance**: When a draft is too short, add mechanisms, scenarios, comparisons, counterexamples, and edge cases. Never pad by repeating conclusions or adding generic background.

### AI Slop Removal
Remove these patterns on sight:
- Generic openings: "In today's rapidly evolving world..." -> Delete. Start with substance.
- Hedge phrases: "It's important to note that..." -> Delete. Say the thing directly.
- Empty summaries: "In summary, this chapter has discussed..." -> Delete. Let content speak.
- Unsubstantiated superlatives: "revolutionary", "game-changing", "unprecedented" -> Replace with specific capabilities
- Over-polite hedging: "I would suggest that perhaps you might..." -> "Use X. It handles Y."
- Noun stacks: "utilization of the optimization methodology" -> "use the optimization method"
- Circular definitions: "X is a process of processing X" -> Replace with concrete meaning

### Terminology
- First use: "中文（English, Abbreviation)"
- Subsequent: abbreviation or Chinese
- Cross-reference format: `[chXX](file.md)` or `[appx-X](file.md)`

## Phase 4: Run Quality Audit

Before declaring content complete, verify:

- [ ] Single Diátaxis type maintained throughout
- [ ] Type declared in first-line comment
- [ ] Terminology matches `appx-a-glossary.md`
- [ ] Template references use "模板 XX" format (two digits, zero-padded)
- [ ] P-prefix references include context qualifier (e.g., "流程 P5")
- [ ] Sources and dates attached to time-sensitive claims
- [ ] No AI slop (empty summaries, generic openings, over-polite hedging)
- [ ] Each section leads with its key point and organizes supporting points into a clear pyramid
- [ ] Ideas progress without logical leaps; terms and prerequisites appear before use
- [ ] Every key point has sufficient explanation, evidence or examples, and boundaries; brevity has not made the content thin
- [ ] Cross-references to existing files only (no dangling links)
- [ ] Chinese text uses full-width punctuation; English terms preserved for technology names
- [ ] For How-to/Tutorial: Includes validation step
- [ ] For Reference: Includes definition, taxonomy, and cross-references
- [ ] For Explanation: Includes causal chain and at least one misconception

## Agent-Facing Doc Rules

When writing documents that an AI agent will read (AGENTS.md, SKILL.md, prompts):

- **Default action is deletion, not explanation**: Don't explain what the agent already knows
- **Predictable behavior change**: Every instruction must change what the agent does
- **Context load vs Turn load**: Optimize for low Context load; move mechanics to Turn load

## Output Format

When generating content, wrap in:

```markdown
<!-- Diátaxis: {Type} -->
<!-- Source: {original prompt or research notes} -->
<!-- Generated by: allen-writes v1.1.0 -->

{content}

---

## Quality Audit Trail

- Type check: {pass / fail - explain}
- Style check: {pass / fail - explain}
- Terminology check: {pass / fail - explain}
- Cross-reference check: {pass / fail - explain}
```

## Version History

- v1.2.0 (2026-11-18): 合并便携版 `skills/allen-writes/SKILL.md` 的 First Principles 段为 `first-principles.md`，单一技能根收敛至 `.qoder/skills/allen-writes/`。
- v1.1.0 (2026-10-25): Add depth, progressive development, point-first organization, and pyramid expression requirements.
- v1.0.0 (2026-10-25): Initial fusion of /technical-writing, /writing-for-agents, /write-skills, /agent-style, /bmad-agent-tech-writer, /report-writing, /unslop, /skill-creator, and /grill-with-docs.
