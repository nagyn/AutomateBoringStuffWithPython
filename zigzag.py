# Write your code here :-)
import sys, time
indent = 0
increase = True

while True:
    time.sleep(0.1)
    print(" " * indent + "********")
    if increase:
        indent += 1
        if indent == 10:
            increase = False
    else:
        indent -= 1
        if indent == 0:
            increase = True
