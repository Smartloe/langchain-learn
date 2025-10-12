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
│   ├── chapter01-summary/        # LangChain 概述和 Hello World
│   ├── chapter02-model IO/       # Model IO 模块
│   │   ├── 01-模型的调用.ipynb
│   │   ├── 02-再谈模型的调用.ipynb
│   │   ├── 03-提示词模板之Prompt Template.ipynb
│   │   ├── 04-提示词模板之ChatPromptTemplate.ipynb
│   │   ├── 05-提示词模板之少量示例的提示词模板.ipynb
│   │   ├── 06-从文档中加载Prompt.ipynb
│   │   ├── 07-输出解析器的使用.ipynb
│   │   ├── 08-LangChain调用本地模型.ipynb
│   │   └── prompt/               # 提示词模板文件
│   ├── chapter03-Chains/         # Chains 模块
│   │   ├── 01-LCEL语法的理解.ipynb
│   │   ├── 02-传统的chain的使用.ipynb
│   │   └── 03-基于LCEL构建的Chains的类型.ipynb
│   ├── chapter04-Memory/         # Memory 模块
│   │   ├── 01-使用Memoery模块之前.ipynb
│   │   ├── 02-基础Memory模块的使用.ipynb
│   │   └── 03-其他Memory模块的使用.ipynb
│   ├── chapter05-Tools/          # Tools 模块
│   │   ├── 01-自定义工具.ipynb
│   │   ├── 02-大模型分析工具的调用.ipynb
│   │   └── a.txt
│   ├── chapter06-Agents/         # Agents 模块
│   │   ├── 01-调用工具之传统方式的使用.ipynb
│   │   ├── 02-调用工具之通用方式的使用.ipynb
│   │   ├── 03-Agent嵌入记忆之传统方式的使用.ipynb
│   │   └── 04-Agent嵌入记忆之通用方式的使用.ipynb
│   └── chapter07-Retrieval/      # Retrieval 模块
│       ├── 01-文档加载器 Document Loaders的使用.ipynb
│       ├── 02-文档拆分器 Text Splitters的使用.ipynb
│       ├── 03-文档嵌入模型Text Embedding Models的使用.ipynb
│       ├── 04-向量数据库的使用.ipynb
│       ├── 05-检索器(召回器) Retrievers的使用.ipynb
│       ├── 06-综合案例：智能对话助手.ipynb
│       ├── 07-综合案例：知识库问答助手.ipynb
│       └── asset/                # 资源文件
│           ├── chroma_db/        # 向量数据库文件
│           └── load/             # 文档加载示例文件
├── docs/                         # 学习文档和资料
│   ├── 01-LangChain使用概述.pdf
│   ├── 02-LangChain使用之Model IO.pdf
│   ├── 03-LangChain使用之Chains.pdf
│   ├── 04-LangChain使用之Memory.pdf
│   ├── 05-LangChain使用之Tools.pdf
│   ├── 06-LangChain使用之Agents.pdf
│   ├── 07-LangChain使用之Retrieval.pdf
│   └── 傻妞的使用说明书.md
├── examples/                     # 示例文件
│   └── 广电套餐合集.pdf
├── tests/                        # 测试代码
│   ├── 01-大模型的异步调用.py
│   ├── Tests01.py
│   ├── tests02.py
│   ├── tests03.py
│   └── 项目的目录结构读取.py
├── main.py                       # 主程序入口
├── pyproject.toml               # 项目配置
├── uv.lock                      # 依赖锁定文件
├── .env                         # 环境变量（本地配置）
├── .gitignore                   # Git忽略文件
└── .python-version             # Python版本配置
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

在项目根目录创建或更新 `.env` 文件，添加所需的大模型 API Key：

```env
OPENAI_API_KEY=your_openai_api_key_here
OTHER_API_KEY=your_other_api_key_here
```

⚠️ **注意**: 出于安全考虑，`.env` 文件已添加到 `.gitignore`，不会被上传到 GitHub。

### 运行项目

```bash
# 运行主程序
python main.py

# 或使用 Jupyter Notebook 运行各章节代码
jupyter notebook
```

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
   - 通用方式调用工具
   - Agent 嵌入记忆功能
7. **Chapter 07**: Retrieval 模块
   - 文档加载器使用
   - 文档拆分器使用
   - 文档嵌入模型
   - 向量数据库使用
   - 检索器使用
   - 综合案例：智能对话助手
   - 综合案例：知识库问答助手

## 🛠️ 技术栈

- **LangChain**: 大语言模型应用开发框架
- **uv**: 快速的 Python 包管理器和解析器
- **Jupyter Notebook**: 交互式编程环境
- **Python 3.x**: 编程语言
- **ChromaDB**: 向量数据库
- **多种文档格式支持**: PDF, CSV, JSON, HTML, Markdown 等

## 📝 使用说明

1. 每个章节的代码都在 `src/longchain_learn/` 对应的目录下
2. 使用 Jupyter Notebook 打开 `.ipynb` 文件进行交互式学习
3. 参考 `docs/` 目录下的 PDF 文档获取详细理论说明
4. 在运行代码前，请确保已正确配置 API Keys
5. 测试代码位于 `tests/` 目录，可用于验证功能
6. 示例文档位于 `examples/` 目录，用于测试文档处理功能

## 🔧 开发工具

- 包管理器: `uv`
- 虚拟环境: `uv` 自动管理
- 代码格式: 遵循 Python PEP8 规范
- 开发环境: Jupyter Notebook

## 🧪 测试

项目包含多个测试文件，位于 `tests/` 目录：

```bash
# 运行测试
python tests/Tests01.py
python tests/tests02.py
python tests/tests03.py
```

## 📄 许可证

本项目仅用于学习目的，遵循原教程的版权声明。

## 🙏 致谢

- 感谢[尚硅谷](https://space.bilibili.com/302417610)提供的优质 LangChain 教程
- 感谢 LangChain 社区提供的强大框架支持
- 感谢所有开源项目的贡献者

---

**开始你的 LangChain 学习之旅吧！** 🚀