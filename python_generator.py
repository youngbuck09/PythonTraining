def fun():
    var=10
    yield var
    var=var+10
    yield var
    var=var+10
    yield var

f=fun()
print(next(f))
print(next(f))
print(next(f))


##def fun():
##    var=10
##    return var
##    var+=10
##    return var
##    var+=10
##    return var
##
##f=fun()
##print(f)
##print(f)
##print(f)
