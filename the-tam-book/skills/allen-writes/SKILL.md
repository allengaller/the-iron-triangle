# allen-writes

## Frontmatter

```json
{
  "name": "allen-writes",
  "description": "The TAM Book unified writing skill. Activate when the user needs to write, revise, or audit technical content for the-tam-book repository. Covers Diátaxis typing, agent-facing doc optimization, depth and pyramid expression, style enforcement, de-slopping, and multi-stage quality assurance.",
  "version": "1.1.0",
  "author": "Allen Galler",
  "project": "the-tam-book"
}
```

## When to Activate

Trigger this skill when any of the following conditions are met:

- User asks to write, draft, or edit a chapter/appendix for the-tam-book
- User pastes raw text and asks for structural or stylistic improvement
- User requests Diátaxis alignment for a document
- User asks to remove "AI flavor" or "AI slop" from a draft
- User requests terminology consistency check across chapters
- User asks to generate a checklist, template, or reference table
- User requests review of AGENTS.md, SKILL.md, or other agent-facing docs
- User mentions any of: Diátaxis, /unslop, /agent-style, /grill-with-docs, /writing-for-agents

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
- **Docstrings**: Document all public functions in `/scripts/` and tools
- **Onboarding**: Keep contributor setup steps tested and current

### 9. Meta-Skill Design (from `/skill-creator`)

When creating new skills for this project:

1. **Discover**: Identify repeated workflows (e.g., "generate a checklist for each chapter")
2. **Analyze**: Define boundaries — what triggers it, what doesn\'t
3. **Design**: Inputs, outputs, and behavioral constraints. Keep it under 300 tokens.
4. **Validate**: Test with 3 different scenarios before finalizing

### 10. Quality Audit (from `/grill-with-docs`)

Before declaring any content complete:

- **Consistency**: Terminology matches `appx-a-glossary.md`; template numbers match `templates/` directory
- **Accuracy**: Claims have sources; numbers add up; dates are realistic
- **Freshness**: No stale references to deprecated processes or outdated regulations
- **Completeness**: Every section promised in the outline is present
- **Cross-reference integrity**: Internal links point to existing files/sections

## Unified Writing Workflow

When activated, follow this 5-phase workflow:

### Phase 1: Type Determination (Diátaxis)

1. Ask or infer: What is the single Diátaxis type of this document?
2. If the user is unclear, ask: "Is this meant to teach someone to do something (Tutorial), solve a specific problem (How-to), look up facts (Reference), or understand why something works (Explanation)?"
3. Declare the type and enforce single-type discipline for the rest of the session.

### Phase 2: Structure Scaffold

Based on the declared type, scaffold the document:

**Tutorial:**
- Prerequisites
- Step 1 → Step N (each with expected outcome)
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

### Phase 3: Content Generation

Generate content while enforcing:

- **Style rules** (Phase 4): Active voice, short sentences, no AI slop
- **Depth**: Short sentences reduce reading load; they do not justify thin content or insufficient length
- **Point-first structure**: State each section's conclusion in its first paragraph, then present grouped supporting points, evidence, examples, and boundaries
- **Pyramid expression**: Place one governing idea above two to four comparable, distinct supporting points; order each level by time, structure, or importance
- **Progressive development**: Move from known to unknown and simple to complex; define terms before use and do not skip causal or operational steps
- **Complete development**: For every key point, explain the claim, why it holds, a concrete example or evidence, and its boundary or application; never substitute a bare list or aphorisms for an argument
- **Substantive expansion**: When a draft is too short, add mechanisms, scenarios, comparisons, counterexamples, and edge cases; never pad through repetition or generic background
- **Terminology**: First use = "中文（English, Abbreviation)"; subsequent = abbreviation or Chinese
- **Evidence**: Sources and dates for time-sensitive claims
- **Cross-references**: Use `[chXX](file.md)` or `[appx-X](file.md)` format

### Phase 4: Style Enforcement & De-Slopping

Run the generated content through these filters:

1. **Active voice check**: Highlight all instances of "被" (Chinese passive) and rewrite to active
2. **Sentence length check**: Flag sentences > 25 Chinese characters
3. **AI slop scan**: Remove generic openings, empty summaries, circular definitions
4. **Superlative audit**: Replace "revolutionary/game-changing" with specific capabilities
5. **Citation check**: Ensure every claim has a source or is marked `[citation needed]`
6. **Depth check**: Expand bare claims and lists with mechanisms, examples or evidence, and boundaries; remove any repetition added only to increase length
7. **Pyramid check**: Verify point-first sections, comparable supporting points, and progression without logical leaps

### Phase 5: Quality Audit

Before delivery, verify:

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

- v1.1.0 (2026-10-25): Add depth, progressive development, point-first organization, and pyramid expression requirements.
- v1.0.0 (2026-10-25): Initial fusion of /technical-writing, /writing-for-agents, /write-skills, /agent-style, /bmad-agent-tech-writer, /report-writing, /unslop, doc lifecycle automation, /skill-creator, and /grill-with-docs.
