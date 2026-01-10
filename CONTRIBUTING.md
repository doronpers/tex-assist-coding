# Contributing to AI-Assisted Coding Guide

Thank you for your interest in contributing! This repository is a community learning resource, and we welcome improvements, corrections, and new content.

## How to Contribute

### 🐛 Report Issues

Found something confusing, incorrect, or broken?

1. **Check existing issues** - Someone might have already reported it
2. **Open a new issue** with:
   - Clear title describing the problem
   - Which file or section has the issue
   - What's wrong or confusing
   - Suggestions for improvement (if you have any)

**Good issue titles:**

- "Typo in documentation/01-github-basics/branches-and-commits.md"
- "Example in Hello API doesn't work - missing import"
- "Analogy in 'Understanding Repositories' is confusing"

### ✨ Suggest Improvements

Have an idea to make something better?

1. **Open an issue** describing:
   - What you want to improve
   - Why it would help learners
   - Your proposed approach

2. **Discuss first** for big changes
   - New sections or major rewrites
   - Structural changes
   - New example projects

### 📝 Fix Documentation

**Small fixes (typos, clarity, formatting):**

- Just open a PR directly!
- No need for an issue first

**Larger improvements:**

- Open an issue to discuss first
- Then submit a PR

### 🎨 Add Examples or Exercises

**We love new content!** Especially:

- Working code examples
- Hands-on exercises
- Real-world scenarios
- Pattern demonstrations

**Before creating:**

1. Check if something similar exists
2. Open an issue to discuss your idea
3. Follow our content guidelines (below)

### 💻 Add Code

**Code contributions should:**

- Work out of the box
- Include clear comments
- Follow the repository's style
- Be tested (if applicable)
- Include a README explaining it

## Content Guidelines

### Tone and Style

**DO:**

- ✅ Use plain, conversational language
- ✅ Explain jargon immediately
- ✅ Use real-world analogies
- ✅ Be encouraging and supportive
- ✅ Normalize mistakes and confusion
- ✅ Provide multiple learning paths

**DON'T:**

- ❌ Use phrases like "obviously," "simply," "just"
- ❌ Assume prior knowledge
- ❌ Make learners feel behind
- ❌ Use unexplained technical jargon
- ❌ Skip steps in explanations

### Content Structure

Every documentation file should have:

1. **Clear Title** - What this teaches
2. **Introduction** - What you'll learn, why it matters
3. **Prerequisites** - What you need to know first (if anything)
4. **Main Content** - The actual teaching
5. **Examples** - Concrete illustrations
6. **Common Questions** - FAQ section
7. **Next Steps** - Where to go from here

### Code Examples

**All code examples must:**

- Be complete and runnable
- Include comments explaining key parts
- Show the output or result
- Handle errors appropriately
- Use meaningful variable names
- Follow modern best practices

**Example of good code:**

```python
def calculate_total_price(items: list[dict]) -> float:
    """
    Calculate total price for shopping cart.
    
    Args:
        items: List of item dictionaries with 'price' key
        
    Returns:
        Total price as float
        
    Raises:
        ValueError: If items list is empty
    """
    if not items:
        raise ValueError("Cannot calculate total for empty cart")
    
    # Sum up all item prices
    total = sum(item['price'] for item in items)
    return round(total, 2)  # Round to 2 decimal places

# Example usage
cart = [
    {'name': 'Book', 'price': 12.99},
    {'name': 'Pen', 'price': 1.50}
]
total = calculate_total_price(cart)
print(f"Total: ${total}")  # Output: Total: $14.49
```

### Example Projects

**Should include:**

- `README.md` - What it is, what you'll learn
- `HOW_TO_BUILD.md` - Step-by-step guide with AI prompts
- Complete working code
- `requirements.txt` or equivalent
- `.gitignore` for the project type
- Optional: Tests

### Exercises

**Should include:**

- Clear goal and time estimate
- Difficulty level
- Prerequisites
- Step-by-step instructions
- Success criteria (checklist)
- Reflection questions
- Common mistakes section
- Next steps

