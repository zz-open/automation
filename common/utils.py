import os
from typing import Dict, Any

import yaml


def get_conf_abs_path(path_: str) -> str:
    if not path_:
        return ""
    if os.path.isabs(path_):
        return path_

    new_path = f'{os.path.dirname(__file__)}/{path_}'
    return os.path.abspath(new_path)


def parse_yaml(_path: str) -> Dict[str, Any]:
    if not _path:
        raise Exception("yaml path 不能为空")

    conf_path = get_conf_abs_path(_path)
    print(conf_path)
    if not os.path.exists(conf_path):
        raise Exception(f"{conf_path} 不存在")

    with open(conf_path, 'r') as f:
        data = yaml.safe_load(f)
        return {} if data is None else data
