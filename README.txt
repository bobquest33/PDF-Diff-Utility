PDF Diff Utility:
It is a simple utility which helps to do a text level and PDF level comparison between two PDFs.



Requirement:
Python 2.7.9
Note - In case you do not have Python installed this distribution comes bundled with a version of python for Windows 7



Installation:
- With Python Installed

Deploy Requirements using command
 pip install -r requirements.txt

- Without Python Installed
   	
Type at command prompt
 venv\activate


Execution:
python comparePdf.py <left>.pdf <right>.pdf

Sample Output:

You will get two files.
- For text difference
  e.g. diffile-20151207-122734.txt
- For pdf files
  e.g. diffpdf-20151207-122734.pdf


Notes & Issues:
- The difference between two PDFs is currently determinded based on length of text, there is a md5 comparison but it does not work
- The PDF difference output file takes time to extract and is known to generate huge files.

In Future:
- Improve Diff comparison functionality
- Image comparison in PDFs
- Batch comparison
 


