from pdf2image import convert_from_path
import pytesseract
import cv2
import os


class ImageProcessor:

    # convert a bitmap to binary form(a pixel is either black or white)
    def binarize(self,filename):
        # load image as grayscale
        grayscale_image = cv2.imread(filename, 0)

        # perform binarization of image so that a given pixel is either black or white
        blur = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
        ret3, binary_image = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        return binary_image

    # converts a given pdf to a series of jpgs
    def pdf_to_jpg(self, pdf_filename):

        pages = convert_from_path(pdf_filename)
        pagecounter = 0
        pagelist = []

        # loop over each page and save them as separate jpegs
        for page in pages:
            fname = "page" + str(pagecounter) + ".jpg"
            pagecounter += 1
            pagelist.append(fname)
            page.save(fname, "JPEG")

        # return list of filenames for the pages
        return pagelist

    # extracts text from a given jpeg by using OCR
    def extract_text(self, file,text_language):

        binary_image = self.binarize(file)
        print("starting tesseract")
        text = pytesseract.image_to_string(binary_image, lang=text_language)
        print("stopping tesseract")
       
        return text

    # use OCR to extract text from a pdf
    def extract_text_from_pdf_ocr(self, pdf_name,language):
        textstrings = []
        pages = self.pdf_to_jpg(pdf_name)
        for page in pages:
            textstrings.append(self.extract_text(page,language))
            print(page + " read")
            os.remove(page)
        return textstrings








