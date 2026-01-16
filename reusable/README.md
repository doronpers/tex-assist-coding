# Reusable Learning Resources

This directory contains organized, easily accessible learning resources that can be repurposed across multiple repositories.

## 📚 Quick Access

### Philosophy & Framework
- **[Dark Horse Approach](philosophy/dark-horse-approach.md)** - Individualized learning framework
- **[Micro-Motives Framework](philosophy/micro-motives-framework.md)** - Understanding what energizes learners

### Learning Paths
- **[Complete Beginner Path](paths/complete-beginner-path.md)** - Month-by-month roadmap for absolute beginners
- **[Technical Leader Learning](paths/technical-leader-learning.md)** - Path for managers learning to code

### Exercises
- **[Discover Your Micro-Motives](exercises/discover-your-micro-motives.md)** - Self-discovery exercise

### Templates
- **[Learning Journal](templates/learning-journal.md)** - Progress tracking template
- **[Pull Request Description](templates/pull-request-description.md)** - PR template
- **[Project README](templates/project-readme.md)** - README template

### Guides
- **[GitHub Basics](guides/github-basics/)** - Beginner-friendly GitHub documentation
- **[AI Tools](guides/ai-tools/)** - AI coding tools guide
- **[Workflow Building](guides/workflow-building/)** - Personal workflow development

## 🎯 How to Use in Other Repositories

### Option 1: Copy Specific Files
```bash
# Copy just what you need
cp tex-assist-coding/reusable/philosophy/dark-horse-approach.md \
   your-repo/documentation/learning-philosophy.md
```

### Option 2: Copy Entire Sections
```bash
# Copy a whole section
cp -r tex-assist-coding/reusable/guides/github-basics \
      your-repo/documentation/guides/
```

### Option 3: Reference from Another Repo
```markdown
For learning resources, see [tex-assist-coding reusable content](https://github.com/doronpers/tex-assist-coding/tree/main/reusable)
```

### Option 4: Symlink (For Active Development)
```bash
# From another repo
ln -s ../../tex-assist-coding/reusable your-repo/documentation/learning-resources
```

## 📁 Directory Structure

```
reusable/
├── README.md                    # This file
├── PORTABILITY.md              # Detailed portability guide
├── philosophy/                 # Core learning philosophy
│   ├── dark-horse-approach.md
│   └── micro-motives-framework.md
├── paths/                      # Learning path templates
│   ├── complete-beginner-path.md
│   └── technical-leader-learning.md
├── exercises/                  # Self-discovery exercises
│   └── discover-your-micro-motives.md
├── templates/                  # Reusable templates
│   ├── learning-journal.md
│   ├── pull-request-description.md
│   └── project-readme.md
└── guides/                     # Beginner-friendly guides
    ├── github-basics/         # (symlink to documentation/01-github-basics)
    ├── ai-tools/              # (symlink to documentation/02-ai-tools)
    └── workflow-building/     # (symlink to documentation/03-workflow-building)
```

## 🔗 Source Locations

These files are organized here for easy access, but their source locations are:

- **Philosophy**: `documentation/dark-horse-approach.md`
- **Paths**: `scenarios/`
- **Exercises**: `exercises/`
- **Templates**: `templates/`
- **Guides**: `documentation/01-github-basics/`, `documentation/02-ai-tools/`, `documentation/03-workflow-building/`

## 📝 Notes

- Most items are **symlinks** to the original files - edit the originals, changes appear here
- Templates are **copied** (not symlinked) for independent modification
- When copying to other repos, update relative paths in markdown files
- Keep this directory as the **single organized access point** for reusable content

## 🚀 Quick Copy Commands

```bash
# Copy everything
cp -r tex-assist-coding/reusable your-repo/documentation/learning-resources

# Copy just philosophy
cp -r tex-assist-coding/reusable/philosophy your-repo/documentation/learning/

# Copy just templates
cp tex-assist-coding/reusable/templates/*.md your-repo/templates/
```

See [PORTABILITY.md](PORTABILITY.md) for detailed portability instructions.
