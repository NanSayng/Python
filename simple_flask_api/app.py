from flask import Flask, jsonify  # Import Flask and jsonify tools

app = Flask(__name__)  # Create a new Flask app (our API server)

@app.route('/hello')  # When someone visits the "/hello" URL, run the function below
def hello():
    # Send back a message in JSON format
    return jsonify({"message": "Hello, this is a simple API!"})

if __name__ == '__main__':
    # Start the app so it listens for requests
    app.run(debug=True)
