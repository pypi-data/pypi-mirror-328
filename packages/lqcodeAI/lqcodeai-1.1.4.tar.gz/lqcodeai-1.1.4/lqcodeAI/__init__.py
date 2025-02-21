"""
名称:绿旗编程AI课程SDK

说明:这个模块提供了与绿旗编程AI服务交互的接口。

安装: 	```pip3 install lqcodeAI```

主要功能:
	- 语言类AI
		- AI藏头诗创作
        - AI答题竞赛
	- 图像类AI
		- AI表情包生成
		- AI小学生算术题检验
        - AI证件照生成
    - 音频类AI
		- AI小猪佩奇音频合成
		- AI语音转文字
    - 视频类AI
		- AI

示例:
    >>> from lqcodeAI import LqcodeAI
    >>> ai = LqcodeAI()
    >>> result = ai.chat(workflow_name="AI_POETRY", input_data="春天")
"""

import requests
from cozepy import Coze, COZE_CN_BASE_URL,Message,ChatEventType,MessageContentType,TokenAuth
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
        self.base_url = 'http://127.0.0.1:8001/open/lqedu/coze/getAIToken'
        #self.base_url = 'http://lqms.lqcode.fun:8001/open/lqedu/coze/chat'
    
    def getAIToken(self, password):
        """
        获取AI token
        """
        res = requests.get(self.base_url,params={'password':password})
        return TokenAuth(res.json().get('data'))
    
    
    def chat(self,password):
        coze = Coze(auth=self.getAIToken(password),base_url=COZE_CN_BASE_URL)
        # 创建Message对象
        for event in coze.chat.stream(
            bot_id='7472592963538436150',
            user_id="tivon",
            additional_messages=[Message.build_user_question_text("How are you?")]  # 传入Message对象列表
        ):
             if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
                message = event.message
                print(message.content)
# 导出的内容
__all__ = ['LqcodeAI']