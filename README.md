# Chuck

## Install and run

```
pip install -e .
chuck
```

## Install and run with virturalenv

```
# one time
python3 -mvenv .venv
source .venv/bin/activate
pip install -e .

# each new shell
source .venv/bin/activate

chuck
```

## Build and run docker image

```
docker build -t chuck .
docker run --rm chuck
```
