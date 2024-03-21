import string

class ProcedureChatbot:
    def __init__(self):
        # Initialize the chatbot's knowledge base with questions normalized (lowercase, no punctuation).
        self.knowledge_base = {
            self.normalize_question("What are your operating hours?"): "Our operating hours are 9am to 5pm, Monday to Friday.",
            # Add more questions and answers here, ensuring questions are normalized.
        }

    def normalize_question(self, question):
        # Normalize the question by making it lowercase and removing punctuation.
        return question.lower().translate(str.maketrans('', '', string.punctuation))

    def get_response(self, user_question):
        # Normalize the user's question before trying to find an answer.
        normalized_question = self.normalize_question(user_question)

        # Look for a question in the knowledge base that contains the user's normalized question as a substring.
        for question in self.knowledge_base:
            if normalized_question in question:
                return self.knowledge_base[question]
        
        return "Sorry, I don't understand the question. Can you try rephrasing?"

def main():
    chatbot = ProcedureChatbot()
    print("Welcome to the Procedure Chatbot! Ask me a question or type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
