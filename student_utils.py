def parse_student(line):
    """
    解析学生记录字符串，将成绩转换为整数，并验证数据有效性。
    
    参数:
        line: 包含姓名和成绩的字符串，用逗号分隔，例如 "Alice,85"
    
    返回:
        tuple: (name, score) 姓名字符串和成绩整数
    
    抛出:
        ValueError: 当字段数量不对、姓名为空、或成绩不在 0~100 范围内时
    """
    # 去除首尾空白
    line = line.strip()
    
    # 按逗号分割字段
    parts = line.split(",")
    
    # 检查字段数量是否为 2
    if len(parts) != 2:
        raise ValueError(f"字段数量错误: 期望 2 个字段，实际得到 {len(parts)} 个")
    
    name = parts[0].strip()
    score_str = parts[1].strip()
    
    # 检查姓名是否为空
    if not name:
        raise ValueError("姓名不能为空")
    
    # 尝试将成绩转换为整数
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError(f"成绩必须是整数: '{score_str}'")
    
    # 检查成绩是否在 0~100 范围内
    if score < 0 or score > 100:
        raise ValueError(f"成绩必须在 0~100 范围内: {score}")
    
    return name, score