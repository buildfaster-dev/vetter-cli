# Installation

Vetter requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

## Quick Install (from GitHub)

```bash
uv tool install git+https://github.com/buildfaster-dev/vetter-cli.git
```

This installs the `vetter` command globally. No SSH key needed — the repo is public.

## Development Install

```bash
git clone https://github.com/buildfaster-dev/vetter-cli.git
cd vetter-cli
uv sync
```

Then run with `uv run vetter analyze <repo-path>`.

## API Key

Vetter requires an Anthropic API key:

```bash
export ANTHROPIC_API_KEY=your-key-here
```

## Verify Installation

```bash
vetter --help
vetter analyze --help
```
