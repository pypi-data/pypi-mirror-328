# 流式输出str_api.py
import requests
import json

# 定义API的URL地址
url = "https://api.siliconflow.cn/v1/chat/completions"

# 定义请求的参数和配置
payload = {
    "model": "deepseek-ai/DeepSeek-V3",
    "messages": [
        {
            "role": "user",
            "content": "一句话总结什么是Ai？"
        }
    ],
    "stream": True,  # 启用流式输出
    "max_tokens": 512,
    "temperature": 0.7,
    "top_p": 0.7,
    "top_k": 50,
    "frequency_penalty": 0.5,
    "n": 1
}

# 定义请求头，包括授权信息和内容类型
headers = {
    "Authorization": "Bearer sk-yksxqzhxgdplaymbgbouudgfzqogomabpvcjjpejzmsgxgof",
    "Content-Type": "application/json"
}

# 使用requests库发送HTTP POST请求
try:
    # 设置 `stream=True` 以支持流式响应
    response = requests.post(url, json=payload, headers=headers, stream=True)

    # 检查请求是否成功
    if response.status_code == 200:  # 如果状态码是200，表示请求成功
        print('请求成功，开始接收流式输出：')

        # 初始化变量存储完整内容
        full_content = ""

        # 逐步从响应流中读取每一块数据
        for chunk in response.iter_lines():
            if chunk:  # 忽略空行
                # 强制使用 UTF-8 解码二进制数据
                chunk_decoded = chunk.decode('utf-8').strip()

                # 如果收到结束标记 "[DONE]"，直接跳过
                if chunk_decoded == "[DONE]":
                    continue

                # 移除前缀 "data: "（如果存在）
                if chunk_decoded.startswith("data: "):
                    chunk_decoded = chunk_decoded[len("data: "):]

                try:
                    # 加载每个流式块的内容
                    chunk_data = json.loads(chunk_decoded)
                    if 'choices' in chunk_data:
                        # 提取内容部分
                        content_part = chunk_data['choices'][0]['delta'].get('content', '')
                        full_content += content_part  # 拼接内容
                        print(content_part, end='', flush=True)  # 实时输出
                except json.JSONDecodeError:
                    # 如果解析失败，打印调试信息并跳过
                    print(f"\n收到非JSON数据块：{chunk_decoded}")
                    continue

        print("\n---\n完成接收！")
        print("完整内容：", full_content)

    else:
        # 如果请求失败，打印状态码和返回的错误内容
        print(f"Error: {response.status_code}, {response.text}")

except Exception as e:
    # 捕获可能的异常并打印
    print(f"请求过程中发生错误：{str(e)}")
