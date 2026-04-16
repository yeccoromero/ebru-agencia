import PyPDF2, sys
for path in sys.argv[1:]:
    print(f"--- {path} ---")
    try:
        reader = PyPDF2.PdfReader(path)
        print(" ".join(page.extract_text() for page in reader.pages)[:400].replace('\n', ' '))
    except Exception as e:
        print(f"Error: {e}")
