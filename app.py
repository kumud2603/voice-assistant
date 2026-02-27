from flask import Flask, render_template, request, jsonify
import webbrowser
import wikipedia
import datetime
import subprocess

app = Flask(__name__)

# ---------------- COMMAND PROCESSING ---------------- #

def process_command(command):
    command = command.lower()
    response = ""

    if "hello" in command:
        response = "Hello! How can I help you?"

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {now}"

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        response = "Opening Google"

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube"

    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        if query:
            try:
                result = wikipedia.summary(query, sentences=2)
                response = result
            except:
                response = "Could not find information."
        else:
            response = "Please tell what to search on Wikipedia."

    elif "open command prompt" in command:
        try:
            subprocess.Popen("cmd.exe")
            response = "Opening Command Prompt"
        except:
            response = "Unable to open Command Prompt"

    else:
        response = "Sorry, I can't do that yet."

    return response


# ---------------- ROUTES ---------------- #

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    command = data.get("command")

    response = process_command(command)

    return jsonify({"response": response})


# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    app.run(debug=True)