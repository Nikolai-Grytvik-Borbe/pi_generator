import flask
import flask_cors
import decimal
import threading
import time

decimal.getcontext().prec = 100000000

def calculate_PI():
    global current_PI, iterations
    pi = decimal.Decimal(0)
    i = 0
    while True:
        pi += decimal.Decimal((-1) ** i / (2 * i + 1))
        current_PI = 4*pi
        iterations = i
        i += 1
        time.sleep(0.1)



app = flask.Flask(__name__)
flask_cors.CORS(app)

# Endpoint to get the current approximation of pi
@app.route("/api/pi", methods=["GET"])
def get_pi():
    return flask.jsonify(pi=current_PI, iterations=iterations)

# Start the background thread when the Flask app starts
if __name__ == "__main__":
    thread = threading.Thread(target=calculate_PI)
    thread.daemon = True  # Allows the thread to close when the main process ends
    thread.start()
    app.run(host="0.0.0.0", port=5001)