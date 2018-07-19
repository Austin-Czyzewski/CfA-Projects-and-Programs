import numpy as np
import matplotlib.pyplot as plt

#Load in the loop data

Loops = np.loadtxt("Stable_Models.txt")
loops = Loops[::,4]  #Only looking at the last (5th) value of reach column
parse_by = 8 #essentially how many loops there are

#This is simply turning the long list into lists of 8 within a list, to easily plot and sort later.

all_loops = []
for i in range(0,len(loops),parse_by):
    temp_list = []
    for j in range(parse_by):
        if i+j < len(loops):
            temp_list.append(loops[i+j])
    all_loops.append(temp_list)
    
#Naming loops to easily identify what loop is returning the best results
    
Loop_Names = ['Model_5_30000','Model_5_60000','Model_7_30000','Model_7_60000','Model_9_30000',
             'Model_9_60000','Model_11_30000','Model_11_60000','Model_18_30000',
             'Model_18_60000','Model_19_30000','Model_19_60000']

#Plotting 

plt.figure(figsize=(12,8))
nums = np.arange(1,9)
colors = ["red","blue","green","yellow","magenta","black"]
pallette = [item for items in zip(colors, colors) for item in items] #since we will have 2 of each graph we need 2 of 
for i in range(len(all_loops)):                                      #each color
    if i%2 == 0:         #plots all of the 30000 loops
        plt.plot(nums,all_loops[i],color = pallette[i],label = Loop_Names[i],alpha = 0.5,linewidth = 2.5)
    else:                #plots all of the 60000 loops
        plt.plot(nums,all_loops[i],color = pallette[i], linestyle = 'dashed',alpha = 0.5,linewidth = 2.5)
plt.ylim(0,0.010)
plt.hlines(0.002,1,8,color = 'black',alpha = 0.25)
plt.annotate('Line of statistical significance',xy = (1,0.0015),fontsize = 10)
plt.legend(shadow=True)
plt.title("R-Value for Stable Models",fontsize = 20)
plt.xlabel("Loop Number",fontsize = 17)
plt.ylabel("R-Value", fontsize = 17)

#summing up all of the values to see which model has the highest overall statistical significance

sums = []
for i in all_loops:
    sums.append(sum(i))
print "The model with the best results is",Loop_Names[sums.index(min(sums))]
plt.show()
