import inspect


def introspection_info(obj):

    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    obj_module = inspect.getmodule(obj)
    module_name = obj_module.__name__ if obj_module else None

    result = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module_name
    }

    return result

number_info = introspection_info(42)
print(number_info)
