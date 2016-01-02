.PHONY: docs

init:
	pip install -r requirements.txt

test:
	# This runs all of the tests. To run an individual test, run py.test with
	# the -k flag, like "py.test -k test_path_is_not_double_encoded"
	py.test test_requests.py

coverage:
	py.test --verbose --cov-report term --cov=requests test_requests.py

ci: init
	py.test --junitxml=junit.xml

publish:
	@if ! grep "test_pw = \"\"" tests/defaults.py ; then echo "Remove credentials in tests/defaults.py!!!" && exit -1; fi
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel upload

publish-test:
	@if ! grep "test_pw = \"\"" tests/defaults.py ; then echo "Remove credentials in tests/defaults.py!!!" && exit -1; fi
	python setup.py register -r https://testpypi.python.org/pypi
	python setup.py sdist upload -r https://testpypi.python.org/pypi
	python setup.py bdist_wheel upload -r https://testpypi.python.org/pypi

docs-init:
	pip install -r docs/requirements.txt

docs:
	cd docs && make html

clean:
	rm -rf dist build
	rm -rf SimpleTR64UPnP.egg-info
	cd docs && make clean
	python setup.py clean