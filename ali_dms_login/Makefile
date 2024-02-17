.PHONY:	help test
help:
	@echo "usage: make <option>"
	@echo "options and effects:"
	@echo "    help                     : Show help"
	@echo "    test                     : Test ..."

test:
	@echo "test ..."

.PHONY:	create-requirements run
create-requirements:
	@conda list -e > requirements.txt

run:
	@python main.py
