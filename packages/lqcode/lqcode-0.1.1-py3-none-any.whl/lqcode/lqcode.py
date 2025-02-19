"""
绿旗编程AI课程SDK
"""
FUN_AI_POETRY = "AI_POETRY"
FUN_AI_EMOJI = "AI_EMOJI"
FUN_AI_HEAD_POEM = "AI_HEAD_POEM"
import requests

class Lqcode:
    res = requests.get('http://lqcode.fun:8001/open/lqedu/coze/chat')
# 导出的内容
__all__ = ['Lqcode', 'FUN_AI_POETRY', 'FUN_AI_EMOJI', 'FUN_AI_HEAD_POEM'] 