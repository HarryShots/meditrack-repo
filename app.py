from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
patients = []
next_id = 1


# Health check
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200


# Get all patients
@app.route('/patients', methods=['GET'])
def get_patients():
    return jsonify(patients), 200


# Get single patient
@app.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    for patient in patients:
        if patient["id"] == id:
            return jsonify(patient), 200
    return jsonify({"error": "Patient not found"}), 404


# Add new patient
@app.route('/patients', methods=['POST'])
def add_patient():
    global next_id
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_patient = {
        "id": next_id,
        "name": data["name"],
        "age": data.get("age", ""),
        "condition": data.get("condition", "")
    }

    patients.append(new_patient)
    next_id += 1

    return jsonify(new_patient), 201


# Update patient
@app.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    data = request.get_json()

    for patient in patients:
        if patient["id"] == id:
            patient["name"] = data.get("name", patient["name"])
            patient["age"] = data.get("age", patient["age"])
            patient["condition"] = data.get("condition", patient["condition"])
            return jsonify(patient), 200

    return jsonify({"error": "Patient not found"}), 404


# Delete patient
@app.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    global patients

    for patient in patients:
        if patient["id"] == id:
            patients.remove(patient)
            return jsonify({"message": "Patient deleted"}), 200

    return jsonify({"error": "Patient not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
