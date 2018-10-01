import sys
import random
import time
import matplotlib.pyplot as plt

n1 = input("Give the number of digits:")
n = int(n1)
max = (10 ** n) - 1
min = max * (-1)

a = [0] * 1000000
b = [0] * 1000000

for i in range(1000000):

    a[i] = random.randint(min, max)

    b[i] = random.randint(min, max)

 

start_time = time.time()

total=0

for i in range(1000000):

    result = a[i] + b[i]

    print("a[",i,"] + b[",i,"] = ",result)

    total=total+(sys.getsizeof(a[i])+sys.getsizeof(b[i])+sys.getsizeof(result)+sys.getsizeof(i))

 

print("Execution time=", time.time() - start_time)

 

print(total,"bytes")

 
#these are values found by executing above code
y=[0.1718292236328125,0.17183828353881836,0.20308160781860352,0.2187025547027588,0.2499079704284668,0.2968111038208008,0.39053893089294434,0.6404821872711182]

x=[4,8,16,32,64,128,256,512]

# plotting the points 

plt.plot(x,y)

  

# naming the x axis

plt.xlabel('number of digits')

# naming the y axis

plt.ylabel('Execution time')

  

# giving a title to my graph

plt.title('Time complexity')

  

# function to show the plot

plt.show()

 

y=[1119992,1119996,1239996,1479996,1940244,2796744,4479868, 7839996]

x=[4,8,16,32,64,128,256,512]

# plotting the points 

plt.plot(x,y)

  

# naming the x axis

plt.xlabel('number of digits')

# naming the y axis

plt.ylabel('Memory used in Bytes')

  

# giving a title to my graph

plt.title('Space complexity')

  

# function to show the plot

plt.show()
