from flask import Flask, make_response, jsonify, request
from bd  import Motos

app = Flask('__name__')
app.config['JSON_SORT_KEYS'] = False

@app.route('/motos', methods=['GET'])
def get_motos():
    return make_response(
        jsonify(
            message='lista de motos',
            data= Motos)
    )

@app.route('/motos', methods=['POST'])
def create_motos():
    moto = request.json
    Motos.append(moto)
    return make_response(jsonify(
        message= 'nova moto inclusa',
        data= moto
    ))



if __name__ == '__main__':
    app.run()