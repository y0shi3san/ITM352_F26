#
#
#

with (open("names.txt", "r") as file_object):
   while (line := file_object.readline()):
       print(line.strip())