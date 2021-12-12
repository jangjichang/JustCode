.PHONY: check
check:
	isort . --diff
	isort . --check-only
	black -S -l 110 --check leetcode
	flake8

.PHONY: format
format:
	isort .
	black . --config pyproject.toml
