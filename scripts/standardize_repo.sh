#!/bin/bash

# Standardization Setup Script
# Use this to quickly apply global standards to any new repository.

echo "🚀 Starting Repository Standardization..."

# 1. Create Governance Directory
mkdir -p Documentation/Governance

# 2. Deploy Standards Files
# These are copied from the latest standards in sonotheia-enhanced
cat <<EOF > Documentation/Governance/AGENT_REFORMATTING_GUIDELINES.md
$(cat /Volumes/Treehorn/Gits/sonotheia-enhanced/Documentation/Governance/AGENT_REFORMATTING_GUIDELINES.md)
EOF

cat <<EOF > Documentation/Governance/AGENT_BEHAVIORAL_STANDARDS.md
$(cat /Volumes/Treehorn/Gits/sonotheia-enhanced/Documentation/Governance/AGENT_BEHAVIORAL_STANDARDS.md)
EOF

# 3. Create/Update .flake8
cat <<EOF > .flake8
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = .git,__pycache__,venv,.venv
EOF

# 4. Update root pyproject.toml
cat <<EOF > pyproject.toml
[tool.black]
line-length = 88
target-version = ["py311"]

[tool.isort]
profile = "black"
line_length = 88
EOF

# 5. Add "Priming" instructions to README.md
if ! grep -q "AGENT_BEHAVIORAL_STANDARDS" README.md; then
    echo -e "\n## Agent Instructions\nThis repository follows [Agent Behavioral Standards](Documentation/Governance/AGENT_BEHAVIORAL_STANDARDS.md). All AI agents MUST read these before performing any tasks." >> README.md
fi

echo "✅ Standardization Complete! Running 'black .' to finalize..."
black .
