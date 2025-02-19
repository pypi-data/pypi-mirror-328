# API Testing Framework for Python

This Python package is designed to accelerate the development of API tests by providing a robust and flexible framework. It integrates seamlessly with [Allure](https://docs.qameta.io/allure/) for detailed reporting, ensuring that every request and assertion is logged and visible in the test reports.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

---

## Overview

This framework simplifies the process of creating API tests by encapsulating HTTP requests and responses into reusable components. The `Client` class manages API sessions, while the `ApiResponse` class provides methods for validating HTTP responses. All interactions and assertions are automatically logged in Allure reports, making it easier to debug and analyze test results.

---

## Features

- **Simplified Request Management**: Easily send HTTP requests using the `Client` class.
- **Response Validation**: Use the `ApiResponse` class to validate status codes, response times, JSON data, headers, and more.
- **Allure Integration**: Automatically log request and response details in Allure reports.
- **Method Chaining**: Chain multiple assertions for cleaner and more readable test code.
- **Session Support**: Optionally use persistent sessions for better performance during test execution.

---

## Installation

To install this package, you can use `pip`. First, ensure that you have Python 3.11+ installed on your system.

```bash
pip install rapidus
```

Alternatively, if you are using this as part of a project, include it in your `requirements.txt` file:

```
rapidus
```

---

## Usage

### Step 1: Import the Classes

```python
from rapidus import Client
```

### Step 2: Initialize the Client

```python
base_url = "https://api.example.com"
client = Client(base_url=base_url, use_session=True)  # Use sessions for better performance
```

### Step 3: Send Requests and Validate Responses

```python
client.send_request(
    method="GET",
    endpoint="/users",
    headers={"Authorization": "Bearer <token>"}
).assert_status_code(200).assert_response_time(500).assert_json_contains("id", 123)
```

### Step 4: Close the Session (If Used)

```python
client.close()
```

---

## Examples

### Example 1: Basic GET Request

```python
from rapidus import Client


Client(base_url="https://jsonplaceholder.typicode.com").send_request("GET", "/posts/1").assert_status_code(200).assert_json_contains("userId", 1)
```

### Example 2: POST Request with JSON Payload

```python
from rapidus import Client


client = Client(base_url="https://jsonplaceholder.typicode.com", use_session=True)

payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = client.send_request(
    method="POST",
    endpoint="/posts",
    json=payload
)

response.assert_status_code(201).assert_json_contains("id")
client.close()
```

---

## Contributing

We welcome contributions from the community! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -m "Add new feature"`).
4. Push the branch (`git push origin feature/new-feature`).
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contact

If you have any questions or need further assistance, feel free to open an issue or contact us directly.

Happy testing! 🚀