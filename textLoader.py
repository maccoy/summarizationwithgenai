from langchain_community.document_loaders import TextLoader

# Read the Full extracted Text content from a file.
def getFullText():
    loader = TextLoader("finalCombinedText.txt","UTF-8")
    doc = loader.load()
    # print(doc)
    # print(doc[0])

    fullExtractedText=doc[0].page_content
    print(fullExtractedText)
    return fullExtractedText

if __name__ == '__main__':
    getFullText()