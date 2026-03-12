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

## 常见报错排查（你这次遇到的就是这一类）

### 报错 1：`can't open file ... tools/generate_day1_ppt.py`

这通常表示你当前本地仓库里还没有这个脚本（分支不对或没拉到最新提交）。按下面顺序执行：

```bash
cd ~/summy4bobo
git remote -v
git fetch --all --prune
git branch -a
```

然后切到包含课程文件的分支（例如 `work`）：

```bash
git checkout work || git checkout -b work origin/work
git pull
```

再确认文件存在：

```bash
ls -lh tools/generate_day1_ppt.py
ls -lh "Day1_OpenClaw_安装部署与首个任务_录播课脚本.md"
```

### 报错 2：`The file ... build/...pptx does not exist`

这是因为上一步脚本没有成功执行，或者你不在仓库目录。重新执行：

```bash
cd ~/summy4bobo
python3 tools/generate_day1_ppt.py
ls -lh "build/Day1_OpenClaw_安装部署与首个任务_课程讲解PPT.pptx"
open "build/Day1_OpenClaw_安装部署与首个任务_课程讲解PPT.pptx"
```

## 课程文档

- 录播课脚本：`Day1_OpenClaw_安装部署与首个任务_录播课脚本.md`
- PPT 生成器：`tools/generate_day1_ppt.py`
