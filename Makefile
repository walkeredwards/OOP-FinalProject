TEST = python -m pytest
TEST_ARGS = -s --verbose --color=yes
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports
STYLE_CHECK = flake8
COVERAGE = pytest

.PHONY: all
all: check-style check-type run-test-coverage clean
	@echo "All checks passed"

.PHONY: check-type
check-type:
	$(TYPE_CHECK) finalproject

.PHONY: check-style
check-style:
	$(STYLE_CHECK) finalproject

# discover and run all tests
.PHONY: run-test
run-test:
	$(TEST) $(TEST_ARGS) finalproject/tests

.PHONY: run-test-coverage
run-test-coverage:
	$(COVERAGE) -v --cov-report=html:finalproject/htmlcov --cov-report=term --cov=finalproject finalproject/tests


.PHONY: clean
clean:
	# remove all caches recursively
	rm -rf `find . -type d -name __pycache__` # remove all pycache
	rm -rf `find . -type d -name .pytest_cache` # remove all pytest cache
	rm -rf `find . -type d -name .mypy_cache` # remove all mypy cache
	rm -rf `find . -type d -name .hypothesis` # remove all hypothesis cache
	rm -rf `find . -name .coverage` # remove all coverage cache 
