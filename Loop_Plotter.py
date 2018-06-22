#Importing...

import numpy as np
import matplotlib.pyplot as plt

#These make the graphs prettier
import seaborn as sns
sns.set()

#This is pulling the selected file using numpy and the input from the user
#Raw input is used to evaluate the input as a literal string

What_Loops = raw_input("What is the name of the file? ")
loops = np.loadtxt(What_Loops)

#This requires user input to determine when to reiterate through the selected file
#NOTE:
#THE FILE SHOULD BE STRUCTURED WITH NO WORDS OR SPACES BETWEEN COLUMNS SIMPLY;
#NUMBER NUMBER NUMBER NUMBER NUMBER 
#NUMBER NUMBER NUMBER NUMBER NUMBER
#Repeating all the way through

num_loops = int(input("How many loops were used? "))

#Creating a list from the values to later manipulate

loop_vals = []
for i in range(num_loops):
    loop_vals.append(loops[i::num_loops,4])
    
#Gathering useful naming information and asking the user what loop they want to plot   

Model = What_Loops[12:14]
what_loop = raw_input("What loop do you want to plot?(int/all) ")

#Gathering the maximum value in all of the arrays to create a common axis later

LOOP_ARRAY = np.array(loop_vals)
max_value = LOOP_ARRAY.max()

#Using the conditional statement of wether or not the user wants to plot all
#of the loops or just one of the loops

#Plotting all is recommended for the best level of consistency in figure size but is not required

if what_loop == "all":
    for i in range(num_loops):
        loop_name = i #tells numpy what to use (0-X)
        temp_name = i+1  #tells us what we're seeing based on a "normal" naming system (1-X)
        plt.plot(np.arange(1,len(loop_vals[i])+1),loop_vals[i])
        plt.title("Model "+Model+" Loop " + str(temp_name))
        plt.xlabel("Iteration Number (x10000)")
        plt.xticks(np.arange(1,len(loop_vals[i])+1),np.arange(1,len(loop_vals[i])+1)*10000)
        plt.ylabel("R-Value")
        plt.ylim(0,max_value*1.1)
        plt.hlines(0.002,1,len(loop_vals[loop_name])) #Shows the threshold of statistically significant values
        plt.grid(True)
        #plt.show()
        plt.savefig("Model_"+Model+"_Loop_"+str(temp_name)+"_Rvalues_plot.png")
        plt.close(True)
        
    
    
else:

    loop_name = int(what_loop)

    plt.plot(np.arange(1,len(loop_vals[loop_name - 1])+1)*10000,loop_vals[loop_name - 1])
    plt.title("Model "+Model+" Loop " + str(loop_name))
    plt.xlabel("Iteration Number (x10000)")
    plt.ylabel("R-Value")
    plt.hlines(0.002,1,len(loop_vals[loop_name]))
    plt.ylim(0,max_value*1.1)
    plt.grid(True)
    plt.savefig("Model_"+Model+"_Loop_"+str(loop_name)+"_Rvalues_plot.png")
    plt.show()

