import packages.image_processing.pdf_processor as p

n = p.pdf_processor()

text = n.extract_text_from_pdf("image_processing/doc.pdf")


for j in text:
    for k in j:
        print(k)


