x = 101 #Global Variable/scope

def func():
  x = 102
  print(x)

func()
print(x)