import inspect


class Test:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("I'm here!")

test_class = Test('aloha')

def introspection_info(obj):

    obj_type = type(obj)
    obj_attr = dir(obj)
    obj_mod = inspect.getmodule(obj)
    obj_call = callable(obj)
    obj_hasattr = hasattr(obj, 'name')
    introspection_dict = {'Тип': obj_type, 'Атрибуты': obj_attr, 'Модуль': obj_mod,
                          'Вызов': obj_call, 'Наличие атрибута "имя"': obj_hasattr}
    print(introspection_dict)


introspection_info(test_class)
