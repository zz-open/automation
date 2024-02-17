# ali_dms_login
自动登录阿里云DMS管理平台

## 如何使用
- conda env create -f freeze.yml
- playwright install
- 修改conf.yaml 完善参数
- 修改main.py debug = False
- 运行python main.py

## 问题
- 代码中没有对随机出现的滑块验证做逻辑处理，碰见了重新运行脚本即可
- 代码中加入了stealth.min.js 用于防检测