from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]
number_to_guess = random.randint(1, 100)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play_rps', methods=['POST'])
def play_rps():
    user_choice = request.json['choice']
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    })

@app.route('/play_guess', methods=['POST'])
def play_guess():
    global number_to_guess
    user_guess = int(request.json['guess'])
    if user_guess < number_to_guess:
        result = "Too low!"
    elif user_guess > number_to_guess:
        result = "Too high!"
    else:
        result = "Correct! A new number has been generated."
        number_to_guess = random.randint(1, 100)  # Generate a new number
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
