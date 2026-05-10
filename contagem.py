
import time
print("Contagem")
for i in range(5):
    print(5 - i, end="\r")
    time.sleep(1)

print("Acabou")