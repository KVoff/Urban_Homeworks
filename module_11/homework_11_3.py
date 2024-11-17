def introspection_info(obj):
    """
    Возвращает подробную информацию об объекте.

    :param obj: Объект для интроспекции.
    :return: Словарь с информацией об объекте.
    """
    import inspect

    # Основные свойства объекта
    obj_type = type(obj).__name__
    obj_module = getattr(obj, '__module__', 'built-in')

    # Получение атрибутов.
    attributes = [attr for attr in dir(obj) if
                  not callable(getattr(obj, attr)) and not attr.startswith(
                      "__")]

    # Получение методов.
    methods = [attr for attr in dir(obj) if
               callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Дополнительные свойства, если объект является классом
    if inspect.isclass(obj):
        base_classes = [base.__name__ for base in obj.__bases__]
    else:
        base_classes = None

    # Итоговый словарь.
    result = {
        'type': obj_type,
        'module': obj_module,
        'attributes': attributes,
        'methods': methods,
        'base_classes': base_classes,
    }

    return result


# С числом.
number_info = introspection_info(42)
print("Информация о числе:")
print(number_info)


# Класс для проверки.
class MyClass:
    def __init__(self, name):
        self.name = name
        self.value = 42

    def greet(self):
        return f"Hello, {self.name}!"


# Использование с объектом класса.
my_object = MyClass("Python")
object_info = introspection_info(my_object)
print("\nИнформация об объекте класса MyClass:")
print(object_info)

# Использование с классом.
class_info = introspection_info(MyClass)
print("\nИнформация о классе MyClass:")
print(class_info)
