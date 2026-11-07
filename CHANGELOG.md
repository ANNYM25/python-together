# Changelog

All notable changes to this lab. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added
- **Repository architecture pass**: hero README with a Mermaid learning-path
  diagram, curriculum-at-a-glance, and a repo-layout map.
- **Leak-proof tooling**: `gitleaks` secret-scanning GitHub Action, `.gitleaks.toml`,
  and `SECURITY.md`.
- Repo hygiene: `.gitattributes` (LF normalization), `CHANGELOG.md`, GitHub issue
  templates (bug report + new-lesson request).

## [0.2.0] — 2026-11-07

### Changed
- **Converted the entire lab to runnable Jupyter notebooks** (58 `.ipynb` across
  11 tracks). Lessons are now flat and beginner-first — markdown explanation then
  plain code — instead of `def`-wrapped scripts. Notebooks are the source of truth.
- Fixed contributor name spelling throughout (Anny).

### Added
- Deep **machine-learning** track: ML taxonomy, KNN, neural-net-from-scratch,
  CNN intro, and a Kaggle workflow.
- New **projects**: build-your-own `NeuralNet` class and a tiny character-level
  language model.
- Deepened **mathematics** (incl. probability) and **data-science** (incl. statistics).
- "Open in Colab" badge on every lesson; CI that executes all notebooks;
  CodeRabbit config; Colab/Jupyter/GitHub-for-two-people docs.
- Self-verifying `✔️ Quick check` cells replace the old pytest suite.

## [0.1.0]

### Added
- Initial shared Python, math, ML, and fintech lab (script-based lessons).
