rm -rf dist
python setup.py sdist bdist_wheel
pip install -e .
twine  check  dist/*
twine  upload -u maher.naija --skip-existing  dist/*
