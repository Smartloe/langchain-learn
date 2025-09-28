# -*- coding: utf-8 -*-
"""
@Author: Chenxr
@Date:   2025/9/28 00:04
@Last Modified by:   Chenxr
@Last Modified time: 2025/9/28 00:04
@Description: 
"""
import asyncio
import time


async def call_model_async():
	# 模拟异步API调用
	print("开始调用模型...")
	await asyncio.sleep(5)  # 异步等待
	print("模型调用完成。")
	return "模型结果"


async def perform_other_tasks_async():
	# 模拟执行其他任务
	for i in range(5):
		print(f"执行其他任务 {i + 1}")
		await asyncio.sleep(1)  # 异步等待


async def main_async():
	start_time = time.time()

	# 创建任务并发执行
	model_task = asyncio.create_task(call_model_async())
	other_tasks = asyncio.create_task(perform_other_tasks_async())

	# 等待两个任务都完成
	await asyncio.gather(model_task, other_tasks)

	end_time = time.time()
	total_time = end_time - start_time
	return f"总共耗时：{total_time}秒"


# 运行异步版本
async def run_async_example():
	result = await main_async()
	print(result)


# 执行异步示例
print("=== 异步调用版本 ===")
asyncio.run(run_async_example())