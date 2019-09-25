from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import cv2
import os

class pdf_processor:

    #converts a given pdf to a series of jpgs
    def pdf_to_jpg(self,pdf_filename):
        pages = convert_from_path(pdf_filename,500)
        pagecounter = 0
        pagelist = []
        
        #loop over each page and save them as separate jpegs
        for page in pages:
            fname = "page" + str(pagecounter) + ".jpg"
            pagecounter += 1
            pagelist.append(fname)
            page.save(fname,"JPEG")


        return pagelist

    #extracts text from a given jpeg
    def extract_text(self,file):
        image = cv2.imread(file)
        grayscale_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        grayscale_image = cv2.threshold(grayscale_image,0,255,cv2.THRESH_OTSU)[1]
        filename = "{}.JPG".format(os.getpid())
        cv2.imwrite(filename,grayscale_image)
        print("starting tesseract")
        text = pytesseract.image_to_string(Image.open(filename))
        print("stopping tesseract")
        os.remove(filename)
        return text

    def extract_text_from_pdf(self,pdf_name):
        textstrings = []
        pages = self.pdf_to_jpg(pdf_name)
        for page in pages:
            textstrings.append(self.extract_text(page))
            print(page)
            os.remove(page)
        return textstrings






