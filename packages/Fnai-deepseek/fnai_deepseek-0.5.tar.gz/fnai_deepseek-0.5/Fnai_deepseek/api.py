# 非流式输出api.py


import requests

# 定义API的URL地址
url = "https://api.siliconflow.cn/v1/chat/completions"

# 定义请求的参数和配置
payload = {
    # 指定使用的AI模型
    "model": "deepseek-ai/DeepSeek-V3",
    # 定义对话历史，用于给AI提供上下文
    "messages": [
        {
            "role": "user",  # 指定当前消息的角色是用户（user）
            "content": "一句话总结什么是Ai？"  # 用户输入的内容
        }
    ],
    # 是否启用流式输出，当前设置为关闭
    "stream": False,
    # 指定生成内容的最大token数
    "max_tokens": 512,
    # 设置停止生成的条件，当前未使用有效停止符（null可能需进一步调整）
    "stop": ["null"],
    # 设置生成内容的随机性（值越高生成越多样化，值越低生成更确定的内容）
    "temperature": 0.7,
    # 核采样参数，限制生成内容的概率分布
    "top_p": 0.7,
    # 限制生成时只考虑概率最高的前k个词
    "top_k": 50,
    # 降低重复使用相同词语的概率
    "frequency_penalty": 0.5,
    # 指定生成候选响应的数量
    "n": 1,
    # 设置响应格式为纯文本格式
    "response_format": {"type": "text"},
    # 工具字段，可能是扩展功能的占位符，当前未实际使用
    "tools": [
        {
            "type": "function",  # 工具类型
            "function": {
                "description": "<string>",  # 工具描述，当前为占位符
                "name": "<string>",  # 工具名称，当前为占位符
                "parameters": {},  # 工具参数，当前为空
                "strict": False  # 是否严格执行，当前为False
            }
        }
    ]
}

# 定义请求头，包括授权信息和内容类型
headers = {
    "Authorization": "Bearer sk-yksxqzhxgdplaymbgbouudgfzqogomabpvcjjpejzmsgxgof",  # API密钥
    "Content-Type": "application/json"  # 设置请求体为JSON格式
}

# 使用requests库发送HTTP POST请求
response = requests.request("POST", url, json=payload, headers=headers)

# 检查请求是否成功
if response.status_code == 200:  # 如果状态码是200，表示请求成功
    print('请求成功')  # 打印成功信息
    data = response.json()  # 将返回的响应转换为JSON格式（Python字典）
    # 提取生成内容的核心部分
    content = data["choices"][0]["message"]["content"]  # 从返回的JSON中找到content字段
    print(content)  # 打印生成的内容
    print('总token：'+data['usage']['total_tokens'])  # 打印总token
else:
    # 如果请求失败，打印状态码和返回的错误内容
    print(f"Error: {response.status_code}, {response.text}")
