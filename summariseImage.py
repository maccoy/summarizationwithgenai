import base64
from openai import OpenAI
from textLoader import getFullText
API_KEY='***'
client = OpenAI(api_key=API_KEY)

# Helper function to convert a file to base64 representation
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Takes in a base64 encoded image and prompt (requesting an image summary)
# Returns a response from the LLM (image summary)

def image_summarize(prompt):
    ''' Image summary '''
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                "type": "image_url",
                "image_url": {
                   "url": "https://stackqstorage.blob.core.windows.net/testimages/page_2_image_1.png"
                },


                },

                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://stackqstorage.blob.core.windows.net/testimages/page_1_image_2.png"
                    },

                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://stackqstorage.blob.core.windows.net/testimages/page_3_image_1.png"
                    },

                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://stackqstorage.blob.core.windows.net/testimages/page_4_image_1.png"
                    },

                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://stackqstorage.blob.core.windows.net/testimages/page_5_image_1.png"
                    },

                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://stackqstorage.blob.core.windows.net/testimages/page_5_image_2.png"
                    },

                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://stackqstorage.blob.core.windows.net/testimages/page_6_image_1.png"
                    },

                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://stackqstorage.blob.core.windows.net/testimages/page_6_image_2.png"
                    },

                },


            ],
            }
        ],
        max_tokens=1500,
    )
    content = response.choices[0].message.content
    print(content)
    print("------------------------------------",response)
    tokens_used = response.usage.total_tokens
    print(f"Tokens used: {tokens_used}")
    print("------------------------------------")
    return content


if __name__ == '__main__':

# image_base64 = encode_image("page_1_image_2.png")
    fullText=getFullText()
    context=(" You are an Information Specialist: Specializes in distilling large amounts of"
             " information into concise, actionable summaries. This role often involves "
             "creating summaries for business intelligence or strategic decision-making."
             "You have  to Summarize the given Text and Images. Cover both Extractvie Summary and Abstractive summary."
             " Summarise in not more than 500 words."
             " Mention in a PS Note: "
             " What is summarised from Text and What is summarised from Images.")
    prompt=context+fullText
    image_summarize(prompt)