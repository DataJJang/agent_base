# e-gov Branch PR Draft

## Title

Add eGov/public-sector profile routing and brownfield support

## Summary

- add a public-sector/eGov overlay path without introducing a new top-level project family
- expand brownfield analyzer coverage for eGovFrame-style repositories
- add KRDS/public UI review assets and prompt examples for public-sector work
- surface `organizationProfile = egov-public-sector` through bootstrap, generation manifests, and starter output

## Why

- our main use case is not a broad generic harness but repeatable support for Korean public-sector SI and eGovFrame-heavy work
- these projects often mix brownfield migration, legacy constraints, KRDS/accessibility review, and public-sector delivery expectations
- keeping common project families while turning on an explicit org/domain profile keeps the system narrower and easier to operate

## What Changed

### Public-sector overlay

- added `docs/ai/org-specific/egov-public-sector-guide.md`
- added eGov bootstrap/adoption/UI review prompt pack
- added `checklists/public-sector-ui-review.md`

### Brownfield analyzer

- expanded `source/scripts/analyze_repository.py`
- now emits stronger hints for eGovFrame, Spring MVC/JSP, MyBatis, Tiles/layout, Globals, shared JS/CSS, and public-sector UI patterns
- continues to write inventory, docs gap report, and role recommendation as a bundle

### organizationProfile support

- added `organizationProfile` to the generation spec flow
- added `egov-public-sector` as the first real organization profile
- routed this profile into bootstrap CLI, context manifest, generation manifest, refinement manifest, generated README, and starter helper output
- kept existing `projectFamily` values unchanged

### Docs and examples

- updated bootstrap/adoption/selection/spec docs to explain family vs organization profile
- added example spec for `egov-public-sector`
- added maintainer-facing organization profile overview

## Verification

- `python3 -m py_compile source/scripts/analyze_repository.py source/scripts/project_bootstrap_cli.py source/scripts/generate_project.py source/scripts/show_start_path.py`
- `python3 source/scripts/analyze_repository.py --repo /tmp/hf-egov-sample`
- `python3 tools/build_templates.py`
- `python3 tools/build_templates.py --check`

## Risks / Follow-Up

- current runnable scaffolds still reflect common family baselines; deeper eGovFrame-specific runnable scaffolds are still future work
- `organizationProfile` currently starts with `egov-public-sector`; more profiles should be added only when they represent real repeated work
- repository family/profile routing is stronger now, but CI workflow coverage is still a separate track
