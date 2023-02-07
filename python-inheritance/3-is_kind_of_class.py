def is_kind_of_class(obj, a_class):
    """ True if the object is an instance or is an instance of /
    a class that inherited from, the specified class, otherwise False """
    if type(obj) is a_class or issubclass(type(obj), a_class):
        return True
    else:
        return False
# issubclas permite verificar si una clase es una subclase de otra clase
