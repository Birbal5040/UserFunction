# def sum_numbers(*args):
#       print(type(args))
#   print(args)

#   sum = 0
#   for num in args :
#     sum +=num
#   return sum

# print(sum_numbers(1,2,3,4,5))


# def fn(a,b,*args):
#     print(a)
#     print(b)
#     print(args)
#     print(*args)


# fn(5,6,7,8,9)


# def fn(*args,a,b):  this is give a eroor
#     print(a)
#     print(b)
#     print(args)
#     print(*args)


# fn(5,6,7,8,9)



# def fn(*args,a,b):
#     print(a)
#     print(b)
#     print(args)
#     print(*args)


# fn(5,6,7,a=8,b=9)



# def display_info(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

#     for key, value in kwargs.items():
#         print(key ," -> " ,value)

# display_info(name="Birbal", age=19, city = "DCE,Darbhanga")




# def func (a, b, *args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)


# func(5,6,7,8,9,name="Birbal", age=19)



# def func1(**kwargs, a,b):  # this is gives error message
#     print(kwargs)
#     print(a)
#     print(b)


# func1(name="Birbal",age=9, 7,9)



# def add_numbers(a : int,b : int)-> int :
#     return a+b

# print(add_numbers(5.5,7.7))





def outer():
    print("Hello from the outer")

    def inner():
        print("Hello from the inner")

    return inner

fn = outer()
print("  ")
fn()
print("  ")
outer()()