from flask import jsonify

def model_to_json(model):
    if type(model) is list:
        return jsonify([each.to_dict() for each in model])
    else:
        return jsonify(model.to_dict())