## Pull Request Process

### 1. Fork and Clone

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR-USERNAME/tex-assist-coding.git
cd tex-assist-coding
```

### 2. Create a Branch

```bash
git checkout -b your-descriptive-branch-name
```

**Good branch names:**

- `fix-typo-in-readme`
- `add-database-pattern-example`
- `improve-git-basics-explanation`

### 3. Make Your Changes

- Follow the content guidelines above
- Keep changes focused (one thing per PR)
- Test any code you add
- Check spelling and grammar

### 4. Commit Your Changes

```bash
git add .
git commit -m "Descriptive commit message"
```

**Good commit messages:**

- "Fix typo in Understanding Repositories"
- "Add example for email validation pattern"
- "Improve explanation of decorators with analogy"
- "Add exercise for practicing branches"

### 5. Push and Create PR

```bash
git push origin your-branch-name
```

Then on GitHub:

1. Go to the original repository
2. Click "Pull Request"
3. Fill in the PR description (see template below)
4. Click "Create Pull Request"

### PR Description Template

```markdown
## What This PR Does

Brief description of your changes

## Type of Change

- [ ] Bug fix (typo, broken link, incorrect info)
- [ ] Content improvement (better explanation, new example)
- [ ] New content (new file, new section, new example)
- [ ] Other (describe):

## Checklist

- [ ] I've read the contributing guidelines
- [ ] My changes follow the content style
- [ ] I've tested any code I added
- [ ] I've checked for typos and grammar
- [ ] I've added myself to CONTRIBUTING.md (if this is my first contribution)

## Additional Context

Any other relevant information
```

## Review Process

1. **Maintainers will review** within a few days
2. **May request changes** - that's normal!
3. **Make requested changes** and push again
4. **Once approved**, a maintainer will merge

## Content Ideas We're Looking For

### High Priority

- [ ] More complete example projects
- [ ] More exercises for each section
- [ ] More scenario files (career changer, founder, hobbyist)
- [ ] Remaining workflow building files
- [ ] Pattern examples with full code
- [ ] Video tutorials (links or embedded)

### Medium Priority

- [ ] Advanced topics (documentation/05-advanced)
- [ ] More templates
- [ ] Troubleshooting guides
- [ ] FAQ sections
- [ ] Glossary of terms

### Nice to Have

- [ ] Translations to other languages
- [ ] Dark mode toggle
- [ ] Interactive quizzes
- [ ] Cheat sheets (printable)

## Questions?

- **Open an issue** - Label it "question"
- **Start a discussion** - In the Discussions tab
- **Ask maintainers** - Tag us in an issue or PR

## Recognition

All contributors will be:

- Added to the Contributors section below
- Credited in their PRs/issues
- Appreciated publicly!

## Code of Conduct

### Our Standards

- Be kind and respectful
- Welcome beginners warmly
- Provide constructive feedback
- Celebrate others' contributions
- Assume good intentions

### Not Acceptable

- Harassment or discrimination
- Dismissive or condescending comments
- Gatekeeping ("you should already know this")
- Spam or self-promotion
- Any behavior that makes others feel unwelcome

### Reporting

If you experience or witness unacceptable behavior:

1. Contact repository maintainers
2. All reports will be taken seriously
3. We'll respond promptly and fairly

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Thank You

Every contribution, no matter how small, makes this resource better for learners worldwide. Thank you for taking the time to help! 🙏

---

**Ready to contribute?** Pick an issue labeled "good first issue" to get started!

---

## Contributors

Thank you to everyone who has contributed to making this learning resource better! 🙏

### Project Creator

**Doron Pers** - [@doronpers](https://github.com/doronpers)

- Created and maintains the AI-Assisted Coding Guide
- Vision: Make AI-assisted development accessible to complete beginners

### Contributors List

<!-- Contributors will be added here as they contribute -->

*Your name could be here! Make your first contribution today.*
