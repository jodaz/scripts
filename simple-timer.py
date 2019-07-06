import time
import webbrowser 

rounds      = int(input("Reps: "))
time_work   = int(input("Work session length: ")) * 60
time_rest   = int(input("Rest session length: ")) * 60

for i in range(rounds):
    print()
    print("Session %s started" % i)
    webbrowser.open("alert-start.html")
    time.sleep(time_work)
    webbrowser.open("alert-end.html")
    time.sleep(time_rest)
    print("Session %s finished" % i)
    
print("Sessions finished")
