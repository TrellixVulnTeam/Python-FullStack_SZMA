print('把模块当成脚本来使用')
#执行一个py文件
#   在cmd执行,在python执行:直接执行这个文件-以脚本的形式运行这个文件
#   导入这个文件

#都是py文件
#   直接运行这个文件 这个文件就是一个脚本  能独立的提供一个功能,能自主完成交互
#   导入这个文件 这个文件就是模块     能够被导入调用这个功能,不能自主交互

#一个文件中的__main__变量
#       当这个文件被当做脚本执行的时候 __name__ == '__main__'
#       当这个文件被当做模块导入的时候 __name__ == '模块的名字'
print(__name__)
if __name__ == '__main__':
    print('I am executiable')