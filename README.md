# python-cli-calculator

[![CI](https://github.com/Chrismastian/python-cli-calculator/actions/workflows/ci.yml/badge.svg)](https://github.com/Chrismastian/python-cli-calculator/actions/workflows/ci.yml)

A simple CLI calculator built while learning Python: project structure, `argparse`, `pytest`, and CI.

## Usage

```bash
python -m calculator.cli 2 3 --op add   # -> 5.0
python -m calculator.cli 10 4 --op div  # -> 2.5
```

Operations: `add`, `sub`, `mul`, `div`.

## Development

```bash
pip install pytest
pytest
```

## Structure

```
calculator/
  core.py   # pure logic (pure functions) — easy to test
  cli.py    # argparse: reads terminal input, calls core
tests/
  test_core.py
```
