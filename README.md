# **Sequence Alignment** 

A simple python program to align sequence globally or locally.

## Overview

This is a python program to perform pairwise local alignment and global alignment for a character sequence, e.g. DNA, RNA or protein sequence. It uses Needleman–Wunsch algorithm to perform alignment, which is a commonly used algorithm in aligning short sequence.

## Prerequisites

- Python 3

## Getting started

You can either use it directly or use it in your program.

### Use directly

1. `cd aligner`

2. type `python local_alignment <seq_s> <seq_t> <match> <mismatch> <indel>` for local alignment

   OR

   `python global_alignment <seq_s> <seq_t> <match> <mismatch> <indel>` for global alignment

| Parameters | Description             |
| ---------- | ----------------------- |
| `seq_s`    | The target sequence `s` |
| `seq_t`    | The target sequence `t` |
| `match`    | The match score         |
| `mismatch` | The mismatch score      |
| `indel`    | The indel score         |

### Use in your program

``` python
from aligner import local_alignment, global_alignment

local_alignment.initialize(SEQ_S, SEQ_T, MATCH, MISMATCH, INDEL)
local_alignment.calculate()
score = format(local_alignment.optimal_score())
local_alignment.print_result()
```

There are some examples under `example.py`.

## License

This project is licensed under the MIT License - see the LICENSE file for details