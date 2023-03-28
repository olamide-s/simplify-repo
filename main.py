import openai
import pytesseract 
from PIL import Image, ImageEnhance
import hide





# put your openai api key on a .py file 
# set the API key
openai.api_key = hide.api



# function to call the ai to summarize the text
def simplify_text(text):
    model_engine = "text-davinci-002"
    prompt = (f"explain  more about this text like a teacher and give refrence to make me understand : {text}"
             )

    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
    message = completions.choices[0].text
    return message.strip()

# change the image and make sure the image are clear  
# load image
img = Image.open('img.png')

# to load  pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# adding some sharpness and contrast to the image 
enhancer1 = ImageEnhance.Sharpness(img)
enhancer2 = ImageEnhance.Contrast(img)
img_edit = enhancer1.enhance(20.0)
img_edit = enhancer2.enhance(1.5)

# run tesseract OCR on the image
text = pytesseract.image_to_string(img)


simplified_text = simplify_text(text)
print(simplified_text)