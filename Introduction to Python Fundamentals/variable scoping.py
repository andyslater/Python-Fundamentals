count = 0

def show_count():
    print("count = ", count)

def set_count(c):
    count = c # only sets the local variable

def set_count_global(c):
    global count # will set the global variable
    count = c

show_count()
set_count(22)
show_count() # only the local is changed
set_count_global(23)
show_count() # the global is changed