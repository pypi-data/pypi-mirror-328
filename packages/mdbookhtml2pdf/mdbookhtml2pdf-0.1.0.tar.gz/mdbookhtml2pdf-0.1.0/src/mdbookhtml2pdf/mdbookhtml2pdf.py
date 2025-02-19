import asyncio
from bs4 import BeautifulSoup
import os
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, TextLexer, guess_lexer
from pygments.util import ClassNotFound
import subprocess
from weasyprint import HTML
import tempfile
import re
import time
import toml
from datetime import datetime
import hashlib
import shutil
import sys

# 异步函数：生成目录
async def generate_toc(soup):
    """生成目录"""
    # 获取内容div
    content_div = soup.find('div', id='content')
    if not content_div:
        return

    # 创建目录容器
    toc = soup.new_tag('article')
    toc['id'] = 'contents'

    # 添加目录标题
    title = soup.new_tag('h2')
    title.string = '目录'
    toc.append(title)

    # 创建部分标题和列表
    headers = content_div.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    # 用于跟踪每个级别的索引
    current_indices = [0] * 6

    for header in headers:
        # 为每个标题生成唯一ID（如果没有的话）
        if not header.get('id'):
            header['id'] = f'header-{hash(header.get_text())}'

        # 根据标题级别组织部分
        level = int(header.name[1])  # h1=1, h2=2, ...

        # 更新当前级别的索引
        current_indices[level - 1] += 1

        # 重置下级别的索引
        for i in range(level, 6):
            current_indices[i] = 0

        # 生成前缀
        prefix = '.'.join(str(i) for i in current_indices if i > 0)

        # 处理 h1 标签
        if level == 1:
            # 处理 h1 标签
            current_h1 = soup.new_tag('a')
            current_h1['href'] = f'#{header["id"]}'
            current_h1['class'] = 'toc_section'
            current_h1.string = f'{prefix} {header.get_text()}'
            toc.append(current_h1)

            # 创建一个新的列表
            ul = soup.new_tag('ul')
            toc.append(ul)
        else:
            # 处理 h2-h6 标签
            li = soup.new_tag('li')
            link = soup.new_tag('a')
            link['href'] = f'#{header["id"]}'
            link.string = f'{prefix} {header.get_text()}'
            li.append(link)
            ul.append(li)  # 将链接添加到当前 h1 的列表中

# 添加目录样式
    style = soup.find('style')
    if not style:
        style = soup.new_tag('style')
        soup.head.append(style)
        style.string = ""

    # 添加目录样式
    toc_style = """
h2,
h3,
h4,
h5,
h6 {
  page-break-before: always;
  page-break-after: avoid;
}

a.toc_section::before {
  background: #fbc847;
  display: block;
  content: '';
  height: .08cm;
  margin-bottom: .25cm;
  width: 100%;
}

a.toc_section {
  font-weight: 500;
  margin: 3em 0 1em;
}

#contents {
    break-before: right;
    break-after: left;
    page: no-chapter;
}

#contents h2 {
    font-size: 20pt;
    font-weight: 400;
    margin-bottom: 3cm;
}

#contents a {
    font-weight: 500;
    display: block;  /* 使a表现得像块元素 */
    margin: 1em 0;  /* 添加间距 */
}

#contents ul {
    list-style: none;
    padding-left: 0;
}

#contents ul li {
    border-top: .25pt solid #c1c1c1;
    margin: .25cm 0;
    padding-top: .25cm;
}

#contents ul li a::before {
    color: #fbc847;
    content: '• ';
    font-size: 40pt;
    line-height: 16pt;
    vertical-align: bottom;
}

#contents ul li a {
    color: inherit;
    text-decoration-line: inherit;
}

#contents ul li a::after {
    color: #fbc847;
    content: target-counter(attr(href), page);
    float: right;
}
"""

    if style.string is None:
        style.string = toc_style
    else:
        style.string += toc_style

    return toc

