#-*-coding=utf-8-*-
#文本块生成器
"""
将文本之间块分开
"""
"""
def lines(file):
    for line in file:
        yield line
        yield  "\n"
def blocks(file):
    block=[]
    for line in lines(file):
        if line.strip():
            block.append(line)
        else:
            yield "".join(block).strip()
            block=[]