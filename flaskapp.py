from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'Contact': "7539517539",
        'Name': 'Raju',
        'done': 'false',
        'id': '1'
    },
    {
        'Contact': "8528528528",
        'Name': 'Rahul',
        'done': 'false',
        'id': '2'
    }
]

@app.route("/add-data", methods=["POST"])

def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }

    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)


