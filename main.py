import requests
import os
import sys
import fitz  
import docx  
from urllib.parse import unquote

def extract_text_from_pdf(pdf_path):
    text = ''
    with fitz.open(pdf_path) as doc:
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text += page.get_text()
    return text

def extract_text_from_text_file(txt_path):
    with open(txt_path, 'r') as file:
        text = file.read()
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

def extract_text_from_document(file_path):
    _, extension = os.path.splitext(file_path)
    if extension.lower() == '.pdf':
        return extract_text_from_pdf(file_path)
    elif extension.lower() == '.txt':
        return extract_text_from_text_file(file_path)
    elif extension.lower() == '.docx':
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type.")

def send_prompt_to_local_api(prompt):
    api_url = "http://localhost:11434/api/generate"
    payload = {
        "model": "docsGPT",
        "prompt": f"[INST] {prompt} [/INST]",
        "raw": True,
        "stream": False
    }

    response = requests.post(api_url, json=payload)
    return response.json().get('response', 'No response')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_and_chat.py <file_path>")
        sys.exit(1)

    file_path = unquote(sys.argv[1])
    conversation_history = []

    try:
        extracted_text = extract_text_from_document(file_path)

        print("Text extracted successfully:")
        print(extracted_text)

        
        response = send_prompt_to_local_api(extracted_text)
        conversation_history.append(("System", extracted_text))
        conversation_history.append(("Model", response))

        print("Response from the language model API:")
        print(response)

        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                break

            
            conversation_history.append(("User", user_input))

            conversation_prompt = ' '.join([f"[{role}] {text}" for role, text in conversation_history])
            response = send_prompt_to_local_api(conversation_prompt)
            
            conversation_history.append(("Model", response))

            print("Response from the language model API:")
            print(response)

    except Exception as e:
        print(f"Error: {e}")
