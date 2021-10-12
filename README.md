# Python Poetry build example.

### Example for build your python project with offline dependencies

Export python instaled dependencies

```sh
poetry export -o requirements.txt
```

Download project dependencies

```sh
pip download -r requirements.txt -d dependencies/
```

Install offline dependencies

```sh
pip install --no-index --find-links dependencies/ -r requirements.txt 
```
