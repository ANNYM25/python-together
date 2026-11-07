# GitHub for two people (you + Anny)

The question you asked: *"If I add a collaborator, is the repo visible in both our
GitHub accounts?"*

Short answer: **a repository physically lives in exactly one place.** It can't be
"owned" by two personal accounts at once. But there are clean ways to make this a
truly shared project where you both push and both get credit.

---

## The three models

### 1. A GitHub Organization — recommended for a 50/50 project ✅

An **organization** is a shared namespace that sits above both your personal
accounts. The repo lives in the org, not in either person's account, so it feels
equally owned.

```
github.com/R341CUL/python-together     <- the org owns it
   ├── member: lucifer   (owner)
   └── member: anny     (owner)
```

- Both of you see it the same way and push directly.
- Neither account "owns" it over the other.
- Free for public repos and unlimited collaborators.

**Set it up (web):**
1. github.com → top-right **+** → **New organization** → Free plan.
2. Name it (e.g. `python-together`).
3. Invite Anny: Org → **People** → **Invite member** → her username → role **Owner**.
4. Create the repo *inside the org*: **+** → New repository → Owner = the org.

> The "Open in Colab" badges in every notebook point at
> `R341CUL/python-together`. If you pick a different org or repo name, do
> a find-and-replace of that string across the `.ipynb` files (one line in each
> notebook's first cell) so the badges open the right place.

### 2. One owner + the other as collaborator

The repo lives in one personal account; the other person is added as a
collaborator with push access.

```
github.com/lucifer/python-together
   └── collaborator: anny   (write access)
```

- Anny can push, open PRs, review — full working access.
- **Her commits still count on her own contribution graph / profile.** 👍
- But the repo is *listed* under your account, not hers. It shows up for her
  under "Repositories I have access to," not as a repo she owns.

**Add a collaborator (web):** Repo → **Settings** → **Collaborators** →
**Add people** → Anny's username.

### 3. Fork + pull requests

Each of you keeps your own copy and sends pull requests to a shared "upstream."
This is how strangers contribute to open source. For two close collaborators it
just adds friction — **skip it** unless you specifically want review gates.

---

## Who gets "credit"?

Credit on GitHub comes from the **commit author email**, not from who owns the
repo. As long as each of you commits under your own identity, both of you light
up your own contribution graphs — in *any* of the models above.

Set your identity once per machine:

```bash
# on Lucifer's laptop
git config --global user.name  "Lucifer"
git config --global user.email "anishchatterjee13@gmail.com"

# on Anny's laptop
git config --global user.name  "Anny"
git config --global user.email "anny@example.com"   # her GitHub email
```

> Use the email that's verified on each person's GitHub account, otherwise the
> commits won't be linked to the profile.

---

## First push (from this folder)

```bash
# 1. make sure everything is committed locally
git add -A
git commit -m "Convert foundations to notebooks; add build pipeline"

# 2. point at the GitHub repo you created (org model shown)
git remote add origin https://github.com/R341CUL/python-together.git

# 3. push
git branch -M main
git push -u origin main
```

Anny then clones the same URL:

```bash
git clone https://github.com/R341CUL/python-together.git
```

## The everyday loop (both of you)

```bash
git pull                      # get the other person's work first
git switch -c teach-decorators   # a short-lived branch
# ... edit a lesson notebook, run it top to bottom ...
git add -A && git commit -m "teach decorators with a timing example"
git push -u origin teach-decorators
# open a Pull Request on GitHub; the other reviews and merges
```

Pushing straight to `main` is fine when you're both in sync, but branches +
pull requests give you a built-in review step — nice when a lesson crosses both
your areas (e.g. an ML credit model with a finance story).
