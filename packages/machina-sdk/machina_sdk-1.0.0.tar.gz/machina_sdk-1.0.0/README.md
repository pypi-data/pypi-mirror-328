# Machina @ SDK

## Installation
```shell
python3.11 -m venv venv

source venv/bin/activate

pip install pdm

pip install build

pdm install

python -m build

pip install ~/machina/machina-core-sdk/dist/machina_sdk-0.1.21-py3-none-any.whl --force-reinstall
```

## Release a version
```shell
chmod +x release.sh

./release.sh
```

## Publication
```shell
pip install twine

twine upload dist/*
```