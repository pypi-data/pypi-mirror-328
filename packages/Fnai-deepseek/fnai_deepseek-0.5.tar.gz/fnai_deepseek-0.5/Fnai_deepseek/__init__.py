# Fnai_deepseek/__init__.py
from .llm_api import talk, stream_talk, APIError

__all__ = ["talk", "stream_talk", "APIError"]