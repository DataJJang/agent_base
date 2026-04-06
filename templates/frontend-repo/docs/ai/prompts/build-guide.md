# Build Guide Prompt

## Prompt Template

```text
Create a build guide for the following project work item.

Repository: {{REPOSITORY}}
Branch: {{BRANCH}}
Scope: {{SCOPE}}
Target environments: {{ENVIRONMENTS}}
Relevant code paths:
- {{CODE_PATH_1}}
- {{CODE_PATH_2}}
Relevant build and config files:
- {{BUILD_FILE}}
- {{CONFIG_FILE}}
Reference docs:
- {{DOC_PATH_1}}
- {{DOC_PATH_2}}
Out of scope:
- {{OUT_OF_SCOPE}}

Requirements:
- Follow AGENTS.md and the relevant docs/ai service guide.
- Focus on prerequisites, local setup, required dependencies, build commands, profile considerations, and common failure points.
- Distinguish mandatory steps from optional troubleshooting tips.
- Include validation after build.
- Explicitly list secrets or environment values that must not be hardcoded in docs.

Output format:
- Purpose
- Preconditions
- Required files and settings
- Build steps
- Verification steps
- Common failures and fixes
- Manual follow-ups
```
