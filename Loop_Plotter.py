import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

What_Loops = raw_input("What is the name of the file? ")
loops = np.loadtxt(What_Loops)

num_loops = int(input("How many loops were used? "))

loop_vals = []
for i in range(num_loops):
    loop_vals.append(loops[i::num_loops,4])
    
Model = What_Loops[12]
what_loop = raw_input("What loop do you want to plot?(int/all) ")


if what_loop == "all":
    for i in range(num_loops):
        loop_name = i
        temp_name = i+1
        plt.plot(np.arange(1,len(loop_vals[i])+1),loop_vals[i])
        plt.title("Model "+Model+" Loop " + str(temp_name))
        plt.xlabel("Iteration Number (x10000)")
        plt.ylabel("R-Value")
        plt.hlines(0.002,1,len(loop_vals[loop_name]))
        plt.grid(True)
        plt.savefig("Model"+Model+"Loop"+str(temp_name)+"_Rvalues_plot.png")
        plt.close(True)
    
    
else:

    loop_name = int(what_loop)

    plt.plot(np.arange(1,len(loop_vals[loop_name - 1])+1),loop_vals[loop_name - 1])
    plt.title("Model "+Model+" Loop " + str(loop_name))
    plt.xlabel("Iteration Number (x10000)")
    plt.ylabel("R-Value")
    plt.hlines(0.002,1,len(loop_vals[loop_name]))
    plt.grid(True)
    plt.savefig("Model"+Model+"Loop"+str(loop_name)+"_Rvalues_plot.png")
    plt.show()
