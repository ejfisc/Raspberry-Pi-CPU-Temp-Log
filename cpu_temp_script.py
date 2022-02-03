# This script is used to monitor the CPU temperature of a Raspberry Pi
# it creates a csv file

# import GPIO Zero module to get acccess to cpu temperature and time
import gpiozero, time

# cpu object
cpu = gpiozero.CPUTemperature()

# create a new csv file called cpu_temp.csv and opens it in append mode with the name log
with open('/home/pi/cpu_temp.csv', 'a') as log:
    while True:
        temp = cpu.temperature
        # write the current date and time plus the temperature to the csv file
        log.write('{0},{1}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'),str(temp)))
        time.sleep(1) # sleep for 1 second