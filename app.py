from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_uid', methods=['POST'])
def check_uid():
    uid = request.json.get('uid')
    if not uid:
        return jsonify({"error": "No UID provided"}), 400
    
    # Calling the external API
    api_url = f"https://region-info-52.vercel.app/region?uid={uid}"
    try:
        response = requests.get(api_url)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": "Failed to connect to API"}), 500

# Required for Vercel
if __name__ == '__main__':
    app.run(debug=True)
