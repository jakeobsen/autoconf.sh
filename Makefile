.PHONY: build test-release release install clean

build:
	python -m build

test-release:
	python3 -m twine upload --repository testpypi -u "__token__" -p "${PYPI_TOKEN_TEST}" dist/*

release:
	python3 -m twine upload -u "__token__" -p "${PYPI_TOKEN}" dist/*

install:
	python3 setup.py install --user

clean:
	rm -rf ./src/autoconfsh/__pycache__ ./src/autoconfsh.egg-info/ ./build/ ./dist/
