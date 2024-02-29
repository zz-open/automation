# AliDmsLogin
自动登录阿里云DMS管理平台

## 如何使用
- conda env create -f freeze.yml
- playwright install
- 修改conf.yaml 完善参数
- 运行python main.py 或者python main.py -f "本地自定义配置文件"

## 问题
- 代码中没有对随机出现的滑块验证做逻辑处理，碰见了重新运行脚本即可
- 代码中加入了stealth.min.js 用于防检测

## 第三方依赖
```shell
conda install playwright

playwright install

playwright codegen

C:\Users\zaizai\AppData\Local\ms-playwright\chromium-1097
```