from flask import Flask, jsonify, request, Response

app = Flask('basic_server')
app.debug = True

buttons = []

@app.route('/new-button', methods=['OPTIONS'])
def new_button_options():
    r = Response(status=200)
    r.headers.extend({
        'Access-Control-Allow-Origin': 'http://localhost:3000',
        'Access-Control-Allow-Method': 'Post',
        'Access-Control-Allow-Headers': 'content-type'
        })
    return r


@app.route('/new-button', methods=['POST'])
def new_button():
    buttons.append(request.json)
    return Response(status=200)

@app.route('/get-buttons')
def get_buttons():
    return jsonify(buttons)

if __name__ == '__main__':
    app.run()
