# summy4bobo

本仓库不直接提交课程 `.pptx` 二进制文件，避免在 PR 中出现“未显示二进制文件 / 不支持二进制文件”的评审问题。

## 先进入仓库目录（关键）

你必须先 `cd` 到仓库目录再运行脚本。macOS 示例：

```bash
cd ~/summy4bobo
```

## 生成 Day 1 课程 PPT

优先使用 `python3`（macOS 通常没有 `python` 命令）：

```bash
python3 tools/generate_day1_ppt.py
```

默认输出路径：

- `build/Day1_OpenClaw_安装部署与首个任务_课程讲解PPT.pptx`

生成后可直接打开（macOS）：

```bash
open "build/Day1_OpenClaw_安装部署与首个任务_课程讲解PPT.pptx"
```

也可以自定义输出路径：

```bash
python3 tools/generate_day1_ppt.py -o "./Day1_OpenClaw_安装部署与首个任务_课程讲解PPT.pptx"
```

## 课程文档

- 录播课脚本：`Day1_OpenClaw_安装部署与首个任务_录播课脚本.md`
- PPT 生成器：`tools/generate_day1_ppt.py`
