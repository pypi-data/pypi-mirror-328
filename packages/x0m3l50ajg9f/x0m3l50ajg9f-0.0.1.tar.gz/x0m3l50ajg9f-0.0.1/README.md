# pypitemplate

## Setup

```
python3 -m venv venv
. venv/bin/activate.fish
python3 -m pip install -r requirements.txt
```

## Build

```
python3 -m build
```

## Distribute

### TestPyPI

```
python3 -m twine upload --repository testpypi dist/*
```

### Production

```
python3 -m twine upload dist/*
```
