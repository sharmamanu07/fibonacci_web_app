from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

def fibonacci(n):
    a, b = 0, 1
    sequence = []
    while a <= n:
        sequence.append(str(a))
        a, b = b, a + b
    return ' '.join(sequence)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        if "submit" in request.form:
            try:
                limit = int(request.form["number"])
                result = fibonacci(limit)
            except ValueError:
                result = "Please enter a valid integer."
        elif "reset" in request.form:
            return redirect(url_for("index"))
        elif "quit" in request.form:
            return "Application exited. You may close the browser."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
