

def title():
    return """# Showcase\n\n"""

def colors():
    return """## Colors\n\nColors"""


def colormaps():
    return """## Colormaps\n\nColormaps"""


def source():
    return """## Source\n\nA small portion of these color themes were sourced from color design websites, including <a href="https://coolors.co/">coolors.co</a> and <a href="https://www.canva.com/">canva.com</a>. Thanks!"""


def notice():
    return """\n---\n🤖 This file was autogenerated by `scripts/gen_readme.py`."""


def build_readme():
    readme = '\n\n'.join([title(), colors(),  colormaps(), source(), notice()])
    return readme


if __name__ == '__main__':
    readme = build_readme()
    with open('matplotlib_colors/README.md', 'w', encoding="utf-8") as f:
        f.write(readme)
