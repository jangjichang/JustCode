typehint:
	mypy	ch02/

test:
	pytest	ch02/

lint:
	pylint --rcfile=/Users/jangjichang/Workspace/JustCode/python_clean_code/.pylintrc --exit-zero ch02/

checklist: lint typehint test

.PHONY: typehint test lint checklist
