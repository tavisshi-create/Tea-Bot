from flask import Flask, render_template, request

app = Flask(__name__)

# This route opens your HTML page
@app.route("/")
def index():
    return render_template("index.html")

# This route handles the "TeaBot" logic
@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg').lower()
    
    # Simple logic for TeaBot responses
    if "hello" in user_text or "hi" in user_text:
        return "Hello! Would you like a virtual cup of Earl Grey or Matcha today? 🍵"
    elif "tea" in user_text:
        return "I love tea! It's the best way to steep away the stress. 🌿"
    elif "how are you" in user_text:
        return "I'm feeling quite cozy! Just sitting here keeping the water warm. How about you?"
    else:
        return "That sounds interesting! Tell me more while I prepare another pot of tea. ☕"

if __name__ == "__main__":
    app.run(debug=True)