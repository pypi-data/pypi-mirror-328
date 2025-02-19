# Aporia AST

This package provides the interpreter, parser and the AST objects for the Aporia language.
The Aporia language is described in [this paper](https://www.arxiv.org/abs/2411.05570). 

Example programs of the language can be found [here](./examples). The Backus-Naur-Form Grammar of the language is specified here:
![aporia bnf](bnf_aporia.png)


## Installation

You can install the package with

```bash
pip install aporia-interpreter
```

## Usage

### Command Line Interface

You can use the interpreter via the command line interface

```bash
aporia file_to_be_executed.spp
```
Additional options can be found with `aporia -h`

### Python Library

You can also use the library by importing packages with
```python
import aporia.aporia_ast
import aporia.interpreter
import aporia.parser
```

## Contributing

Dependency management and the publishing of packages is managed by [uv](https://github.com/astral-sh/uv).
You can install it with `pip install uv`. The interpreter can be run with `uv run aporia`
