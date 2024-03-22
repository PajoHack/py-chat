from flask import Flask, request, render_template_string
import string

app = Flask(__name__)

class ProcedureChatbot:
    def __init__(self):
        self.knowledge_base = {
            self.normalize_question("What are your operating hours?"): "Our operating hours are 9am to 5pm, Monday to Friday.",
        }

    def normalize_question(self, question):
        return question.lower().translate(str.maketrans('', '', string.punctuation))

    def get_response(self, user_question):
        normalized_question = self.normalize_question(user_question)
        for question in self.knowledge_base:
            if normalized_question in question:
                return self.knowledge_base[question]
        return "Sorry, I don't understand the question. Can you try rephrasing?"

chatbot = ProcedureChatbot()

# HTML template for the chat interface
HTML_TEMPLATE = """
<!doctype html>
<html>
<head><title>Procedure Chatbot</title></head>
<body>
  <h2>Procedure Chatbot</h2>
  <form action="/" method="post">
    Your question: <input type="text" name="user_question">
    <input type="submit" value="Ask">
  </form>
  <p>{{response}}</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        user_question = request.form["user_question"]
        response = chatbot.get_response(user_question)
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(debug=True)
