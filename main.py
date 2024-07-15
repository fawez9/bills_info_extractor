from src.extractor import extract_info
from src.file_processor import extract_text_pdf, extract_text_images
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def chatbot():
    print("Welcome to the Document Information Extractor!")
    
    file_path = input("Enter the path to your file: ")
    try:
        if file_path.lower().endswith(".pdf"):
            document_text = extract_text_pdf(file_path)
        elif file_path.lower().endswith((".jpg", ".png", ".jpeg")):
            document_text = extract_text_images([file_path])
        else:
            print("Unsupported file format. Please provide a PDF or image file.")
            return
        print(f"File loaded successfully. ({len(document_text)} characters)")
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    while True:
        query = input("\nEnter your query (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
        
        try:
            result = extract_info(document_text, query)
            print("\nExtracted Information:")
            print(result)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    chatbot()
