---
description: Pre-task instructions for all agents working on tex-assist-coding
---

# Before Starting Any Task

Before making ANY changes, read the `AGENT_KNOWLEDGE_BASE.md` file in the repository root.

```bash
cat AGENT_KNOWLEDGE_BASE.md
```

This file contains critical instructions including:

1. Prime directives (non-negotiable rules)
2. Coding standards (black, flake8, type hints)
3. Project architecture overview
4. Development workflows
5. Testing requirements

## Verification

After completing your task, run the pre-commit checklist:

```bash
# Format code
black .

# Check linting
flake8 .

# Check YAML
yamllint .

# Run all pre-commit hooks (final check)
pre-commit run --all-files
```

**CRITICAL**: See `.agent/workflows/pre-commit-checklist.md` for detailed requirements to prevent commit failures.
