from ctypes import HRESULT

from flask import Flask, jsonify, request

app = Flask(__name__)

# route 1
@app.route("/")
def welcome():
    return "<h1>Welcome to My Flask API!</h1>"

# route 2
@app.route("/about")
def about():
    return jsonify({"name": "Sarah",
         "course": "MCON-504 - Backend Development",
         "semester": "Spring 2025"})

# route 3
@app.route("/greet/<name>")
def greet(name):
    return f"<p>Hello, {name}! Welcome to Flask.</p>"

# route 4
@app.get("/calculate")
def calculate():
    num1 = request.args.get("num1", type=int)
    num2 = request.args.get("num2", type=int)
    operation = request.args.get("operation")

    if num1 is None or num2 is None or operation is None:
        return jsonify({"error": "No parameters provided."}), 400

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return jsonify({"error": "Cannot divide by 0"}), 400
        result = num1 / num2
    else:
        return jsonify({"error": "Invalid operation."}), 400
    return jsonify({
        "result": result,
        "operation": operation
    })

# route 5
@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON provided."}), 400

    data["echoed"] = True
    return jsonify(data)

#route 6
@app.route("/status/<int:code>")
def status(code):
    return f"code: {code} ", code

if __name__ == "__main__":
    app.run(debug=True, port=5000)
