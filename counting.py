loop_running = True
arr = []
while loop_running:
    user_input = int(input("give number or zero to quit").strip())
    if user_input == 0:
        loop_running = False
    else:
        arr.append(user_input)
print(arr)
for p in arr:
    print (p)
    for j in range(1,p+1):
        print (j*5)