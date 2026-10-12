with open('demolog.log') as f:
    for line in f:

        if "ERROR" in line:
            
            with open('error.log', 'a') as ft:
                ft.write(line)
        elif "INFO" in line:
            with open('info.log', 'a') as ft:
                ft.write(line)
                        







'''filename=demolog.log
import sys
from collections import Counter

filename=sys.argv[1] 

with open(filename) as f:
    lines=f.readlines()
    
print("Total lines:", len(lines))'''



    

