#Stack
#Queue
#Linked List
#Binary tree
#Dictionaries

stack = []
stackTailPointer = -1
stackHeadPointer = -1

def push(val):
    global stackTailPointer
    global stackHeadPointer
    if stackTailPointer == 9:
        print("Stack is full")
    else:
        stack.append(val)
        if stackHeadPointer == -1:
            stackHeadPointer += 1
        stackTailPointer+=1

def pop():
    global stackTailPointer
    global stackHeadPointer
    if stackHeadPointer == -1:
        print("Stack is empty")
    else:
        removed = stack[stackTailPointer]
        stack.remove(stack[stackTailPointer])
        stackTailPointer -=1
        if stackTailPointer == -1:
            stackHeadPointer -=1
        return removed

queue = [-1 for i in range(10)]
queueTailPointer = -1
queueHeadPointer = int(input("Set the head pointer: "))
spaces = 10

def enqueue(val):
    global queueTailPointer
    global queueHeadPointer
    if spaces == 0:
        print("Queue is full")
    else:
        queue[queueHeadPointer] = val
        if queueHeadPointer == -1:
            queueHeadPointer += 1
        queueTailPointer+=1

def dequeue():
    global queueTailPointer
    global queueHeadPointer
    if queueHeadPointer == -1:
        print("Queue is empty")
    else:
        removed = queue[queueTailPointer]
        queue.remove(queue[queueTailPointer])
        queueTailPointer -=1
        if queueTailPointer == -1:
            queueHeadPointer -=1
        return removed
    

engldictionary = {
    "aerobic" : 300,
    "kazakhstan" : 600,
    "zigzag" : 900,
    }

