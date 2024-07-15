# src/extractor.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# Define the extraction function
def extract_info(text, query, instructions=None):
    prompt = f"""
    You are an expert bill analyzer. Analyze the following bill text:

    Bill: {text}


    User Query: {query}

    Based on the user's query, extract and provide the relevant information from the bill. 
    If the requested information is not present in the bill, clearly state that it's not available.
    Present the extracted information in a clear, structured format.
    If there are any unusual or potentially important details related to the query, please mention them.
    

    """

    response = model.generate_content(prompt)
    return response.text

