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
        getAIToken(password: str) -> TokenAuth: 获取AI访问令牌
        chat(password: str, message: str = "How are you?") -> None: 与AI进行对话
    """
    
    FUN_AI_POETRY = {"name": "AI_POETRY", "desc": "AI藏头诗创造", "bot_id": "1"}
    FUN_AI_EMOJI = {"name": "AI_EMOJI", "desc": "AI生成emoji", "bot_id": "2"}
    
    def __init__(self):
        self.base_url = 'http://127.0.0.1:8001/open/lqedu/coze/getAIToken'
    
    def __getAIToken(self, password: str) -> TokenAuth:
        """
        获取AI访问令牌（私有方法）
        
        Args:
            password (str): 访问密码
            
        Returns:
            TokenAuth: AI访问令牌
            
        Raises:
            requests.RequestException: 当API请求失败时
            ValueError: 当返回数据格式不正确时
        """
        try:
            res = requests.get(self.base_url, params={'password': password})
            res.raise_for_status()
            data = res.json()
            if 'data' not in data:
                raise ValueError("API返回数据格式不正确")
            return TokenAuth(data['data'])
        except requests.RequestException as e:
            raise requests.RequestException(f"获取AI Token失败: {str(e)}")
    
    def chat(self, password: str, message: str) -> None:
        """
        与AI进行对话
        
        Args:
            password (str): 访问密码
            message (str): 发送给AI的消息，默认为"How are you?"
            
        Raises:
            requests.RequestException: 当API请求失败时
            ValueError: 当参数无效时
        """
        try:
            # 将消息格式化为字符串
            message_str = f'{{"function": "AI_POETRY", "input": "{message}"}}'
            coze = Coze(auth=self.__getAIToken(password), base_url=COZE_CN_BASE_URL)
            for event in coze.chat.stream(
                bot_id='7472592963538436150',
                user_id="tivon",
                additional_messages=[Message.build_user_question_text(message_str)]
            ):
                if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
                    message = event.message
                    print(message.content, end='')
        except Exception as e:
            raise Exception(f"聊天过程中出现错误: {str(e)}")

# 导出的内容
__all__ = ['LqcodeAI']