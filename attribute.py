# coding:utf-8
'''
学习class的几个常用属性
__author__ = suwenkui
'''
class A(object):
    pass

if __name__ == '__main__':
    a = A()

    dir(a)
    print 'object a is:',a
    print 'dir a',dir(a)
    #print 'dir A',dir(A)
    '''
    object a is: <__main__.A object at 0x7fa2ff189fd0>
dir a ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
dir A ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
    '''
