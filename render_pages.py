import fitz
import os

pdf_path = "projects/Catleya Cafeteria/02-Entregables/present-cattleya-cafeteria-mafer.pdf"
out_dir = "projects/Catleya Cafeteria/extracted-images"

os.makedirs(out_dir, exist_ok=True)
doc = fitz.open(pdf_path)

for i in range(len(doc)):
    page = doc.load_page(i)
    mat = fitz.Matrix(2.0, 2.0)
    pix = page.get_pixmap(matrix=mat)
    pix.save(f"{out_dir}/slide_{i+1:02d}.jpg")

print(f"Rendered {len(doc)} pages.")
