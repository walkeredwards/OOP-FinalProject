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
	$(TYPE_CHECK) project

.PHONY: check-style
check-style:
	$(STYLE_CHECK) project

# discover and run all tests
.PHONY: run-test
run-test:
	cd project && \
	$(TEST) $(TEST_ARGS)

.PHONY: run-test-coverage
run-test-coverage:
# allows pytest to find the image paths within the container
	cd project && \
	$(COVERAGE) -v --cov-report=html:project/htmlcov --cov-report=term --cov=project


.PHONY: clean
clean:
	# remove all caches recursively
	rm -rf `find . -type d -name __pycache__` # remove all pycache
	rm -rf `find . -type d -name .pytest_cache` # remove all pytest cache
	rm -rf `find . -type d -name .mypy_cache` # remove all mypy cache
	rm -rf `find . -type d -name .hypothesis` # remove all hypothesis cache
	rm -rf `find . -name .coverage` # remove all coverage cache 
