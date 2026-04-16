import fitz # PyMuPDF
import os

pdf_path = "projects/Catleya Cafeteria/02-Entregables/present-cattleya-cafeteria-mafer.pdf"
out_dir = "projects/Catleya Cafeteria/extracted-images"

os.makedirs(out_dir, exist_ok=True)
doc = fitz.open(pdf_path)
img_count = 0

for i in range(len(doc)):
    for img in doc.get_page_images(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n - pix.alpha > 3:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        pix.save(f"{out_dir}/img_{img_count}.png")
        img_count += 1
        pix = None

print(f"Extracted {img_count} images.")
