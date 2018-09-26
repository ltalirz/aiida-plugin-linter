# aiida-plugin-linter

A tool to provide automatic advice for transitioning plugins
from aiida-core v0.x to aiida-core v1.0

**Warning:** So far, this just demonstrates how to use pylint. *Not* yet useful for production

## Usage

```
pip install -e .
./run.sh
```


## Warnings

Warns about

* 'W2000': 'workfunction has moved to aiida.work.workfunctions'
* 'W2001': 'submit is now JobCalculation.submit'
* 'W2002': "functions moved from 'aiida.work.run' to 'aiida.work.launch'
