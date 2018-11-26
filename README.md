# 编写单元测试
* 我们需要编写一个测试类，从unittest.TestCase继承。
* 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
* 对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。


### Mock的安装和导入
* 在Python 3.3以前的版本中，需要另外安装mock模块，可以使用pip命令来安装：


    $ sudo pip install mock
* 然后在代码中就可以直接import进来：


    import mock


* 从Python 3.3开始，mock模块已经被合并到标准库中，被命名为unittest.mock，可以直接import进来使用：


    from unittest import mock

* Mock对象是mock模块中最重要的概念。Mock对象就是mock模块中的一个类的实例，这个类的实例可以用来替换其他的Python对象，来达到模拟的效果。Mock类的定义如下：


    class Mock(spec=None, side_effect=None, return_value=DEFAULT, wraps=None, name=None, spec_set=None, **kwargs)

* name: 这个是用来命名一个mock对象，只是起到标识作用，当你print一个mock对象的时候，可以看到它的name。

* return_value: 这个我们刚才使用过了，这个字段可以指定一个值（或者对象），当mock对象被调用时，如果side_effect函数返回的是DEFAULT，则对mock对象的调用会返回return_value指定的值。

* side_effect: 这个参数指向一个可调用对象，一般就是函数。当mock对象被调用时，如果该函数返回值不是DEFAULT时，那么以该函数的返回值作为mock对象调用的返回值。

###patch和patch.object
> 在了解了mock对象之后，我们来看两个方便测试的函数：patch和patch.object。这两个函数都会返回一个mock内部的类实例，这个类是class _patch。返回的这个类实例既可以作为函数的装饰器，也可以作为类的装饰器，也可以作为上下文管理器。使用patch或者patch.object的目的是为了控制mock的范围，意思就是在一个函数范围内，或者一个类的范围内，或者with语句的范围内mock掉一个对象。