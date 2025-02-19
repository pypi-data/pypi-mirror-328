import logging
from openai import OpenAI  # 请确认你安装的 openai 库版本支持这种调用方式

# -------------------------
# 配置 httpcore 日志，将其写入到 trace.log 文件中
# -------------------------
# 获取用于 HTTP/1.1 的 httpcore logger
httpcore_logger = logging.getLogger("httpcore.http11")
httpcore_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("trace.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
httpcore_logger.addHandler(file_handler)

# 同时配置 "httpcore" 的根 logger（如有必要）
root_httpcore_logger = logging.getLogger("httpcore")
root_httpcore_logger.setLevel(logging.DEBUG)
root_httpcore_logger.addHandler(file_handler)

# -------------------------
# 使用 OpenAI API 发起请求
# -------------------------
client = OpenAI(api_key="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")  # 替换成你的 API key

# 构造消息（这里的 prompt 会作为请求体的一部分发送）
messages = [
    {
        "role": "user",
        "content": "请帮我写一段 Python 代码，实现计算斐波那契数列。"
    }
]

# 发起 API 请求
response = client.chat.completions.create(
    messages=messages,
    model="gpt-4o",
    temperature=0.9,
)

# 获取返回内容并打印
content = response.choices[0].message.content
print("Response content:", content)
