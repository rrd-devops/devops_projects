from flask import Flask, jsonify
import random


app = Flask(__name__)
JOKES = [
"Why did the programmer quit his job? Because he didn't get arrays.",
"I told my computer I needed a break, and it said 'No problem — I'll go to sleep.'",
"There are 10 types of people: those who understand binary and those who don't.",
]


@app.route('/joke')
def joke():
    return jsonify({"joke": random.choice(JOKES)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
