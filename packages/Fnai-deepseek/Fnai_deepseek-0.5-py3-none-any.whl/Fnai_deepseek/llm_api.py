# fai_deepseek/llm_api.py
import requests
import json


class APIError(Exception):
    """自定义异常类，用于处理API错误"""

    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error {status_code}: {message}")


def talk(
        user_input: str,
        model: str = "deepseek-ai/DeepSeek-V3",
        max_tokens: int = 512,
        temperature: float = 0.7,
        api_key: str = "sk-yksxqzhxgdplaymbgbouudgfzqogomabpvcjjpejzmsgxgof"
) -> str:
    """
    非流式对话方法：用户传入问题，直接返回完整回答

    参数：
    - user_input: 用户的问题（字符串）
    - model: 模型名称（默认 deepseek-ai/DeepSeek-V3）
    - max_tokens: 最大生成长度
    - temperature: 随机性控制（0-1）
    - api_key: API密钥（建议通过环境变量传入）

    返回：
    - 模型生成的完整回答（字符串）
    """
    url = "https://api.siliconflow.cn/v1/chat/completions"

    # 自动构造 messages 列表
    messages = [{"role": "user", "content": user_input}]

    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        else:
            raise APIError(response.status_code, response.text)
    except Exception as e:
        raise APIError(500, f"请求失败: {str(e)}")


def stream_talk(
        user_input: str,
        model: str = "deepseek-ai/DeepSeek-V3",
        max_tokens: int = 512,
        temperature: float = 0.7,
        api_key: str = "sk-yksxqzhxgdplaymbgbouudgfzqogomabpvcjjpejzmsgxgof",
        callback=None  # 可选的回调函数，实时处理流式输出
) -> str:
    """
    流式对话方法：逐块返回回答（支持回调函数实时输出）

    参数：
    - user_input: 用户的问题（字符串）
    - model: 模型名称（默认同上）
    - max_tokens: 最大生成长度
    - temperature: 随机性控制
    - api_key: API密钥
    - callback: 接收每个片段的回调函数（如 print）

    返回：
    - 完整拼接的回答（字符串）
    """
    url = "https://api.siliconflow.cn/v1/chat/completions"

    messages = [{"role": "user", "content": user_input}]

    payload = {
        "model": model,
        "messages": messages,
        "stream": True,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    full_content = ""
    try:
        response = requests.post(url, json=payload, headers=headers, stream=True)
        if response.status_code != 200:
            raise APIError(response.status_code, response.text)

        for chunk in response.iter_lines():
            if chunk:
                chunk_str = chunk.decode('utf-8').strip()
                if chunk_str == "data: [DONE]":
                    continue
                if chunk_str.startswith("data: "):
                    chunk_str = chunk_str[6:]

                try:
                    chunk_data = json.loads(chunk_str)
                    if "choices" in chunk_data:
                        content = chunk_data["choices"][0]["delta"].get("content", "")
                        full_content += content
                        if callback:
                            callback(content)  # 实时输出到回调函数
                except json.JSONDecodeError:
                    continue
        return full_content
    except Exception as e:
        raise APIError(500, f"流式请求失败: {str(e)}")
