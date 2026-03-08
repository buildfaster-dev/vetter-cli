# ADR-001: Rebrand the-driver to Vetter

## Status

Accepted

## Context

"The Driver" was a working prototype name for the AI-powered code review CLI. As the project moves toward public release, a more descriptive and brandable name is needed.

The name "Vetter" was chosen because:
- It directly communicates the tool's purpose — vetting candidates
- The domain `vetter.so` has been purchased
- It's concise and memorable

## Decision

- Rename the Python package from `the-driver` to `vetter`
- Rename the CLI command from `the-driver` to `vetter`
- Rename the GitHub repo from `buildfaster-dev/the-driver` to `buildfaster-dev/vetter-cli` (keeping `vetter` free for a future web app)

## Consequences

- All imports change from `the_driver.*` to `vetter.*`
- CLI invocation changes from `the-driver analyze` to `vetter analyze`
- All documentation updated to reflect new name
- Git remote URL changes
- Existing installations need reinstallation
