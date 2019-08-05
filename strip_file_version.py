#suppose file 'my-server-build.conf' in your project is versioned as 'my-server-build-1.0.conf', 'my-server-build-2.0.conf' ....so on 'my-server-build-x.0.conf' 
#but you need the original name to everytime you want use this file in ops work.
#So, how to get back th eoriginal file name back. One solution is split the file name with dynamic regular exp.

#!/usr/bin/python
import sys

file=sys.argv[1]
newfilename = re.split(r'(-\d*\.?\d+)', 'file')

print(newfilename)

