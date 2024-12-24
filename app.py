from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    analysis = None
    if request.method == 'POST':
        text = request.form.get('text')
        if not text.strip():
            analysis = {
                "input": "No input provided",
                "sentiment": "Neutral",
                "details": "Please provide some text for analysis."
            }
        elif "good" in text.lower():
            analysis = {
                "input": text,
                "sentiment": "Positive",
                "details": "The text contains positive sentiment keywords like 'good'."
            }
        elif "bad" in text.lower():
            analysis = {
                "input": text,
                "sentiment": "Negative",
                "details": "The text contains negative sentiment keywords like 'bad'."
            }
        else:
            analysis = {
                "input": text,
                "sentiment": "Neutral",
                "details": "The text does not contain strong positive or negative sentiment."
            }
    return render_template('index.html', analysis=analysis)

if __name__ == '__main__':
    app.run(debug=True)
