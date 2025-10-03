import os


def generate_dir_structure(path, prefix="", ignore_dirs=None):
    """
    生成目录树结构
    :param path: 起始路径
    :param prefix: 前缀，用于绘制树枝
    :param ignore_dirs: 需要忽略的目录列表
    """
    if ignore_dirs is None:
        ignore_dirs = [".git", "__pycache__", ".idea", ".venv"]  # 常见可忽略目录

    # 获取路径下所有文件和文件夹，并排序
    try:
        entries = os.listdir(path)
    except PermissionError:
        return
    entries.sort()  # 按字母顺序排序

    # 过滤掉需要忽略的目录
    entries = [e for e in entries if e not in ignore_dirs]

    for index, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        # 判断是否是最后一个条目，用于绘制分支图形
        is_last = index == len(entries) - 1

        # 当前层级的前缀
        print(prefix + ("└── " if is_last else "├── ") + entry)

        # 如果是目录，则递归处理，并更新前缀
        if os.path.isdir(full_path):
            extension = "    " if is_last else "│   "
            generate_dir_structure(full_path, prefix + extension, ignore_dirs)


if __name__ == "__main__":
    start_path = (
        input("请输入要生成目录树的路径（直接回车使用当前路径）: ").strip() or "."
    )
    print(f"目录树: {os.path.abspath(start_path)}")
    generate_dir_structure(start_path)
