def parse_student(line):
    """将一行 "姓名,成绩" 解析为字典，无效记录抛 ValueError。"""
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量错误: {len(parts)}")
    name, score_str = parts
    if not name.strip():
        raise ValueError("姓名为空")
    score = int(score_str)
    if not 0 <= score <= 100:
        raise ValueError(f"成绩 {score} 超出 0~100 范围")
    return {"name": name.strip(), "score": score}