# 异步函数：处理代码高亮
async def process_code_block(code_block, soup):
    """处理代码高亮"""
    try:
        code = code_block.get_text()

        # 获取语言类型
        language = None
        if code_block.get('class'):
            for cls in code_block.get('class'):
                if cls.startswith('language-'):
                    language = cls.replace('language-', '')
                    break

        # 确定使用的样式
        style_name = 'monokai'

        try:
            if language:
                lexer = get_lexer_by_name(language)
            else:
                lexer = guess_lexer(code)
        except ClassNotFound as e:
            print(f"无法找到语言解析器: {e}")
            lexer = TextLexer()

        # 检查是否为块级元素
        is_block = code_block.parent.name == 'pre'

        # 使用特定的格式化选项
        formatter = HtmlFormatter(
            style=style_name,
            cssclass='highlight',  # 使用统一的基础类名
            nowrap=False if is_block else True,
            linenos=False,
        )

        highlighted = highlight(code, lexer, formatter)

        # 创建包装元素
        new_div = soup.new_tag('div' if is_block else 'span')
        new_div['class'] = f'highlight' if is_block else 'highlight-inline'

        # 直接使用 HTML 字符串创建新的标签
        new_code = BeautifulSoup(highlighted, 'html.parser')
        if new_code.contents:
            new_div.extend(new_code.contents)

        code_block.replace_with(new_div)

        # 添加样式（只添加一次）
        if not soup.find('style', class_='pygments-style'):
            style_tag = soup.new_tag('style')
            style_tag['class'] = 'pygments-style'

            # 生成基础高亮样式
            base_style = formatter.get_style_defs('.highlight')

            # 添加容器样式
            container_style = """
            .highlight {
                break-inside: avoid;
                display: block;
                padding: 1em;
                font-size: 8pt;
                border-radius: 4px;
                background-color:rgb(245, 246, 237);
                overflow-x: auto;
            }

            .highlight-inline {
                display: inline;
                padding: 0.1em 0.1em;
                border-radius: 3px;
                background-color: #272822;
                color: #f8f8f2;
            }

            .highlight {
                background: transparent !important;
            }

            .highlight pre {
                margin: 0;
                padding: 0;
            }

            .highlight span {
                white-space: pre;
                word-wrap: normal;
                word-break: keep-all;
            }
            """

            style_tag.string = base_style + container_style
            if soup.head:
                soup.head.append(style_tag)
            else:
                print("文档没有 <head> 标签，无法插入样式")

    except Exception as e:
        import traceback
        print(f"代码高亮处理失败: {e}")
        print(traceback.format_exc())

# 异步函数：处理mermaid图表
async def process_mermaid(mermaid_block, soup, index, output_dir):
    """处理mermaid图表"""
    mermaid_content = mermaid_block.get_text().strip()

    # 检查mermaid内容是否为空
    if not mermaid_content:
        print(f"警告: 空的mermaid块 #{index}")
        return

    # 使用MD5生成唯一的文件名
    content_hash = hashlib.md5(mermaid_content.encode('utf-8')).hexdigest()
    output_file = os.path.join(output_dir, f'mermaid_{content_hash}.png')

    # 检查文件是否已存在
    print('检查文件是否存在:', output_file)
    if os.path.exists(output_file):
        print(f"使用缓存的mermaid图片 #{index}: {os.path.basename(output_file)}")
        # 直接使用已存在的图片
        img = soup.new_tag('img')
        img['src'] = f'{output_dir}/mermaid_{content_hash}.png'
        img['class'] = 'mermaid'
        mermaid_block.replace_with(img)
        return

    # 创建临时文件存储mermaid内容
    with tempfile.NamedTemporaryFile(mode='w', suffix='.mmd', delete=False) as f:
        f.write(mermaid_content)
        mmd_file = f.name

    try:
        # 使用python subprocess调用mmdc命令，添加超时设置
        process = await asyncio.create_subprocess_exec(
            'mmdc',
            '-i', mmd_file,
            '-o', output_file,
            '-t', 'default',  # 使用默认主题
            '-b', 'transparent',  # 透明背景
            '-q', '4',  # 设置质量为4（最高质量）
            '-w', '2048',  # 设置宽度（可以根据需要调整）
            '-s', '2',  # 设置缩放比例为2（提高清晰度）
            '--pdfFit',  # 适应PDF大小
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        try:
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=30.0)

            if process.returncode == 0 and os.path.exists(output_file):
                print(f"生成新的mermaid图片 #{index}: {os.path.basename(output_file)}")
                # 创建新的img标签，使用相对路径
                img = soup.new_tag('img')
                img['src'] = f'{output_dir}/mermaid_{content_hash}.png'
                img['class'] = 'mermaid'
                mermaid_block.replace_with(img)
            else:
                print(f"Mermaid转换失败 #{index}: {stderr.decode()}")
                # 保留原始mermaid块
                print(f"原始内容: {mermaid_content[:100]}...")
        except asyncio.TimeoutError:
            print(f"Mermaid转换超时 #{index}")
            process.kill()

    except Exception as e:
        print(f"处理Mermaid图表时出错 #{index}: {e}")
    finally:
        # 清理临时文件
        try:
            os.unlink(mmd_file)
        except:
            pass

