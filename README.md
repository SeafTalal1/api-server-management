# api-server-management
Flask-based API for managing and configuring server data, including adding, updating, and retrieving server configurations. This API supports POST and PUT requests for adding and modifying server details like region, and GET requests for viewing system information.

# Flask Server Configuration API

This is a simple Flask-based API for managing and configuring server data. It allows you to add, update, and retrieve server configurations.

## Features

- **POST /configure**: Adds a new server configuration.
- **PUT /configure**: Updates an existing server's region.
- **GET /system_usage**: Retrieves the system usage details (CPU, memory, region) for a specific server.

## API Endpoints

### 1. **POST /configure**
Adds a new server configuration.

- **Request**: 
    - JSON body with the following fields:
        - `server_name` (string): The name of the server.
        - `region` (string): The region where the server is located.
        
    Example:
    ```json
    {
        "server_name": "server1",
        "region": "us-east-1"
    }
    ```

- **Response**:
    - `200 OK`: Successfully added the server configuration.

### 2. **PUT /configure**
Updates an existing server configuration (e.g., region).

- **Request**:
    - JSON body with the following fields:
        - `server_name` (string): The name of the server to update.
        - `region` (string): The new region to assign to the server.

    Example:
    ```json
    {
        "server_name": "server1",
        "region": "us-west-2"
    }
    ```

- **Response**:
    - `200 OK`: Successfully updated the server configuration.

### 3. **GET /system_usage**
Retrieves system usage details (CPU, memory, region) for a specific server.

- **Request**: 
    - URL query parameter `server_name`: The name of the server to get the system usage details for.

    Example:
    ```bash
    GET /system_usage?server_name=server1
    ```

- **Response**:
    - JSON object with the server's CPU, memory usage, and region.

    Example:
    ```json
    {
        "server_name": "server1",
        "region": "us-east-1",
        "cpu": 10,
        "memory": 512
    }
    ```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/seaftalal1/server-config-api.git
    ```

2. Navigate to the project directory:
    ```bash
    cd server-config-api
    ```

3. Create a virtual environment (if not already created):
    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On Linux/Mac:
      ```bash
      source venv/bin/activate
      ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the Flask app:
    ```bash
    python app.py
    ```

The API will be running at `http://localhost:5000`.

## Technologies Used

- **Flask**: Python web framework for building the API.
- **Python**: Programming language used for the project.
- **JSON**: Used for data exchange between client and server.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
