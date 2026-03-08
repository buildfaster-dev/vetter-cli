# Plan: Improve CLI Help Text & README Clarity

## Context

Users expect `--repo-url` to clone a remote repo. In reality, it's metadata for the report header. The CLI help text doesn't make this clear, leading to confusion. The `analyze` command description and option help strings need to be more explicit.

**Scope**: Documentation-only. No behavior changes.

---

## 1. Spec — Define the change

### Problem

- `--repo-url` help says "Repository URL for report header" — users expect it to clone
- `--output` help doesn't show the default value
- `analyze` docstring is generic ("a candidate's Git repository")
- README explains the metadata nature but it's easy to miss

### Files to change

| File | Change |
|------|--------|
| `src/vetter/cli.py` | Improve help strings for all options and `analyze` docstring |
| `README.md` | Make "local repos only" clearer, improve option descriptions |
| `CLAUDE.md` | Update CLI Interface section to match |

---

## 2. Implement — Write code following existing patterns

### cli.py

```python
# analyze docstring
"Analyze a candidate's Git repository and generate a report."
→ "Analyze a local Git repository and generate a report."

# --candidate help
"Candidate name for report header."
→ "Candidate name (report header only, does not affect analysis)."

# --repo-url help
"Repository URL for report header."
→ "Repository URL (report header only — does not clone)."

# --output help
"Output file path."
→ "Output file path (default: ./report.md)."

# --model stays the same
```

### README.md

- Add explicit note above Usage: "Vetter analyzes local repositories only. Clone the repo first, then point Vetter at it."
- Update Options table descriptions to match CLI help

### CLAUDE.md

- Update CLI Interface option descriptions to match

---

## 3. Test — Add/update tests

No new tests needed — documentation-only change.

```bash
uv run pytest -v              # All 52 tests still pass
uv run vetter analyze --help  # Verify improved help output
```

---

## 4. Review — Verify against acceptance criteria

- [ ] `vetter analyze --help` clearly states local-only, no-clone behavior
- [ ] `--repo-url` help explicitly says "does not clone"
- [ ] README has visible "local repos only" note
- [ ] All 52 tests pass
- [ ] No behavior changes — only text