# 异步函数：生成PDF封面
async def generate_cover(book_toml_path: str, soup: BeautifulSoup) -> None:
    """生成PDF封面"""
    try:
        # 读取book.toml文件
        with open(book_toml_path, 'r', encoding='utf-8') as f:
            book_config = toml.load(f)

        # 创建封面div
        cover = soup.new_tag('div')
        cover['class'] = 'cover'

        # 添加标题
        title = soup.new_tag('h1')
        title['class'] = 'cover-title'
        title.string = book_config['book']['title']
        cover.append(title)

        # 创建信息容器
        info_container = soup.new_tag('div')
        info_container['class'] = 'cover-info'

        # 添加作者、时间和字数信息
        info_text = f"作者：{', '.join(book_config['book']['authors'])} | "
        info_text += f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        # 统计字数（可选）
        content_div = soup.find('div', id='content')
        if content_div:
            word_count = len(''.join(content_div.stripped_strings))
            info_text += f" | 总字数：{word_count:,} 字"

        info = soup.new_tag('p')
        info['class'] = 'cover-info-text'
        info.string = info_text
        info_container.append(info)

        cover.append(info_container)

        # 在内容最前面插入封面
        content_div = soup.find('div', id='content')
        if content_div:
            content_div.insert(0, cover)

    except Exception as e:
        print(f"生成封面时出错: {e}")

# 异步函数：检查是否安装了mermaid-cli工具
async def check_mermaid_cli():
    """检查是否安装了mermaid-cli工具"""
    if not shutil.which('mmdc'):
        return False
    return True

