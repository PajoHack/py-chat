class ProcedureChatbot:
    def __init__(self):
        # Initialize the chatbot's knowledge base.
        self.knowledge_base = {
            "What are your operating hours?": "Our operating hours are 9am to 5pm, Monday to Friday.",
            # Add more questions and answers specific to your procedures here.
        }
    
    def get_response(self, user_question):
        # Try to find an answer in the knowledge base.
        return self.knowledge_base.get(user_question, "Sorry, I don't understand the question. Can you try rephrasing?")

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
