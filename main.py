from flask import Flask, request, jsonify
import psutil

app = Flask(__name__)

servers = {}


# POST /configure
@app.route('/configure', methods=['POST'])
def configure():
    data = request.json
    server_name = data.get('server_name')
    region = data.get('region')

    if not server_name or not region:
        return jsonify({"error": "server_name and region are required"}), 400

    servers[server_name] = {"region": region, "cpu_usage": 0, "memory_usage": 0}
    return "200 OK", 200


# GET /system_usage
@app.route('/system_usage', methods=['GET'])
def system_usage():
    server_name = request.args.get('server_name')

    if server_name in servers:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        servers[server_name]["cpu_usage"] = cpu_usage
        servers[server_name]["memory_usage"] = memory.percent

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
