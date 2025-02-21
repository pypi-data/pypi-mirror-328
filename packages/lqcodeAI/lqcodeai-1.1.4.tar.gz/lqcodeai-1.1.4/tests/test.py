import sys
import os
import json
# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lqcodeAI import LqcodeAI
lqcode = LqcodeAI()
res = lqcode.chat(LqcodeAI.FUN_AI_POETRY, "冯涛")
# json_data = json.loads(json.dumps(res, ensure_ascii=False))
# poetry = json_data['poetry']
print(res)
