memory = 0

def memory_clear():
    global memory
    memory = 0

def memory_recall():
    return memory

def memory_store(value):
    global memory
    memory = value

def memory_add(value):
    global memory
    memory += value
