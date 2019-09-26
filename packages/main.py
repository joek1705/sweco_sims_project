import packages.image_processing.pdf_processor as p

n = p.pdf_processor()

#t = n.extract_text_from_pdf("image_processing/scanned_text_document.pdf")

print(n.extract_text("page1.jpg"))


