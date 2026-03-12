import argparse
from datetime import UTC, datetime
from pathlib import Path
import zipfile
from xml.sax.saxutils import escape

DEFAULT_OUTPUT = Path("build/Day1_OpenClaw_安装部署与首个任务_课程讲解PPT.pptx")

SLIDES = [
    ("Day 1｜OpenClaw 零门槛上手", ["安装部署 + 第一个任务（网页/文档摘要）", "课程讲解用 PPT"]),
    ("本课定位", ["适合人群：零命令行经验的新手与办公/运营/内容从业者", "课程时长：25～35 分钟（录播建议）", "核心目标：安装 → 启动 → 跑通首个 AI 任务", "学习策略：先求第一次成功，再做功能进阶"]),
    ("学习成果（学完即得）", ["OpenClaw 成功启动截图 1 张", "摘要任务输入与输出截图 1 组", "50～100 字复盘：问题、排查、收获"]),
    ("课程流程总览", ["模块 1：开场与心理建设（3 分钟）", "模块 2：下载与安装 OpenClaw（8～10 分钟）", "模块 3：图形界面认识（5 分钟）", "模块 4：实操任务——网页/文档摘要（10～12 分钟）", "模块 5：收尾与作业（3～5 分钟）"]),
    ("模块 1｜开场与心理建设", ["今天不写代码、不用终端、不讲复杂原理", "唯一目标：跑通一次任务，建立正反馈", "讲师话术：你今天只要会点鼠标，就能完成流程", "讲师话术：先不追求复杂功能，先追求第一次成功"]),
    ("模块 2｜下载与安装（步骤）", ["打开课程下载页 / 企业网盘链接", "按系统选择安装包（Windows / macOS）", "双击安装，默认“下一步”完成部署", "首次启动遇到权限弹窗：点击“允许/仍要打开”"]),
    ("模块 2｜常见问题排查", ["安装包打不开：重新下载 + 核对系统版本", "安全策略拦截：在“隐私与安全性”中允许应用", "白屏或卡住：等待 30～60 秒后重启并检查网络", "讲师强调：问题正常，按清单逐项排查"]),
    ("模块 3｜界面认知四件套", ["任务输入区：填写网页链接或粘贴文档", "模型/能力选项区：选择“摘要/总结”模板", "运行按钮：开始执行任务", "输出结果区：查看、复制、导出摘要"]),
    ("模块 4｜实操任务步骤", ["准备素材：公开网页链接或 1000～3000 字文档", "选择“摘要/总结”任务模板", "粘贴链接/文档并设置输出格式", "点击运行并进行人工校验（准确性/完整性/可读性）", "导出结果，作为课堂成果提交"]),
    ("推荐输出格式（统一模板）", ["3 句话总结核心内容", "5 个关键要点", "1 条可立即执行建议", "全程使用简体中文，避免空话"]),
    ("示例提示词（可直接复制）", ["请阅读以下内容并输出：", "1）用 3 句话概括核心内容；", "2）提炼 5 个关键要点；", "3）给出 1 条可立即执行的建议；", "4）全程使用简体中文，避免空话。"]),
    ("录播与作业", ["分镜建议：开场→安装→界面认识→实操→收尾", "录制前检查：麦克风、1080p、素材与账号", "后期重点：高亮关键点击 + 易错点提示卡", "课后作业：再做一次岗位相关摘要并优化提示词"]),
]


def make_slide_xml(title: str, bullets: list[str]) -> str:
    title = escape(title)
    bullet_xml = ""
    for line in bullets:
        line = escape(line)
        bullet_xml += (
            '<a:p><a:pPr lvl="0"><a:buChar char="•"/></a:pPr>'
            f'<a:r><a:rPr lang="zh-CN" sz="2400"/><a:t>{line}</a:t></a:r>'
            '<a:endParaRPr lang="zh-CN"/></a:p>'
        )

    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      <p:sp>
        <p:nvSpPr><p:cNvPr id="2" name="Title 1"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="457200" y="274320"/><a:ext cx="11277600" cy="914400"/></a:xfrm></p:spPr>
        <p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="zh-CN" sz="4000" b="1"/><a:t>{title}</a:t></a:r><a:endParaRPr lang="zh-CN"/></a:p></p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr><p:cNvPr id="3" name="Content 2"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="685800" y="1371600"/><a:ext cx="10858560" cy="4937760"/></a:xfrm></p:spPr>
        <p:txBody><a:bodyPr/><a:lstStyle/>{bullet_xml}</p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>'''


def generate(output_path: Path) -> None:
    now = datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    content_types = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n',
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">\n',
        '  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>\n',
        '  <Default Extension="xml" ContentType="application/xml"/>\n',
        '  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>\n',
        '  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>\n',
        '  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>\n',
    ]
    for i in range(1, len(SLIDES) + 1):
        content_types.append(
            f'  <Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>\n'
        )
    content_types.append('</Types>')

    rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''

    core = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>Day1 OpenClaw 课程讲解PPT</dc:title>
  <dc:creator>Codex</dc:creator>
  <cp:lastModifiedBy>Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>
</cp:coreProperties>'''

    app = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office PowerPoint</Application>
  <Slides>{len(SLIDES)}</Slides>
  <Notes>0</Notes>
  <HiddenSlides>0</HiddenSlides>
</Properties>'''

    slide_ids = "\n".join([f'    <p:sldId id="{255 + i}" r:id="rId{i}"/>' for i in range(1, len(SLIDES) + 1)])
    presentation = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldIdLst>
{slide_ids}
  </p:sldIdLst>
  <p:sldSz cx="12192000" cy="6858000" type="screen16x9"/>
  <p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>'''

    presentation_rels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n']
    for i in range(1, len(SLIDES) + 1):
        presentation_rels.append(
            f'  <Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>\n'
        )
    presentation_rels.append('</Relationships>')

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", "".join(content_types))
        zf.writestr("_rels/.rels", rels)
        zf.writestr("docProps/core.xml", core)
        zf.writestr("docProps/app.xml", app)
        zf.writestr("ppt/presentation.xml", presentation)
        zf.writestr("ppt/_rels/presentation.xml.rels", "".join(presentation_rels))

        for i, (title, bullets) in enumerate(SLIDES, start=1):
            zf.writestr(f"ppt/slides/slide{i}.xml", make_slide_xml(title, bullets))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Day 1 OpenClaw PPTX.")
    parser.add_argument("-o", "--output", type=Path, default=DEFAULT_OUTPUT, help=f"output pptx path (default: {DEFAULT_OUTPUT})")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    generate(args.output)
    print(f"Generated: {args.output}")
