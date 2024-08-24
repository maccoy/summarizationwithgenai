import fitz  # PyMuPDF

# Path to the PDF file
pdf_path = 'Market Review - July 2024.pdf'

# Open the PDF document
pdf_document = fitz.open(pdf_path)

# Convert PDF pages to images
image_paths = []
zoom_factor = 2.0
matrix = fitz.Matrix(zoom_factor, zoom_factor)
for page_num in range(len(pdf_document)):
    # Load the page
    page = pdf_document.load_page(page_num)

    # Render page to an image (Pixmap)
    image = page.get_pixmap(dpi=300)

    # Define the output image path
    image_path = f'page_{page_num + 1}.png'

    # Save the image as PNG
    image.save(image_path)

    # Store the path to the saved image
    image_paths.append(image_path)

# Print the paths to the saved images
for path in image_paths:
    print(f"Saved {path}")
