# This script is used to monitor the CPU temperature of a Raspberry Pi
# it uses GPIO Zero to get live temperature data from the cpu and writes that data to a csv file that is created
# matplotlib is used to visually represent the data as it comes in
# add this line to the bottom of the crontab to automate the script so that it runs everytime the raspberry pi boots up:
# @reboot python3 /home/pi/temp_monitor.py

# import GPIO Zero module to get acccess to cpu temperature, time module for date and time, and matplotlib to graph the data
from gpiozero import CPUTemperature
from time import strftime, time
import matplotlib.pyplot as plt

cpu = CPUTemperature()

plt.ion() # enable interactive plotting
x = []
y = []

# function to write to csv file
def writeTemp(temp):
    # create a new csv file called temp_log.csv and opens it in append mode with the name log
    with open('home/pi/temp_log.csv', 'a') as log:
        # write the current date and time plus the temperature to the csv file
        log.write('{0},{1}\n'.format(strftime('%Y-%m-%d %H:%M:%S'),str(temp)))

# function to graph the temperature data against time
def graph(temp):
    y.append(temp) # add the current temperature to the end of the y list
    x.append(time()) # add the current time to the end of the x list
    plt.clf() # clear the current figure
    plt.scatter(x,y) # creates a scatter plot of y vs x (identifies the points of the graph)
    plt.plot(x,y) # plots y versus x as lines (identifies the lines of the graph)
    plt.draw()

# main loop
while True:
        temp = cpu.temperature
        writeTemp(temp)
        # graph(temp)
        plt.pause(1)