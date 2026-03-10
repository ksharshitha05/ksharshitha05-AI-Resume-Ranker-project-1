import PyPDF2
import re

def extract_text_from_pdf(file):

    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def extract_email(text):

    email = re.findall(r'\S+@\S+', text)

    if email:
        return email[0]
    return "Not Found"


def extract_phone(text):

    phone = re.findall(r'\+?\d[\d -]{8,12}\d', text)

    if phone:
        return phone[0]

    return "Not Found"