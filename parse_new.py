import PyPDF2, os, glob
folders = ["projects/Mutta", "projects/PilotsCafe", "projects/Samay", "projects/Swipe"]
for f in folders:
    pdfs = glob.glob(os.path.join(f, "**/*.pdf"), recursive=True)
    if pdfs:
        try:
            reader = PyPDF2.PdfReader(pdfs[0])
            text = " ".join(page.extract_text() for page in reader.pages)[:300].replace('\n', ' ')
            print(f"--- {pdfs[0]} ---")
            print(text)
        except:
            pass
