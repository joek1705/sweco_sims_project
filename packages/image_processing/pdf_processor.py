from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import numpy as np
import cv2
import os

class pdf_processor:

    #converts a given pdf to a series of jpgs
    def pdf_to_jpg(self,pdf_filename):
        pages = convert_from_path(pdf_filename)
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
        image = cv2.imread(file,0)
        gaussblur = cv2.GaussianBlur(image,(3,3),0)
        grayscale_image = cv2.threshold(gaussblur,0, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        filename = "{}.JPG".format(os.getpid())
        cv2.imwrite(filename,grayscale_image)
        print("starting tesseract")
        text = pytesseract.image_to_string(Image.open(filename), lang="swe")
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






