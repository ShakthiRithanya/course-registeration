import pypdf
import os

pdfs = [
    "AIDS_Curriculum.pdf",
    "AIML_Curriculum.pdf",
    "CSBS_Curriculum.pdf",
    "CSE_curriculum.pdf",
    "CYS_Curriculum.pdf",
    "ECE_Curriculum.pdf",
    "IT_Curriculum.pdf",
    "MECH_Curriculum.pdf"
]

base_dir = r"d:\course"
output_dir = r"d:\course\course-registeration\backend"

for pdf in pdfs:
    pdf_path = os.path.join(base_dir, pdf)
    output_path = os.path.join(output_dir, pdf.replace("_Curriculum.pdf", "_text.txt").replace("_curriculum.pdf", "_text.txt").lower())
    
    print(f"Extracting {pdf} to {output_path}...")
    try:
        reader = pypdf.PdfReader(pdf_path)
        with open(output_path, "w", encoding="utf-8") as f:
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    f.write(text + "\n")
        print(f"Successfully extracted {pdf}")
    except Exception as e:
        print(f"Error extracting {pdf}: {e}")
