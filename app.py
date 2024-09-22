from flask import Flask, request, jsonify
import base64
import mimetypes

app = Flask(__name__)

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        data = request.json.get('data', [])
        file_b64 = request.json.get('file_b64', None)
        
        # Process data
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        highest_lowercase = sorted([x for x in data if x.islower()], reverse=True)[:1]
        
        # File validation
        file_valid = False
        mime_type = ""
        file_size_kb = 0
        if file_b64:
            try:
                file_data = base64.b64decode(file_b64)
                file_size_kb = len(file_data) / 1024
                mime_type = mimetypes.guess_type(file_data)[0]
                file_valid = True
            except Exception as e:
                file_valid = False
        
        # Prepare response
        response = {
            "is_success": True,
            "user_id": "Tanishka_Maheshwari_21032003",
            "email": "tb8980@srmist.edu.in",
            "roll_number": "RA2111027010093",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase,
            "file_valid": file_valid,
            "file_mime_type": mime_type,
            "file_size_kb": file_size_kb
        }
        return jsonify(response)

    elif request.method == 'GET':
        return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
