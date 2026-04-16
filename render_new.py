import fitz
import os
import glob
folders = ["projects/Mutta", "projects/PilotsCafe", "projects/Samay", "projects/Swipe"]

for f in folders:
    pdfs = glob.glob(os.path.join(f, "**/*.pdf"), recursive=True)
    if not pdfs: continue
    out_dir = f"{f}/extracted-images"
    os.makedirs(out_dir, exist_ok=True)
    try:
        doc = fitz.open(pdfs[0])
        for i in range(len(doc)):
            mat = fitz.Matrix(2.0, 2.0)
            pix = doc.load_page(i).get_pixmap(matrix=mat)
            pix.save(f"{out_dir}/slide_{i+1:02d}.jpg")
            
        imgs = glob.glob(f"{out_dir}/*.jpg")
        largest = max(imgs, key=os.path.getsize)
        print(f"[{f}] Pages: {len(doc)} | Largest/Cover: {largest}")
    except Exception as e:
        print(f"Error on {f}: {e}")
