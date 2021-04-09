import hashlib
import time 

salt = "e361bfc569ba48dc" # Change this Accordingly 

i = 100000000
strttime = time.perf_counter()
print("Starting Hash Bruteforce")
while True:
    password = f"{salt}{i}".encode('utf8')

    NewHash = hashlib.md5(password).hexdigest()
    if NewHash[0:2] == "0e" and NewHash[2:32].isdigit():
        print(f"Password : {password}\nValue of I : {i}\nNewHash : {NewHash}")
        endtime = time.perf_counter()
        print(f"Time Elapsed : {int(endtime - strttime)/ 60} Minutes")
        print(f"Script Finshed , Enjoy :D")
        break
    i += 1
    print(i)