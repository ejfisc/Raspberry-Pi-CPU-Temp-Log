# This script is used to monitor the CPU temperature of a Raspberry Pi
# it creates a csv file

# import GPIO Zero module to get acccess to cpu temperature and time
import gpiozero, time
# import matplotlib to graph the data
import matplotlib.pyplot as plt

plt.ion() # enable interactive plotting
# create the two lists that will hold the data to be plotted:
x = []
y = []
# x axis will be measured in time and y axis will be measured in temperature

# cpu object
cpu = gpiozero.CPUTemperature()

plt.show() # show the current figure

# create a new csv file called cpu_temp.csv and opens it in append mode with the name log
with open('./cpu_temp_log.csv', 'a') as log:
    while True:
        temp = cpu.temperature # get current temperature

        # live graphing:
        y.append(temp) # add the current temperature to the end of the y list
        x.append(time.time()) # add the current time to the end of the x list
        plt.clf() # clear the current figure
        plt.scatter(x,y) # creates a scatter plot of y vs x (identifies the points of the graph)
        plt.plot(x,y) # plots y versus x as lines (identifies the lines of the graph)

        # write the current date and time plus the temperature to the csv file
        log.write('{0},{1}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'),str(temp)))
        plt.draw() # redraw the graph
        plt.pause(1)
