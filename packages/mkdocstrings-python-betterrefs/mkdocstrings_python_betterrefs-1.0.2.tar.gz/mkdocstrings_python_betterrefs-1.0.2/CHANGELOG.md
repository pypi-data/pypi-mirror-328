## Version 1.0.2

(bugfix) Pass configuration options over to collect during reference checking.

## Version 1.0.1 (2025-02-12)

Documentation improvements.

## Version 1.0.0 (2025-02-12)

This is the initial release following a **rewrite of the project (fork)**.

### Breaking changes

- Handler name was renamed to `python_betterrefs` (from `python_xrefs`)
- Config option `relative_crossrefs` was renamed to `better_crossrefs`
- Config option `better_crossrefs` (previously `relative_crossrefs`) is now enabled by default

### Other changes

- Rewrite the project documentation
- Move to `basedpyright` type-checker (from mypy)
- Move to `uv` package manager (from condadev)
- Improve CI workflows
- Improve testing
