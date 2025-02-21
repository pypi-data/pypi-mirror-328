import sys
import os
import json
# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lqcodeAI import LqcodeAI
lqcode = LqcodeAI()
lqcode.chat(pd='lqcode', func=lqcode.FUN_AI_POETRY, mg='冯涛')

