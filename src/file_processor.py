import pypdfium2 as pdfium
from io import BytesIO
from pytesseract import image_to_string
from PIL import Image

def extract_text_pdf(file_path, scale=300/72):
    pdf_file = pdfium.PdfDocument(file_path)
    page_indices = [i for i in range(len(pdf_file))]

    renderer = pdf_file.render(
        pdfium.PdfBitmap.to_pil,
        page_indices=page_indices,
        scale=scale,
    )

    list_final_images = []

    for i, image in zip(page_indices, renderer):
        image_byte_array = BytesIO()
        image.save(image_byte_array, format='jpeg', optimize=True)
        image_byte_array = image_byte_array.getvalue()
        list_final_images.append({i: image_byte_array})

    return extract_text_with_pytesseract(list_final_images)

def extract_text_with_pytesseract(list_dict_final_images):
    image_list = [list(data.values())[0] for data in list_dict_final_images]
    image_content = []

    for image_bytes in image_list:
        image = Image.open(BytesIO(image_bytes))
        raw_text = image_to_string(image)
        image_content.append(raw_text)

    return "\n".join(image_content)

def extract_text_images(list_files):
    image_content = []

    for file_path_or_bytes in list_files:
        if isinstance(file_path_or_bytes, str):
            image = Image.open(file_path_or_bytes)
        else:
            image = Image.open(BytesIO(file_path_or_bytes))
        raw_text = image_to_string(image)
        image_content.append(raw_text)

    return "\n".join(image_content)


