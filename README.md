# python-cli-calculator

[![CI](https://github.com/Chrismastian/python-cli-calculator/actions/workflows/ci.yml/badge.svg)](https://github.com/Chrismastian/python-cli-calculator/actions/workflows/ci.yml)

Kalkulator sederhana berbasis CLI untuk belajar Python: struktur project, `argparse`, `pytest`, dan CI.

## Cara pakai

```bash
python -m calculator.cli 2 3 --op add   # Hasil: 5.0
python -m calculator.cli 10 4 --op div  # Hasil: 2.5
```

Operasi: `add`, `sub`, `mul`, `div`.

## Development

```bash
pip install pytest
pytest
```

## Struktur

```
calculator/
  core.py   # logika murni (pure functions) — gampang dites
  cli.py    # argparse: baca input terminal, panggil core
tests/
  test_core.py
```
