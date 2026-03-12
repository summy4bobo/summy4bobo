# summy4bobo

本仓库不直接提交课程 `.pptx` 二进制文件，避免在 PR 中出现“未显示二进制文件 / 不支持二进制文件”的评审问题。

## 生成 Day 1 课程 PPT

```bash
python tools/generate_day1_ppt.py
```

默认输出路径：

- `build/Day1_OpenClaw_安装部署与首个任务_课程讲解PPT.pptx`

也可以自定义输出路径：

```bash
python tools/generate_day1_ppt.py -o "./Day1_OpenClaw_安装部署与首个任务_课程讲解PPT.pptx"
```

## 课程文档

- 录播课脚本：`Day1_OpenClaw_安装部署与首个任务_录播课脚本.md`
- PPT 生成器：`tools/generate_day1_ppt.py`
