import base64
from openai import AzureOpenAI
from textLoader import getFullText

AZURE_OPENAI_ENDPOINT='*'
AZURE_OPENAI_KEY='*'
# 19cd54641f5f454aa8d1fa70ec99bc3f
AZURE_OPENAI_API_VERSION="2024-02-15-preview"
AZURE_MODEL='*'
def getClient():
    client = AzureOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_KEY,
        api_version=AZURE_OPENAI_API_VERSION
    )
    return client



# Helper function to convert a file to base64 representation
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Takes in a base64 encoded image and prompt (requesting an image summary)
# Returns a response from the LLM (image summary)

def image_summarize(prompt,encoded_image):
    client=getClient()
    ''' Image summary '''
    response = client.chat.completions.create(
        model=AZURE_MODEL,
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    }
                }

            ],
            }
        ],
        max_tokens=1500,
    )
    content = response.choices[0].message.content
    print(content)
    # print("------------------------------------",response)
    tokens_used = response.usage.total_tokens
    print(f"Tokens used: {tokens_used}")
    print("------------------------------------")
    return content


if __name__ == '__main__':


    # context=(" You are an Information Specialist: Specializes in distilling large amounts of"
    #          " information into concise, actionable summaries. This role often involves "
    #          "creating summaries for business intelligence or strategic decision-making."
    #          "You have  to Summarize the given Text and Tables. "
    #          " Cover both Extractvie Summary and Abstractive summary."
    #          " Summarise in not more than 500 words."
    #          " Mention in a PS Note: "
    #          " What is summarised from Text,Table and What is summarised from Images.")

    context = (" From the given image extract the data from the Table and give in json format")
    prompt=context
    encoded_Image=encode_image("finalQualityImage.png")
    image_summarize(prompt,encoded_Image)