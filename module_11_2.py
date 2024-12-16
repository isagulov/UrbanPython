def introspection_info(obj):
    obj += 3
    return obj

print(type(introspection_info))
print(dir(introspection_info))
print(introspection_info.__module__)