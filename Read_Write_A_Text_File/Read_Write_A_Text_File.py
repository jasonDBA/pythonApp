# Read / Write files in Python
# Project: Read / Write 'Let it be' lylics
# Name: Jason(Jabin) Choi
# Date: June 8, 2020

# Reference: https://docs.python.org/3/tutorial/inputoutput.html


import os   # import os module

script_dir = os.getcwd()
odd_path = "oddlines.txt"
even_path = "evenlines.txt"
output_path = "output.txt"

abs_odd_path = os.path.join(script_dir, odd_path)
abs_even_path = os.path.join(script_dir, even_path)
abs_output_path = os.path.join(script_dir, output_path)

fodd = open(abs_odd_path, 'r', encoding='utf-8')    # open a oddlines text file (r: read mode)
feven = open(abs_even_path, 'r', encoding='utf-8')  # open a evenlines text file (r: read mode)

if os.path.isfile(abs_output_path):  # if output text file is written something,
    os.remove(abs_output_path)       # remove the content
    foutcome = open(abs_output_path, 'w', encoding='utf-8')  # open an output text file (w: write mode)
else:
    foutcome = open(abs_output_path, 'w', encoding='utf-8')

while True: # Loop through the odd and even line til input lines do not exist any more
    oddSentence = fodd.readline()
    foutcome.writelines(oddSentence)

    evenSentence = feven.readline()
    foutcome.writelines(evenSentence)

    if not oddSentence:
        break

foutcome.writelines('\n\n===================================================')
foutcome.writelines('\nName: Jason(Jabin) Choi, Date: June 8, 2020')
foutcome.writelines('\n===================================================')

foutcome.close()    # close the output file
feven.close()
foutcome.close()
