import threading, time
print("start of program")

def takeNap():
    time.sleep(5)
    print("Wake up")
    
threadObj = threading.Thread(tagrget=takeNap)
threadObj.start()

print("end of program")

#passing arguments to the thread's target function
print('cats', 'dogs', 'frogs', sep='&')
threadObj = threading.Thread(target=print, args=['cats', 'dogs', 'frogs'], kwargs={'sep': '&'})
threadObj.start()

