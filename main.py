from flask import Flask, request, jsonify

app = Flask(__name__)

servers = {}

# POST /configure
@app.route('/configure', methods=['POST'])
def configure():
    data = request.json
    server_name = data.get('server_name')
    region = data.get('region')
    cpu = data.get('cpu')
    memory = data.get('memory')

    if not server_name or not region:
        return jsonify({"error": "server_name and region are required"}), 400

    servers[server_name] = {"region": region, "cpu": cpu, "memory": memory}
    return "200 OK", 200

# GET /system_usage
@app.route('/system_usage', methods=['GET'])
def system_usage():
    server_name = request.args.get('server_name')
    if server_name in servers:
        return jsonify(servers[server_name])
    return jsonify({"error": "Server not found"}), 404

# UPDATE /configure
@app.route('/configure', methods=['PUT'])
def update_configure():
    data = request.json
    server_name = data.get('server_name')
    region = data.get('region')

    if not server_name:
        return jsonify({"error": "server_name is required"}), 400

    if server_name not in servers:
        return jsonify({"error": "Server not found"}), 404

    if region:
        servers[server_name]["region"] = region

    return "200 OK", 200

if __name__ == '__main__':
    app.run(debug=True)
