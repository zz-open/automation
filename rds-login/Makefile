# path
MAKEFILE_PATH = $(abspath $(lastword $(MAKEFILE_LIST)))
MAKEFILE_DIR = $(dir $(MAKEFILE_PATH))
SOURCE_PATH = $(MAKEFILE_DIR)

include $(SOURCE_PATH).env
include $(SOURCE_PATH).env.development

PROJECT_DIR = $(dir $(MAKEFILE_DIR)../)
DRIVER_PATH = $(PROJECT_DIR)driver
OUT_PATH = $(MAKEFILE_DIR)out

PYTHON = $(VIRTUAL_ENV_BIN_PATH)/python
PYINSTALLER = $(VIRTUAL_ENV_BIN_PATH)/pyinstaller
COMMAND_PY = command.py
BIN_NAME = rds-login

# long params define
define RDS_COMMAND_PARAMS
-e '$(DRIVER_PATH)/98/chromedriver' \
-b '$(BROWSER_BIN_PATH)' \
-ud '$(SOURCE_PATH)QQBrowserProfile' \
-u '$(ALIYUN_USERNAME)' \
-pwd '$(ALIYUN_PASSWORD)'
endef

.PHONY: help build clean test t-rds-login b-rds-login port ln requirement add-python-path

help:
	@echo "usage: make <option>"
	@echo "options and effects:"
	@echo "    help   			: Show help"
	@echo "    build  			: Build the binary of this project for current platform"
	@echo "    clean  			: Clean build"
	@echo "    test  			: Test"
	@echo "    ln 				: Create ln"
	@echo "    requirement 		: Create requirements.txt"
	@echo "    port   			: Test port available"
	@echo "    t-rds-login 		: Call rds_login.py"
	@echo "    b-rds-login 		: Call rds-login binary"
	@echo "    local-rds-login 	: Local call rds_login.py"
	@echo "    add-python-path  : Add PYTHONPATH to .zshrc"

build:
	@$(PYINSTALLER) -n $(BIN_NAME) -D -w --distpath $(OUT_PATH)/dist --workpath $(OUT_PATH)/build  --specpath $(OUT_PATH) --clean $(SOURCE_PATH)$(COMMAND_PY)
	@echo "Build success ..."

port:
	@lsof -nP -iTCP:9222 -sTCP:LISTEN

t-rds:
	@$(PYTHON) $(SOURCE_PATH)$(COMMAND_PY) \
	$(RDS_COMMAND_PARAMS)
	@echo "python command.py start ..."

b-rds:
	@$(SOURCE_PATH)out/dist/$(BIN_NAME)/$(BIN_NAME) \
	$(RDS_COMMAND_PARAMS)
	@echo "Binary $(BIN_NAME) start ..."

clean:
	@rm -rf $(OUT_PATH)
	@echo "Clean finish ..."

test:
	@echo "Test ..."

requirement:
	@pip freeze > requirements.txt
	@echo "Create requirements.txt success ..."

add-python-path:
	@echo 'export PYTHONPATH="$PYTHONPATH:$(PROJECT_DIR)"' >> ~/.zshrc

ln:
	@ln -s \
	$(PTH_PATH)/zz-playwright.pth \
	$(VIRTUAL_ENV_PATH)/lib/python3.11/site-packages/zz-playwright.pth