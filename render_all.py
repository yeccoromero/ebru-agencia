import fitz
import os

pdf_targets = {
    "projects/Lulas/Lulas-presentación logo.pdf": "projects/Lulas",
    "projects/LaSazonDelSebas/Presentacion-logo-la-sazon del sebas.pdf": "projects/LaSazonDelSebas",
    "projects/WeWine/wewine-presentación logo — 4 de junio 23.46.50.pdf": "projects/WeWine",
    "projects/KapitalMeats/kapital-01-logo-final-out-200708-curvas.pdf": "projects/KapitalMeats",
    "projects/BitBit/Bibit Presentación Final.pdf": "projects/BitBit"
}

for pdf_path, bdir in pdf_targets.items():
    out_dir = f"{bdir}/extracted-images"
    os.makedirs(out_dir, exist_ok=True)
    try:
        doc = fitz.open(pdf_path)
        for i in range(len(doc)):
            page = doc.load_page(i)
            mat = fitz.Matrix(2.0, 2.0)
            pix = page.get_pixmap(matrix=mat)
            pix.save(f"{out_dir}/slide_{i+1:02d}.jpg")
        print(f"Rendered {len(doc)} pages for {bdir}")
    except Exception as e:
        print(f"Error on {pdf_path}: {e}")
