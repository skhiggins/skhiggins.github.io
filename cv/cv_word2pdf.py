# Test word2pdf
# Sean Higgins
# 14mar2018

# Packages
import sys 
import shutil
import re

# Tell Python to recognize where it's saved in Python path
sys.path.append('C:/Dropbox/PythonTools')
	# Local copy of https://github.com/skhiggins/PythonTools/
	
# Import function
from word2pdf import word2pdf

# Convert to pdf
infile = 'C:\\GitHub\\skhiggins.github.io\\cv\\higgins_cv.docx'
outfile = infile.replace('.docx', '.pdf')
webfile1 = 'C:\\GitHub\\skhiggins.github.io\\higgins.pdf'
webfile2 = 'C:\\GitHub\\skhiggins.github.io\\assets\\pdf\\higgins.pdf'
word2pdf(infile)

# Copy to website location
shutil.copy(outfile, webfile1)
	# for backwards compatibility
	
shutil.copy(outfile, webfile2)

