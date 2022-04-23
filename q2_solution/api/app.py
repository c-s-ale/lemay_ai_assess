from .model import ENtoFRModel
from flask import Flask, jsonify, request

app = Flask(__name__)
en_to_fr_model = ENtoFRModel()

@app.route('/translate/en_to_fr/', methods=['POST'])
def translate():
    try:
        input_text = request.json['text']
    except KeyError:
        return jsonify({"error": "no text provided"})

    # translate english text to french
    print(input_text)
    if input_text:
        translation = en_to_fr_model.translate_en_to_fr(input_text)
        print(translation)
    else:
        return jsonify({"error": "no text provided"})

    # return translation
    return jsonify({"original_text" : input_text, "french" : translation})