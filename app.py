from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Go to /generate?n=10 to get even numbers"

@app.route('/generate')
def generate_even_numbers():
    try:
        n = int(request.args.get('n', 10))
        evens = [i for i in range(2, 2 * n + 1, 2)]
        return jsonify(evens)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()
