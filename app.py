from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('scanner.html')

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    code = data.get('code')
    
    print("Scanned Code:", code)   # prints in terminal
    
    return {"status": "success", "code": code}

if __name__ == '__main__':
    app.run(debug=True, )
