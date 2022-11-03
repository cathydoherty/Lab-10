#Cathy Doherty and Amanda Miloserny
def my_get_method (k, d, default):
    if k in d:
        return d[k]
    else:
        return default
d= {"x":1, "y":2, "z":3}

print (my_get_method("x", d, 5))

print (my_get_method("g", d, 10))

print (my_get_method(False, d, 90))