# 异步函数：处理HTML文件
async def process_html_file(html_file):
    start_time = time.time()

    # 获取book.toml路径
    book_toml_path = os.path.join(os.path.dirname(html_file), '..', 'book.toml')

    # 获取输入文件的目录
    output_dir = os.path.dirname(os.path.abspath(html_file))
    mermaid_dir = os.path.join(output_dir, 'mermaid_images')
    os.makedirs(mermaid_dir, exist_ok=True)  # 提前创建mermaid目录

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    parse_time = time.time() - start_time
    print(f"HTML解析耗时: {parse_time:.2f}秒")

    # 检查是否存在mermaid图表
    mermaid_blocks = soup.find_all('pre', class_='mermaid')
    if mermaid_blocks:
        # 如果存在mermaid图表，检查是否安装了mermaid-cli
        if not await check_mermaid_cli():
            print("\n错误: 检测到文档中包含 Mermaid 图表，但未安装 mermaid-cli 工具")
            print("请按照以下步骤安装 mermaid-cli:")
            print("\n1. 首先确保已安装 Node.js 和 npm")
            print("2. 然后运行以下命令安装 mermaid-cli:")
            print("\n   npm install -g @mermaid-js/mermaid-cli")
            print("\n安装完成后重新运行本程序")
            sys.exit(1)

    # 获取或创建content div
    content_div = soup.find('div', id='content')
    if not content_div:
        content_div = soup.new_tag('div')
        content_div['id'] = 'content'
        if soup.body:
            soup.body.append(content_div)

    # 先生成目录
    toc_start = time.time()
    toc = await generate_toc(soup)
    if toc:  # 确保目录生成成功
        content_div.insert(0, toc)  # 先插入目录
    toc_time = time.time() - toc_start
    print(f"目录生成耗时: {toc_time:.2f}秒")

    # 再生成封面（在目录之前）
    cover_time = 0
    if os.path.exists(book_toml_path):
        cover_start = time.time()
        await generate_cover(book_toml_path, soup)
        cover_time = time.time() - cover_start
        print(f"封面生成耗时: {cover_time:.2f}秒")

    # 处理代码高亮
    code_start = time.time()
    code_blocks = soup.find_all('code')
    code_tasks = [process_code_block(block, soup) for block in code_blocks]
    await asyncio.gather(*code_tasks)
    code_time = time.time() - code_start
    print(f"代码高亮处理耗时: {code_time:.2f}秒 (处理了{len(code_blocks)}个代码块)")

    # 处理mermaid图表
    mermaid_time = 0
    if mermaid_blocks:
        mermaid_start = time.time()
        semaphore = asyncio.Semaphore(2)
        async def process_mermaid_with_semaphore(block, soup, i, mermaid_dir):
            async with semaphore:
                return await process_mermaid(block, soup, i, mermaid_dir)

        mermaid_tasks = [process_mermaid_with_semaphore(block, soup, i, mermaid_dir) for i, block in enumerate(mermaid_blocks)]
        await asyncio.gather(*mermaid_tasks)
        mermaid_time = time.time() - mermaid_start
        print(f"Mermaid图表处理耗时: {mermaid_time:.2f}秒 (处理了{len(mermaid_blocks)}个图表)")

    # 添加CSS样式和保存HTML
    save_start = time.time()
    style = soup.new_tag('style')
    style.string = """
    @page {
        @bottom-right {
            background: #fbc847;
            content: counter(page);
            height: 1cm;
            text-align: center;
            width: 1cm;
        }
        @top-center {
            background: #fbc847;
            content: '';
            display: block;
            height: .05cm;
            opacity: .5;
            width: 100%;
            margin-bottom: 7pt;
        }
        @top-right {
            content: string(chapter);
            font-size: 9pt;
            height: 1cm;
            vertical-align: middle;
            width: 100%;
            margin-bottom: 7pt;
        }
    }

    html {
        color: #393939;
        font-family: Fira Sans;
        font-size: 11pt;
        font-weight: 300;
        line-height: 1.5;
    }

    .cover {
        page: cover;
    }

    @page cover {
        @bottom-center {
            content: none;
        }
    }

    /* 修改mermaid图片样式 */
    .mermaid {
        max-width: 100%;
        break-inside: avoid;
        width: auto;
        height: auto;
        image-rendering: high-quality;  /* 添加图片渲染质量设置 */
        -webkit-image-rendering: high-quality;
        -ms-image-rendering: high-quality;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        string-set: chapter content();
    }

    @media print {
        table {
            page-break-after: auto
        }

        tr {
            page-break-inside: avoid;
            page-break-after: auto
        }

        td {
            page-break-inside: avoid;
            page-break-after: auto
        }

        thead {
            display: table-header-group
        }

        tfoot {
            display: table-footer-group
        }
    }
    """
    soup.head.append(style)

    output_html = html_file.replace('.html', '_processed.html')
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    save_time = time.time() - save_start
    print(f"HTML保存耗时: {save_time:.2f}秒")

    # 生成PDF并统计页数
    pdf_start = time.time()
    pdf_path = html_file.replace('.html', '.pdf')
    html = HTML(output_html)
    pdf_document = html.write_pdf(pdf_path)

    # 使用WeasyPrint计算页数
    total_pages = len(html.render().pages)
    pdf_time = time.time() - pdf_start

    print(f"PDF生成耗时: {pdf_time:.2f}秒")
    print(f"PDF总页数: {total_pages}页")
    print(f"平均每页处理时间: {pdf_time/total_pages:.2f}秒")
    print(f"\nPDF文件已生成: {os.path.abspath(pdf_path)}")

    total_time = time.time() - start_time
    print(f"\n总耗时统计:")
    print(f"{'处理步骤':<15} {'耗时(秒)':<10} {'占比':<10}")
    print("-" * 35)
    print(f"{'HTML解析':<15} {parse_time:>10.2f} {parse_time/total_time*100:>9.1f}%")
    print(f"{'封面生成':<15} {cover_time:>10.2f} {cover_time/total_time*100:>9.1f}%")
    print(f"{'目录生成':<15} {toc_time:>10.2f} {toc_time/total_time*100:>9.1f}%")
    print(f"{'代码高亮':<15} {code_time:>10.2f} {code_time/total_time*100:>9.1f}%")
    print(f"{'Mermaid处理':<15} {mermaid_time:>10.2f} {mermaid_time/total_time*100:>9.1f}%")
    print(f"{'HTML保存':<15} {save_time:>10.2f} {save_time/total_time*100:>9.1f}%")
    print(f"{'PDF生成':<15} {pdf_time:>10.2f} {pdf_time/total_time*100:>9.1f}%")
    print("-" * 35)
    print(f"{'总计':<15} {total_time:>10.2f} {'100.0':>9}%")
    print(f"平均每页耗时: {total_time/total_pages:.2f}秒")

# 主函数
def main():
    import sys
    # 检查命令行参数个数
    if len(sys.argv) != 2:
        print("使用方法: python script.py <html文件>")  # 打印使用方法
        sys.exit(1)  # 退出脚本并返回错误代码

    html_file = sys.argv[1]  # 获取HTML文件名
    asyncio.run(process_html_file(html_file))  # 运行异步函数处理HTML文件

if __name__ == "__main__":
    main()  # 调用主函数执行脚本
