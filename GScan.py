# coding:utf-8
from lib.core.option import *
import os

# 作者：咚咚呛
# 版本：v0.1
# 功能：本程序旨在为安全应急响应人员对Linux主机排查时提供便利，实现主机侧安全Checklist的自动化，用于快速主机安全点排查。


if __name__ == '__main__':
    version = 'v0.1'

    main(os.path.dirname(os.path.abspath(__file__)))
