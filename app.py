from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'your-openai-api-key'

def categorize_email(subject, body):
    prompt = f"Categorize the following email:\n\nSubject: {subject}\n\nBody: {body}\n\nCategories: Work, Personal, Promotions, Uncategorized"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10
    )
    category = response.choices[0].text.strip()
    return category

@app.route('/process_email', methods=['POST'])
def process_email():
    data = request.json
    subject = data.get('subject', '')
    body = data.get('body', '')
    category = categorize_email(subject, body)
    return jsonify({'category': category})

if __name__ == '__main__':
    app.run(port=5000)
