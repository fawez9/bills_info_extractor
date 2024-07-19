
from src.extractor import chatbot

if __name__ == "__main__":
    # just for testing
    file_path = input("Enter file path: ")
    user_query = input("what do you want to extract: ")
    print(chatbot(file_path, user_query))
