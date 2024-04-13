@echo off

set SOURCE_BIN="D:\ProgramData\miniconda3\condabin\activate.bat"
echo 当前路径：%cd%
call %SOURCE_BIN% automation
python main.py -f "./kword.yaml"
PAUSE