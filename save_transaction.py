from flask import Flask, request, jsonify
import os
import json
import traceback

app = Flask(__name__)

@app.route('/save_transaction', methods=['POST'])
def save_transaction_route():
    try:
        if request.is_json:
            transaction_data = request.get_json()
            print('Received transaction:', transaction_data)

            if transaction_data:
                file_path = 'data/transaction-history.json'
                save_to_json(transaction_data, file_path)
                return 'Transaction saved successfully'
            else:
                return jsonify({'error': 'Empty JSON data received'}), 400
        else:
            return jsonify({'error': 'Invalid JSON data received'}), 400
    except Exception as e:
        print('Error saving transaction:', e)
        traceback.print_exc()
        return jsonify({'error': 'Internal Server Error'}), 500

def save_to_json(transaction_data, file_path):
    with open(file_path, 'a') as json_file:
        json.dump(transaction_data, json_file, indent=4)

def save(request):
    try:
        data = request.get_json()
        file_path = 'data/transaction-history.json' 

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        existing_data.append(data)

        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=4)

        return 'Data saved successfully'
    except Exception as e:
        print('Error saving data:', e)
        return 'Error saving data'


if __name__ == '__main__':
    app.run(debug=True)
