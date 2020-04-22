# Import modules
import sys
# Read the given file

with open(sys.argv[1]) as filename:
    content = filename.readlines()

# Read the date given in argument
date = sys.argv[2]
hunza = sys.argv[3]

## Loop on all lines
for f in content:
    f.split()[0] == "LOCUS"
    splitted_line = f.split()
    
    #print(splitted_line[0]     + splitted_line[1])
    
    #print(splitted_line[0] + ' ' + str(splitted_line[1].split('_')[0]) +' '+ str(splitted_line[1].split('_')[1]) + ' '+ str(splitted_line[1].split('_')[2]) +' '+ str(splitted_line[2]) + ' ' + date)
    
    print(splitted_line[0] + ' '+ str(splitted_line[1].replace('asad', hunza).split('_')[0])+' '+ str(splitted_line[2]) + ' '+ str(splitted_line[3])+ ' ' + date)
    
