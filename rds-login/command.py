# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 20:49
@Auth ： 仔仔
@File ：rds_automation.py
@Description ：rds集成command
"""
from typing import Dict, Any

import click


@click.command()
@click.option("-b", "--binary-location", type=str, required=True, help="浏览器程序路径")
@click.option("-ud", "--user-data-dir", type=str, required=True, help="用户数据配置路径")
@click.option("-u", "--aliyun-username", type=str, required=True, help="阿里云账号")
@click.option("-pwd", "--aliyun-password", type=str, required=True, help="阿里云密码")
@click.option("-p", "--port", default=9222, show_default=True, type=int, help="浏览器debug模式端口，可以复用进程")
def command(binary_location, user_data_dir, aliyun_username, aliyun_password, port):
    click.echo(click.style(f"binary_location: {binary_location}", fg="red", bold=True))
    click.echo(click.style(f"user_data_dir: {user_data_dir}", fg="red", bold=True))
    click.echo(click.style(f"aliyun_username: {aliyun_username}", fg="red", bold=True))
    click.echo(click.style(f"aliyun_password: {aliyun_password}", fg="red", bold=True))
    click.echo(click.style(f"port: {port}", fg="red", bold=True))
    command_params: dict[str, Any] = {
        "binary_location": binary_location,
        "user_data_dir": user_data_dir,
        "aliyun_username": aliyun_username,
        "aliyun_password": aliyun_password,
        "port": port,
    }


if __name__ == '__main__':
    command()
