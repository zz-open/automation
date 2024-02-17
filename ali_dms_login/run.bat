@echo off

set SOURCE_BIN="D:\ProgramData\miniconda3\condabin\activate.bat"

echo "开始登录"
cd /d "E:\jungle\github\zz-open\automation\ali_dms_login"
call %SOURCE_BIN% automation
python main.py
PAUSE