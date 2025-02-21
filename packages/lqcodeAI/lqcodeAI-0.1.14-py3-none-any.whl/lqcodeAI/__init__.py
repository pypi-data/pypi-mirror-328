"""
绿旗编程AI课程SDK

这个模块提供了与绿旗编程AI服务交互的接口。

主要功能:
    - AI藏头诗创作
    - AI表情符号生成

Classes:
    LqcodeAI: 绿旗编程AI功能的主要接口类

示例:
    >>> from lqcodeAI import LqcodeAI
    >>> ai = LqcodeAI()
    >>> result = ai.chat(workflow_name="AI_POETRY", input_data="春天")
"""

import requests

class LqcodeAI:
    """
    绿旗编程AI功能的主要接口类
    
    Attributes:
        FUN_AI_POETRY (dict): AI藏头诗创作功能的配置
        FUN_AI_EMOJI (dict): AI表情符号生成功能的配置
        base_url (str): API服务器的基础URL
    
    Methods:
        chat(workflow_name, input_data): 与AI服务进行对话交互
    """
    
    FUN_AI_POETRY = {"name": "AI_POETRY", "desc": "AI藏头诗创造", "bot_id": "1"}
    FUN_AI_EMOJI = {"name": "AI_EMOJI", "desc": "AI生成emoji", "bot_id": "2"}
    def __init__(self):
        self.base_url = 'http://127.0.0.1:8001/open/lqedu/coze/chat'
        #self.base_url = 'http://lqms.lqcode.fun:8001/open/lqedu/coze/chat'
    def chat(self, workflow_name=None, input_data=None):
        """
        与AI服务进行对话交互
        
        Args:
            workflow_name (str): 工作流名称，用于选择AI功能
            input_data (str): 用户输入的数据
            
        Returns:
            dict: 包含AI响应的字典，如果发生错误则包含错误信息
            
        Raises:
            requests.RequestException: 当HTTP请求失败时
        """
        try:
            if not workflow_name:
                return {"error": "workflow_name 不能为空"}

            if not input_data:
                return {"error": "input_data 不能为空"}
            params = {
                'workflow': workflow_name or self.FUN_AI_POETRY,
                'input': input_data or ""
            }
            
            res = requests.get(self.base_url, params=params)
            
            if res.status_code != 200:
                return {"error": f"服务器响应错误，状态码: {res.status_code}"}
            
            # 直接返回文本内容，不进行JSON解析
            return res.json()
            
        except requests.RequestException as e:
            return {"error": f"请求失败: {str(e)}"}

# 导出的内容
__all__ = ['LqcodeAI'] 