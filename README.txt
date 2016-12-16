PDF Diff Utility:
It is a simple utility which helps to do a text level and PDF level comparison between two PDFs.



Requirement:
Python 2.7.9
https://www.python.org/downloads/release/python-279/

For library requirements please refer requirements.txt

Installation:
- With Python Installed

Download the utility using git:
 git clone https://github.com/bobquest33/PDF-Diff-Utility.git


Deploy Requirements using command
 pip install -r requirements.txt


Execution:

Open command prompt and go to the path where this utility has been downloaded any type:

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



