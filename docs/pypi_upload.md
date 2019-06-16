### PyPI commands


```bash
python3.6 -m pip install --user --upgrade setuptools wheel
python3.6 setup.py sdist bdist_wheel
python3.6 -m pip install --user --upgrade twine
python3.6 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```