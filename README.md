# LangChain 学习项目

这是一个跟随尚硅谷教程学习 LangChain 的实践项目，涵盖了从基础到实战的多个案例开发。

## 📚 项目简介

本教程从入门到实战，开发多个前沿项目案例，涵盖：
- 🤖 智能对话助手
- 📖 知识库问答助手  
- 🌤️ 天气智能查询助理
- 等多个实战项目

通过实践这些项目，快速提升 LangChain 实战开发经验！

## 🗂️ 项目结构

```plaintext
langchain-learn/
├── src/longchain_learn/          # 主要源代码
│   ├── chapter01-summary/        # LangChain 概述
│   ├── chapter02-model IO/       # Model IO 模块
│   ├── chapter03-Chains/         # Chains 模块
│   ├── chapter04-Memory/         # Memory 模块
│   ├── chapter05-Tools/          # Tools 模块
│   └── chapter06-Agents/         # Agents 模块
├── docs/                         # 学习文档和资料
├── examples/                     # 示例文件
├── tests/                        # 测试代码
├── main.py                       # 主程序入口
├── pyproject.toml               # 项目配置
└── uv.lock                      # 依赖锁定文件
```

## 🚀 快速开始

### 环境要求

- Python 3.x
- uv 包管理器

### 安装依赖

本项目使用 `uv` 进行依赖管理：

```bash
# 安装依赖
uv add <package_name>

# 或根据 pyproject.toml 安装所有依赖
uv sync
```

### 配置 API Keys

在项目根目录创建 `.env` 文件，添加所需的大模型 API Key：

```env
OPENAI_API_KEY=your_openai_api_key_here
OTHER_API_KEY=your_other_api_key_here
```

⚠️ **注意**: 出于安全考虑，`.env` 文件已添加到 `.gitignore`，不会被上传到 GitHub。



## 📖 学习内容

### 各章节内容

1. **Chapter 01**: LangChain 概述和 Hello World
2. **Chapter 02**: Model IO 模块
   - 模型的调用
   - 提示词模板 (Prompt Template, ChatPromptTemplate)
   - 输出解析器
   - 本地模型调用
3. **Chapter 03**: Chains 模块
   - LCEL 语法理解
   - 传统 Chain 使用
   - 基于 LCEL 的 Chains 类型
4. **Chapter 04**: Memory 模块
   - 基础 Memory 使用
   - 其他 Memory 模块
5. **Chapter 05**: Tools 模块
   - 自定义工具
   - 大模型分析工具调用
6. **Chapter 06**: Agents 模块
   - 传统方式调用工具

## 🛠️ 技术栈

- **LangChain**: 大语言模型应用开发框架
- **uv**: 快速的 Python 包管理器和解析器
- **Jupyter Notebook**: 交互式编程环境
- **Python 3.x**: 编程语言

## 📝 使用说明

1. 每个章节的代码都在 `src/longchain_learn/` 对应的目录下
2. 使用 Jupyter Notebook 打开 `.ipynb` 文件进行交互式学习
3. 参考 `docs/` 目录下的 PDF 文档获取详细理论说明
4. 在运行代码前，请确保已正确配置 API Keys

## 🔧 开发工具

- 包管理器: `uv`
- 虚拟环境: `uv` 自动管理
- 代码格式: 遵循 Python PEP8 规范

## 📄 许可证

本项目仅用于学习目的，遵循原教程的版权声明。

## 🙏 致谢

- 感谢[尚硅谷](https://space.bilibili.com/302417610)提供的优质 LangChain 教程
- 感谢 LangChain 社区提供的强大框架支持

---

**注意**: 请妥善保管您的 API Keys，不要上传到公开仓库。

