# Raspberry Pi CPU Temperature Monitor

The purpose of this project was to monitor and visually represent the CPU temperature on a Raspberry Pi, and then automate the program
to run on startup. 

### temp_monitor.py
This is the python script that loops infinitely until the user manually stops it. Each loop  it gets the Raspberry Pi's current
CPU temperature, writes that data to a csv file with the time and date, and then plots the temperature data over time using
matplotlib.pyplot

### temp_log.csv
This is the csv file that is created with the date, time, and temperature data

### temp_monitor.desktop
This is the file that goes in /home/pi/.config/autostart/ in order to run temp_monitor.py when the Raspberry Pi reboots

### What I struggled with
The biggest issue I dealt with was trying to automate the script so it ran on startup. There a few different ways to do this, and I 
went through a couple of them before finally settling on one that worked the way I wanted it to. 

### What I learned in the process
This project taught me a ton, I learned how to the Raspberry Pi set up with the OS, I got a lot more experience working with Git, 
I learned how to create and write to a file in python and interactively plot data with matplotlib, as well as how to set scripts to 
run automatically. 

