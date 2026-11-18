# allen-writes · First Principles

> 由便携版 SKILL.md（`skills/allen-writes/`）并入，2026-11-18 合并，内容原样保留。

## First Principles (融合 10 个上游 Skills)

### 1. Diátaxis Discipline (from `/technical-writing`)

Every document must have a **single Diátaxis type**. No exceptions.

| Type | Purpose | Forbidden Content |
|------|---------|-------------------|
| **Tutorial** | Guide a beginner through hands-on steps to a visible outcome | Background theory, alternative methods, reference tables |
| **How-to** | Solve a specific real-world problem for an experienced user | Conceptual explanation, historical context, definitions |
| **Reference** | Authoritative description of mechanisms, concepts, data | Opinions, steps, explanations of "why" |
| **Explanation** | Clarify background, design choices, and trade-offs | Commands, step-by-step procedures, reference data |

**Type declaration rule**: First line of every `.md` file must be:
```markdown
<!-- Diátaxis: {Explanation|How-to|Reference|Tutorial} -->
```

**Single-type enforcement**: If a draft contains content for two or more types, split into separate files. Never merge types.

### 2. Agent-Facing Doc Optimization (from `/writing-for-agents`)

When writing documents that an AI agent will read (AGENTS.md, SKILL.md, prompts):

- **Default action is deletion, not explanation**: Don't explain what the agent already knows
- **Predictable behavior change**: Every instruction must change what the agent does, not what it knows
- **Context load vs Turn load**: 
  - Context load: Always-loaded material (AGENTS.md rules, SKILL.md frontmatter)
  - Turn load: Single-trigger material (skill body, inline instructions)
  - Optimize for low Context load; move mechanics to Turn load

### 3. Skill Craft (from `/write-skills`)

When creating or editing skills:

- **Trigger from the description**: The `description` field is the only content read before the skill loads. Put trigger conditions there, not in the body.
- **Spend tokens like they are scarce**: State direction; let the model figure out implementation. A wrapper skill can be two sentences.
- **Add mechanics only after demonstrated failure**: Don't preemptively add rules for problems that haven't happened.

### 4. Style Enforcement (from `/agent-style`)

Enforce 21 technical writing rules at generation time (not as post-hoc linting):

**Structural Rules:**
- RULE-01: Curse of Knowledge — Never say "obviously," "clearly," "simply." If it were obvious, it wouldn't need explanation.
- RULE-H: Citation Discipline — Every claim needs a source. If you can\'t cite it, don\'t write it.
- RULE-02: Active Voice Default — Passive voice is only for when the actor is genuinely unknown or irrelevant.
- RULE-03: Short Sentences — If a sentence has more than 25 Chinese characters or 20 English words, break it.

**AI-Specific Anti-Patterns (from field observation):**
- ❌ "In today\'s rapidly evolving world..." → ✅ Delete. Start with the substance.
- ❌ "It\'s important to note that..." → ✅ Delete. Say the thing directly.
- ❌ "By leveraging cutting-edge technology..." → ✅ Name the technology. Say what it does.
- ❌ Over-polite hedging: "I would suggest that perhaps you might consider..." → ✅ "Use X. It handles Y."
- ❌ Empty summarization: "In summary, this chapter has discussed..." → ✅ Delete. Let the content speak.
- ❌ Noun stacks: "utilization of the optimization methodology" → ✅ "use the optimization method"

### 5. Structured Output (from `/bmad-agent-tech-writer`)

When generating complex content:

- **Audience calibration**: Adapt depth based on target audience (technical/executive/operational)
- **Persistent fact loading**: Maintain a running glossary of terms. Cross-check against `appx-a-glossary.md`
- **Multi-format support**: Use tables for comparisons, Mermaid for diagrams, code blocks for configurations
- **Language consistency**: Default to Chinese (full-width punctuation) with English terms for technology names

### 6. Research-to-Delivery (from `/report-writing`)

When transforming research into written content:

- **Input requirements**: Raw research notes, target audience, intended document type
- **Process**:
  1. Organize raw notes into thematic buckets
  2. Draft the narrative (explanation) or procedure (how-to)
  3. Insert evidence at claim points
  4. Add cross-references to related chapters/appendices
  5. Tag with source and date for time-sensitive claims

### 7. De-Slopping (from `/unslop`)

Every draft must pass the de-slopping filter before being considered final:

- **Scan for AI flavor**: Run a pass to detect and remove:
  - Generic opening paragraphs ("In the realm of...")
  - Excessive signposting ("First, we will... Then, we will...")
  - Unsubstantiated superlatives ("revolutionary," "game-changing," "unprecedented")
  - Circular definitions ("X is a process of processing X")
  - Hallucinated citations or statistics
- **Replace with**: Concrete facts, specific examples, quantified claims
- **Tone check**: Would a senior engineer say this in a postmortem? If not, rewrite.

### 8. Doc Lifecycle Automation (from software documentation skills)

When maintaining the repository:

- **README**: Reflect current directory structure and build instructions
- **Changelog**: Summarize commit diffs per release
- **Docstrings**: Document all public functions in `shared/tooling/` and tools
- **Onboarding**: Keep contributor setup steps tested and current

### 9. Meta-Skill Design (from `/skill-creator`)

When creating new skills for this project:

1. **Discover**: Identify repeated workflows (e.g., "generate a checklist for each chapter")
2. **Analyze**: Define boundaries — what triggers it, what doesn\'t
3. **Design**: Inputs, outputs, and behavioral constraints. Keep it under 300 tokens.
4. **Validate**: Test with 3 different scenarios before finalizing

### 10. Quality Audit (from `/grill-with-docs`)

Before declaring any content complete:

- **Consistency**: Terminology matches `appx-a-glossary.md`; template numbers match the `tpl-*.md` files at book root
- **Accuracy**: Claims have sources; numbers add up; dates are realistic
- **Freshness**: No stale references to deprecated processes or outdated regulations
- **Completeness**: Every section promised in the outline is present
- **Cross-reference integrity**: Internal links point to existing files/sections

