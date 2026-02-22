import pypdf
import sys

def extract_text_to_file(pdf_path, output_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        print(f"DEBUG: Found {len(reader.pages)} pages")
        with open(output_path, "w", encoding="utf-8") as f:
            for page_num in range(len(reader.pages)):
                page_text = reader.pages[page_num].extract_text()
                if page_text:
                    f.write(f"--- Page {page_num} ---\n")
                    f.write(page_text + "\n")
        print(f"Success! Text saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_pdf.py <pdf_path> <output_path>")
        sys.exit(1)
    
    extract_text_to_file(sys.argv[1], sys.argv[2])
