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

#### Help
```bash
python cli.py --help
```

#### Print the log's content
```bash
log_analytics show-log --file example/data/race.log
```
or
```bash
python cli.py show-log --file example/data/race.log
```


#### List the race result
```bash
python cli.py race-result --file example/data/race.log

```

#### The best lap of each driver

```bash
python cli.py best-lap --file example/data/race.log

```

#### The race best lap
```bash
python cli.py race-best-lap --file example/data/race.log

```