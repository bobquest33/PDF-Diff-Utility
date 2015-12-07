from urllib2 import Request, urlopen
from pyPdf import PdfFileWriter, PdfFileReader
from StringIO import StringIO

class PdfFromUrl(object):
        def __init__(self):
            print 'Read Pdf from a URL'

        def open_pdf_from_url(self,url,outputfile):
                
                writer = PdfFileWriter()

                remoteFile = urlopen(Request(url)).read()
                memoryFile = StringIO(remoteFile)
                pdfFile = PdfFileReader(memoryFile)

                for pageNum in xrange(pdfFile.getNumPages()):
                        currentPage = pdfFile.getPage(pageNum)
                        #currentPage.mergePage(watermark.getPage(0))
                        writer.addPage(currentPage)


                outputStream = open(outputfile,"wb")
                writer.write(outputStream)
                outputStream.close()