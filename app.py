from flask import Flask, render_template, request, send_from_directory
import os
import save_transaction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/credit')
def credit():
    return render_template('credit.html')

@app.route('/extra')
def extra():
    return render_template('extra.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/transaction')
def transaction():
    return render_template('transaction.html')

@app.route('/save_transaction', methods=['POST'])
def save_transaction_route():
    return save_transaction.save(request)

@app.route('/save_data', methods=['POST'])
def save_data_route():
    return save_transaction.save(request)

@app.route('/data/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))  
    data_dir = os.path.join(root_dir, 'data') 
    return send_from_directory(data_dir, filename)


if __name__ == '__main__':
    app.run(debug=True)
