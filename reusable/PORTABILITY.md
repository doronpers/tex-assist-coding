# Portability Guide

This directory is designed to be easily reused in other repositories.

## Quick Copy Commands

### Copy Everything
```bash
cp -r tex-assist-coding/reusable your-repo/documentation/learning-resources
```

### Copy Specific Sections
```bash
# Just philosophy
cp -r tex-assist-coding/reusable/philosophy your-repo/documentation/learning/

# Just templates
cp tex-assist-coding/reusable/templates/*.md your-repo/templates/

# Just beginner guides
cp -r tex-assist-coding/reusable/guides/github-basics your-repo/documentation/guides/
```

## Link Updates Required

When copying to another repo, update:

1. **Relative paths in markdown files**
   - Old: `../documentation/01-github-basics/`
   - New: `guides/github-basics/` (or appropriate relative path)
   - Old: `../exercises/discover-your-micro-motives.md`
   - New: `exercises/discover-your-micro-motives.md`

2. **References to "tex-assist-coding"**
   - Search and replace with your repo name or remove if not relevant

3. **Repo-specific examples**
   - Update any code examples or references to match your repo's context

## Integration Examples

### In README.md
```markdown
## Learning Resources

See [Learning Resources](documentation/learning-resources/) for:
- Beginner-friendly guides
- Learning path templates
- Micro-motives discovery exercises
```

### In Documentation
```markdown
For learning philosophy, see [Dark Horse Approach](learning-resources/philosophy/dark-horse-approach.md)
```

### In Contributing Guide
```markdown
## For Beginners

If you're new to coding or this project, check out:
- [Complete Beginner Path](documentation/learning-resources/paths/complete-beginner-path.md)
- [GitHub Basics](documentation/learning-resources/guides/github-basics/)
```

## File Structure After Copying

After copying, your structure might look like:

```
your-repo/
├── documentation/
│   └── learning-resources/  # or just "learning/"
│       ├── README.md
│       ├── philosophy/
│       ├── paths/
│       ├── exercises/
│       ├── templates/
│       └── guides/
└── README.md
```

## Symlink Approach (Advanced)

For active development across multiple repos, use symlinks:

```bash
# From your-repo root
ln -s ../../tex-assist-coding/reusable documentation/learning-resources
```

**Benefits:**
- Single source of truth
- Updates propagate automatically
- No duplication

**Drawbacks:**
- Requires tex-assist-coding to be accessible
- Git doesn't track symlinks well (use git submodules if needed)

## Customization

Feel free to:
- Extract only what you need
- Modify content to match your repo's context
- Add repo-specific examples
- Combine with your existing documentation

## Maintenance

- **Primary source**: This directory (tex-assist-coding/reusable) is the authoritative source
- **Updates**: Edit files in their original locations (documentation/, scenarios/, etc.) - symlinks update automatically
- **For sono-eval copy**: The sono-eval/documentation/Learning directory is a copy/extraction - contribute improvements back here
- **Versioning**: Consider tagging versions if breaking changes occur
