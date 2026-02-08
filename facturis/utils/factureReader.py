import pytesseract
from PIL import Image

def fileDataReader(filePath, path=None):
    # 1️⃣ Set tesseract path
    if path:
        pytesseract.pytesseract.tesseract_cmd = path
        QMessagebox.information(
            self,
            "Tesseract Patch Set",
            f"Tesseract binary path set to: {path}"
        )
    else:
        pytesseract.pytesseract.tesseract_cmd = r"ocr\tesseract.exe"

    # 2️⃣ Open the image
    img = Image.open(filePath)

    # 3️⃣ OCR with data output (DICT)
    data = pytesseract.image_to_data(
        img,
        lang="fra+eng",              # invoices often in French + English
        config="--psm 6",            # assume a uniform block of text
        output_type=pytesseract.Output.DICT
    )

    # 4️⃣ Build a list of (word, x, y) tuples
    words = [
        (data["text"][i], data["left"][i], data["top"][i])
        for i in range(len(data["text"]))
        if data["text"][i].strip()   # remove empty words
    ]

    # 5️⃣ Sort words top-to-bottom, left-to-right
    words.sort(key=lambda x: (x[2], x[1]))  # sort by Y, then X

    # 6️⃣ Reconstruct lines based on vertical proximity
    lines = []
    current_line = []
    last_y = None
    LINE_THRESHOLD = 10  # pixels, adjust for your invoices

    for word, x, y in words:
        if last_y is None or abs(y - last_y) <= LINE_THRESHOLD:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
        last_y = y

    if current_line:
        lines.append(" ".join(current_line))

    # 7️⃣ Join all lines into final text
    final_text = "\n \n".join(lines)

    print(final_text)
    return final_text

if __name__ == "__main__":
    fileDataReader(r"C:/Users/kakaFM/3D Objects/Facturis/test_data/facture_2.png")