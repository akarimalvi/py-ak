# Import modules
import sys

# Read the given file
##with open(sys.argv[1]) as file_object:
    ##lines = file_object.readlines()
    ##print(lines)
# list = [el1, el2, e3]

#######file = open("KJ473812.1.gbk","r")
#######file_lines = file.readlines()
#######print(file_lines)


file = open(sys.argv[1])
lines = file.readlines()



# Read the date given in argument
##date = sys.argv[2]

## Loop on all lines

f = lines.split()[0] == "LOCUS"
print(f)
		##splitted_line = line.split()
		##print(splitted_line)
		
		
		
		
		#print(splitted_line[0] + '        ' + str(splitted_line[1].split('_')[0]) + '_' + str(splitted_line[1].split('_')[1]) + "            " + str(splitted_line[1].split('_')[3]) + " bp    DNA     linear       " + date)
	#elif (date in line):
		#continue
    #else:
		#print(line.replace('\n', '')) 
