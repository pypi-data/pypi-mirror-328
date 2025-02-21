import requests

url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "deepseek-ai/DeepSeek-V3",
    "messages": ['什么是Ai'],
    "stream": True,
    "max_tokens": 4096,
    "temperature": 0.8
}
headers = {
    "Authorization": "Bearer sk-yksxqzhxgdplaymbgbouudgfzqogomabpvcjjpejzmsgxgof",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)