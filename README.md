## Log Analytics
---

This project try to solve the gympass interview test.
The challenge description is on [CHALLENGE.md](CHALLENGE.md).

## Technologies
---
 * Python 3.7+

## How to
---

### Install

#### Development environment

```bash
pip install -r requirements-dev.txt
```

#### Bash Command
```bash
pip install --editable .
```

### Tests

```bash
pytest .
```

### Usage

Print the log's content
```bash
log_analytics show-log --file example/data/race.log
```
OR
```bash
python cli.py show-log --file example/data/race.log
```


```bash
log_analytics race-result --file example/data/race.log

```
OR
```bash
python cli.py race-result --file example/data/race.log

```