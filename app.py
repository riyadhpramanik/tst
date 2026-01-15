from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/check', methods=['POST'])
def check_uid():
    uid = request.json.get('uid')
    external_api = f"https://region-info-52.vercel.app/region?uid={uid}"
    
    try:
        response = requests.get(external_api)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
