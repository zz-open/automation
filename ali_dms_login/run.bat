@echo off

set SOURCE_BIN="D:\ProgramData\miniconda3\condabin\activate.bat"

cd /d "E:\jungle\github\zz-open\automation\ali_dms_login"
call %SOURCE_BIN% automation
python main.py -f "E:\jungle\project_conf\ali_dms_login_conf.yaml"
PAUSE