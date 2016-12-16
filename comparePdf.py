from ReadPdfFromUrl import PdfFromUrl
from pdftotext import PdfToText
import sys
import difflib
import os
import md5
import pdfx
import time

(lfile,rfile) = sys.argv[1:]

timestr = time.strftime("%Y%m%d-%H%M%S")
lpdf = pdfx.PDFx(lfile)
lmetadata = lpdf.get_metadata()
print lmetadata

rpdf = pdfx.PDFx(rfile)
rmetadata = rpdf.get_metadata()
print rmetadata

p2t=PdfToText()

#textOfFile1=p2t.convert_pdf_to_txt(lfile).decode('utf-8').encode('ascii','ignore')
#textOfFile2=p2t.convert_pdf_to_txt(rfile).decode('utf-8').encode('ascii','ignore')
textOfFile1=p2t.convert_pdf_to_txt(lfile)
textOfFile2=p2t.convert_pdf_to_txt(rfile)
print textOfFile1
print textOfFile2
##open first pdf file and save it as file1.pdf
#pdffromUrl.open_pdf_from_url("http://www.seleniummaster.com/sitecontent/images/Selenium_Master_Test_Case_Base_Template.pdf","file1.pdf")
##open second pdf file and save it as file2.pdf
#pdffromUrl.open_pdf_from_url("http://www.seleniummaster.com/sitecontent/images/Selenium_Master_TestCase_Modified_Template.pdf","file2.pdf")
##get texts of file1.pdf
##get length of file1.pdf texts
#textOfFile1 = textOfFile1.decode('UTF-8','ignore')
#textOfFile1 = textOfFile1.encode('ascii','ignore')

#textOfFile2 = textOfFile2.decode('UTF-8','ignore')
#textOfFile2 = textOfFile2.encode('ascii','ignore')


lengthOfTextFile1=len(textOfFile1)
##get length of file2.pdf texts
lengthOfTextFile2=len(textOfFile2)
##print text length information
print "Length of text of File1",lengthOfTextFile1
print "Length of text of File2",lengthOfTextFile2
digest1 = md5.new(textOfFile1)
digest2 = md5.new(textOfFile2)
##compare text length
if(lengthOfTextFile1==lengthOfTextFile2):
#if(digest1==digest2):

    print "Two pdf files' texts are the same"
else:
    print "Two pdf files' texts are different"
    #d = difflib.HtmlDiff()
    #with open("diff.html","w") as f:
    #    f.write(d.make_table(textOfFile1, textOfFile2))
    #with open("diffile1.txt","w") as f:
    #    f.write(textOfFile1)
    #with open("diffile2.txt","w") as f:
    #    f.write(textOfFile2)
	#os.chdir("diff2HtmlCompare")
    #os.system("python diff2HtmlCompare\diff2HtmlCompare.py diffile1.txt diffile2.txt")
    d = difflib.Differ()
    result = d.compare(textOfFile1.split('\n'), textOfFile2.split('\n'))
    #print result
    with open("diffile-"+timestr+".txt","w") as f:
        f.write("\n".join(result))
	os.system("diff-pdf\diff-pdf.exe --output-diff diffpdf-"+timestr+".pdf "+lfile+" "+rfile)

