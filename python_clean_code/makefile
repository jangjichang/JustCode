typehint:
	mypy	ch01/

test:
	pytest	ch01/

lint:
	pylint --rcfile=/Users/jangjichang/Workspace/JustCode/python_clean_code/.pylintrc ch01/

checklist: lint typehint test

.PHONY: typehint test lint checklist