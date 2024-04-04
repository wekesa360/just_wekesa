import time
time = time.time()

ts = time()

file = open("just_wekesa.txt", "w")
file.write("Time of run | ")
file.write(str(ts))
file.close()
