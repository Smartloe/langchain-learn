# -*- coding: utf-8 -*-
"""
@Author: Chenxr
@Date:   2025/9/28 00:02
@Last Modified by:   Chenxr
@Last Modified time: 2025/9/28 00:02
@Description: 
"""
import asyncio
import os
import time
import dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

# 初始化大模型
chat_model = ChatOpenAI(model="gpt-4o-mini")


# 同步调用（对比组）
def sync_test():
	messages1 = [
		SystemMessage(content="你是一位乐于助人的智能小助手"),
		HumanMessage(content="请帮我介绍一下什么是机器学习")
	]
	start_time = time.time()
	response = chat_model.invoke(messages1)  # 同步调用
	duration = time.time() - start_time
	print(f"同步调用耗时：{duration:.2f}秒")
	return response, duration


# 异步调用（实验组）
async def async_test():
	messages1 = [
		SystemMessage(content="你是一位乐于助人的智能小助手"),
		HumanMessage(content="请帮我介绍一下什么是机器学习")
	]
	start_time = time.time()
	response = await chat_model.ainvoke(messages1)  # 异步调用
	duration = time.time() - start_time
	print(f"异步调用耗时：{duration:.2f}秒")
	return response, duration


# 运行测试
if __name__ == "__main__":
	# 运行同步测试
	sync_response, sync_duration = sync_test()
	print(f"同步响应内容: {sync_response.content[:100]}...\n")

	# 运行异步测试
	async_response, async_duration = asyncio.run(async_test())
	print(f"异步响应内容: {async_response.content[:100]}...\n")

	# 并发测试 - 修复版本
	print("\n=== 并发测试 ===")
	start_time = time.time()


	async def run_concurrent_tests():
		# 创建3个异步任务
		tasks = [async_test() for _ in range(3)]
		# 并发执行所有任务
		return await asyncio.gather(*tasks)


	# 执行并发测试
	results = asyncio.run(run_concurrent_tests())
	total_time = time.time() - start_time
	print(f"\n3个并发异步调用总耗时: {total_time:.2f}秒")
	print(f"平均每个调用耗时: {total_time / 3:.2f}秒")