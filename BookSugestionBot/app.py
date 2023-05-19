from flask import Flask, render_template, request
import openai


app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'


# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message1 = request.json.get("message")
    # Send the message to OpenAI's API and receive the response

    qu1="suggest a book related  or give price in rupee author name and discription of this book or find  books related to this domain or which has this as content any book about this  "
    qu2="ever new book respose should be on new line or add numbering to every book  "
    qu3="answer just related to book nothing else"
    message=qu1+qu2+qu3+message1
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run()

