# Exercise: Create Your First Branch

**Goal:** Learn to create and use git branches by making a safe experimental change.

**Time:** 15-20 minutes

**Difficulty:** ⭐ Beginner

## What You'll Learn

- How to create a branch
- How to switch between branches
- Why branches are useful
- How to merge a branch

## Prerequisites

- Git installed
- A GitHub account
- Completed [Exercise 01](01-create-repo.md)

## Why This Matters

Branches let you:
- Experiment safely
- Work on features without breaking main code
- Collaborate with others
- Try things and throw them away if needed

**Think of branches as parallel universes for your code!**

## The Task

You'll create a branch, make a change, and merge it back.

---

## Step 1: Check Your Current Branch

```bash
git branch
```

You should see:
```
* main
```

The `*` means you're on the `main` branch.

---

## Step 2: Create a New Branch

```bash
git checkout -b add-description
```

This creates a new branch called `add-description` and switches to it.

**Verify it worked:**
```bash
git branch
```

You should see:
```
  main
* add-description
```

---

## Step 3: Make a Change

Edit your README.md file. Add a description:

```markdown
# My First Repository

## Description
This is my learning repository where I practice using GitHub and git.
```

**Save the file.**

---

## Step 4: Commit Your Change

```bash
git add README.md
git commit -m "Add description to README"
```

**Important:** This change only exists on the `add-description` branch!

---

## Step 5: Switch Back to Main

```bash
git checkout main
```

**Look at your README.md file.** The description is gone!

That's because `main` branch doesn't have your change yet.

---

## Step 6: Switch Back to Your Branch

```bash
git checkout add-description
```

**Look at your README.md again.** The description is back!

**This is the power of branches!**

---

## Step 7: Merge Your Branch

Now let's bring your change into `main`:

```bash
git checkout main
git merge add-description
```

You should see:
```
Updating abc123..def456
Fast-forward
 README.md | 3 +++
 1 file changed, 3 insertions(+)
```

**Look at README.md.** The description is now in `main`!

---

## Step 8: Push to GitHub

```bash
git push origin main
```

**Go to your GitHub repository in your browser.** You should see your new description!

---

## Step 9: Delete the Branch (Optional)

You don't need the `add-description` branch anymore:

```bash
git branch -d add-description
```

**Check your branches:**
```bash
git branch
```

Only `main` should remain.

---

## Success Criteria

✅ You created a branch
✅ You made a commit on the branch
✅ You switched between branches
✅ You merged the branch into main
✅ You pushed to GitHub
✅ You can see your changes on GitHub

**If you did all of these, you've mastered basic branching!** 🎉

---

## What You Learned

- `git checkout -b <name>` - Creates and switches to new branch
- `git checkout <name>` - Switches to existing branch
- `git branch` - Lists all branches
- `git merge <name>` - Merges a branch into current branch
- `git branch -d <name>` - Deletes a branch

## Common Questions

### "When should I use branches?"

**Always!** Use branches when:
- Adding a new feature
- Fixing a bug
- Experimenting with changes
- Working with others

**Never commit directly to `main` in real projects!**

### "What if I'm on the wrong branch?"

No problem! Just switch:
```bash
git checkout correct-branch-name
```

If you have uncommitted changes, git will warn you. Commit them first or stash them.

### "Can I have multiple branches?"

Yes! As many as you want:
```bash
git checkout -b feature-1
git checkout -b feature-2
git checkout -b experiment
```

## Next Challenge

Try this:

1. Create a branch called `add-emoji`
2. Add emojis to your README (🚀 ✨ 💡)
3. Commit the change
4. Merge to main
5. Push to GitHub

**Time yourself - can you do it in under 3 minutes?**

---

## Troubleshooting

### "Error: branch already exists"

You already created that branch. Either:
- Use a different name
- Delete the old branch first: `git branch -d old-name`
- Switch to it: `git checkout existing-branch`

### "Error: uncommitted changes"

Commit your changes before switching branches:
```bash
git add .
git commit -m "Describe your changes"
git checkout other-branch
```

### "Error: merge conflict"

This happens when the same file was changed in both branches. We'll cover this in a later exercise!

---

## Next Steps

**More Git practice:**
→ [Exercise: Resolve a Merge Conflict](03-resolve-conflict.md) *(Coming soon)*

**Understand branches deeper:**
→ [Branches and Commits](../../documentation/01-github-basics/branches-and-commits.md)

**Ready to code:**
→ [Hello API Example](../../examples/01-hello-api/)

---

**Branches are your safety net - use them fearlessly!** 🌿
