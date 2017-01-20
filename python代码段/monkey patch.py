# coding=utf-8
"""
实现猴子补丁的基础
python中所有的东西都是object，包括基本类型。查看一个object的所有属性的方法是：dir(obj)
函数在python中可以像使用变量一样对它进行赋值等操作。
 当我们import一个module时，python会做以下几件事情


  •导入一个module
  •将module对象加入到sys.modules，后续对该module的导入将直接从该dict中获得
  •将module对象加入到globals dict中


当我们引用一个模块时，将会从globals中查找。这里如果要替换掉一个标准模块，我们得做以下两件事情


    1.将我们自己的module加入到sys.modules中，替换掉原有的模块。如果被替换模块还没加载，那么我们得先对其进行加载，否则第一次加载时，还会加载标准模块。（这里有一个import hook可以用，不过这需要我们自己实现该hook，可能也可以使用该方法hook module import）
    2.如果被替换模块引用了其他模块，那么我们也需要进行替换，但是这里我们可以修改globals dict，将我们的module加入到globals以hook这些被引用的模块。
"""
"""
def originalFunc():
    print 'this is original function!'


def modifiedFunc():
    modifiedFunc = 1
    print 'this is modified function!'


def main():
    originalFunc()


if __name__ == '__main__':
    originalFunc = modifiedFunc
    main()