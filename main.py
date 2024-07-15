
from src.extractor import chatbot


if __name__ == "__main__":
    file_path = input("Enter file path: ")
    user_query = input("what do you want to extract: ")
    chatbot(file_path, user_query)
