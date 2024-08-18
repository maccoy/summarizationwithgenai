import pymupdf
import os
import base64
from PIL import Image
import io

def create_allPageExtractedText(folder_path):
    # Specify the folder path
    # Initialize a list to store the content of all .txt files
    combined_content = []

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt') and filename == 'extractedText.txt':  # Skip the combined.txt file if it exists
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                combined_content.append(file.read())

    # Combine all contents into a single string
    combined_text = '\n'.join(combined_content)

    # Save the combined content into a new file named 'combined.txt'
    combined_file_path = os.path.join(folder_path, 'allPagExtractedText.txt')
    with open(combined_file_path, 'w', encoding='utf-8') as combined_file:
        combined_file.write(combined_text)

    # print(f"Combined content saved to: {combined_file_path}")


def chekFolderOrCreate(folder_path):
    if not os.path.exists(folder_path):
        # Create the folder if it doesn't exist
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")
def process_file(pdf_document):
        # Iterate through each page
        for page_num in range(len(pdf_document)):
            # Load the page
            page = pdf_document.load_page(page_num)
            # print("NEW PAGE ---------------------------------------------------------")
            # Extract text
            text = page.get_text()
            # Create one folder for each page which will store the extracted Text and Image
            page_folder="Page"+"_"+str(page_num)
            chekFolderOrCreate(page_folder)
            # text_file_path = os.path.join(page_folder, f'page_{page_num + 1}.txt')
            text_file_path = os.path.join(page_folder, f'extractedText.txt')
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)
                # print("TEXT------------")

            # Extract images
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image_extension = base_image["ext"]
                # print("---------------------Base Image---------------",base_image["width"])
                # print("---------------------Base Image---------------",base_image["height"])
                image_path = os.path.join(page_folder, f'page_{page_num + 1}_image_{img_index + 1}.{image_extension}')
                # base64_image_path = os.path.join(json_path, f'page_{page_num + 1}_image_{img_index + 1}.{image_extension}')
                # print("Image------------",f'page_{page_num + 1}_image_{img_index + 1}.{image_extension}')

                # compressImage(image_bytes, image_path)
                # Save the image
                with open(image_path, 'wb') as img_file:
                    img_file.write(image_bytes)
                    img_file.close()
                    # convert to base64
                with open(image_path, 'rb') as img_file:
                    b64_code=base64.b64encode(img_file.read()).decode('utf-8')
                    text_file_path = os.path.join(page_folder, f'page_{page_num + 1}_image_{img_index + 1}.txt')
                    with open(text_file_path, 'w', encoding='utf-8') as text_file:
                        text_file.write(b64_code)


            print(f"Processed page {page_num + 1}")

        print("Extraction complete. Text and images have been saved.")


def find_files(root_dir, filename):
    matches = []
    combined_content=[]
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if filename in filenames:
            matches.append(os.path.join(dirpath, filename))
            # combined_content = '\n'.join(combined_content)
            prompt_file_path = os.path.join(dirpath, filename)
            # print("---------------------PROMTT FILE PATH---------------")
            # print(prompt_file_path)
            # print("---------------------PROMTT FILE PATH---------------")
            with open(prompt_file_path, 'r', encoding='utf-8') as prompt_file:
                combined_content.append(prompt_file.read())

            # Save the combined content into a new file named 'promptFull.txt'
    # print(combined_content)
    print("*****************************************************")

    result = ', '.join(combined_content)

    # print(result)

    return result
    # combined_file_path = os.path.join(root_dir, 'promptFull.txt')
    # with open(combined_file_path, 'w', encoding='utf-8') as combined_file:
    #      combined_file.write(combined_content)

def writeCombinedText(content):
    file_path = 'finalCombinedText.txt'
    with open(file_path, 'w',encoding='utf-8') as file:
        # Write the string to the file
        file.write(content)

if __name__ == '__main__':

    pdf_path = 'Summarization with GenAI_TextSummarization.pdf'
    # page_folder = 'page'
    pdf_document = pymupdf.open(pdf_path)
    print(len(pdf_document))
    process_file(pdf_document)
    # create_allPageExtractedText(page_folder)

    combinedContent = find_files(".", "extractedText.txt")

    print(combinedContent)

    writeCombinedText(combinedContent)

    # uploadImageToAzure()

