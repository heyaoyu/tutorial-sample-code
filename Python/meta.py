def with_metaclass(meta, *bases):
    return meta("NewBase", bases, {})

class TestMeta(type):

    def __new__(meta, name, bases, attrs):
        print meta.__name__
        print name
        print bases
        print attrs
        new_class = super(TestMeta, meta).__new__(meta, name, bases, attrs)
        new_class.meta_func()
        return new_class

    def meta_func(cls):
        print "func"+cls.__name__

#class UsingTestMeta(object):
#    __metaclass__ = TestMeta

class UsingTestMeta2(with_metaclass(TestMeta)):
    pass