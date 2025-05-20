from quart import Quart, request, jsonify

app = Quart(__name__)

@app.route('/')
async def hello():
    return "Hello, Quart world!"

@app.route('/json', methods=['POST'])
async def json_example():
    data = await request.get_json()
    return jsonify(data)

if __name__ == "__main__":
    app.run()