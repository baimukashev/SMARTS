# Evaluation


## To evaluate locally
```bash
$ cd <path>/SMARTS/competition/evaluate
$ python3.8 -m venv ./.venv
$ source ./.venv/bin/activate
$ pip install --upgrade pip
$ python3.8 evaluate.py --input_dir=<path/to/submission/folder> --local
# For example:
$ python3.8 evaluate.py --input_dir=<path>/SMARTS/competition/submission --local
```