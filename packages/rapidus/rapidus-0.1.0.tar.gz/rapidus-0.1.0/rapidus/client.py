import requests
from requests import Session, request
from requests.structures import CaseInsensitiveDict
from allure import step, attach, attachment_type


class ApiResponse:
    """Class to encapsulate and validate HTTP response data."""

    def __init__(self, response: requests.Response) -> None:
        """
        Initialize ApiResponse with a given HTTP response.

        Args:
            response (requests.Response): The HTTP response object from the requests library.
        """
        self.response: requests.Response = response
        self.status_code: int = response.status_code
        self.headers: dict = dict(response.headers)
        self.text: str = response.text
        try:
            self.json_data: dict = response.json()
        except ValueError:
            self.json_data = None

    @step(title='Assert status code is {expected}')
    def assert_status_code(self, expected: int):
        """
        Assert that the HTTP status code matches the expected value.

        Args:
            expected (int): The expected HTTP status code.

        Raises:
            AssertionError: If the actual status code does not match the expected value.

        Returns:
            ApiResponse: Self for method chaining.
        """
        actual: int = self.response.status_code
        if actual != expected:
            raise AssertionError(f'Expected status code {expected}, but got {actual}')
        return self

    @step(title='Assert response time is less than {max_time_ms}ms')
    def assert_response_time(self, max_time_ms: int):
        """
        Assert that the response time is less than the specified limit.

        Args:
            max_time_ms (int): The maximum allowed response time in milliseconds.

        Raises:
            AssertionError: If the response time exceeds the limit.

        Returns:
            ApiResponse: Self for method chaining.
        """
        response_time: float = self.response.elapsed.total_seconds() * 1000
        if response_time > max_time_ms:
            raise AssertionError(f'Response time {response_time}ms exceeded the limit of {max_time_ms}ms')
        return self

    @step(title='Assert JSON contains key "{key}" with value "{value}"')
    def assert_json_contains(self, key, value=None):
        """
        Assert that the JSON response contains a specific key with an optional expected value.

        Args:
            key (str): The key to check in the JSON response.
            value (Any, optional): The expected value for the key. Defaults to None.

        Raises:
            AssertionError: If the key is missing or the value does not match.

        Returns:
            ApiResponse: Self for method chaining.
        """
        json_data = self.response.json()
        if key not in json_data:
            raise AssertionError(f'Key "{key}" not found in response JSON')
        if value is not None and json_data[key] != value:
            raise AssertionError(f'Value for key "{key}" is "{json_data[key]}", but expected "{value}"')
        return self

    @step(title='Assert response body contains substring "{substring}"')
    def assert_body_contains(self, substring):
        """
        Assert that the response body contains a specific substring.

        Args:
            substring (str): The substring to search for in the response body.

        Raises:
            AssertionError: If the substring is not found.

        Returns:
            ApiResponse: Self for method chaining.
        """
        body: str = self.response.text
        if substring not in body:
            raise AssertionError(f'Substring "{substring}" not found in response body')
        return self

    @step(title='Assert header "{header_name}" contains value "{value}"')
    def assert_header_contains(self, header_name, value=None):
        """
        Assert that the response headers contain a specific header with an optional expected value.

        Args:
            header_name (str): The name of the header to check.
            value (str, optional): The expected value for the header. Defaults to None.

        Raises:
            AssertionError: If the header is missing or the value does not match.

        Returns:
            ApiResponse: Self for method chaining.
        """
        headers: CaseInsensitiveDict[str] = self.response.headers
        if header_name not in headers:
            raise AssertionError(f'Header "{header_name}" not found in response')
        if value is not None and headers[header_name] != value:
            raise AssertionError(f'Value for header "{header_name}" is "{headers[header_name]}", but expected "{value}"')
        return self

    def __repr__(self) -> str:
        """
        Return a string representation of the ApiResponse object.

        Returns:
            str: A formatted string containing status code, headers, text, and JSON data.
        """
        return (
            f'ApiResponse(\n'
            f'  Status Code: {self.status_code},\n'
            f'  Headers: {self.headers},\n'
            f'  Text: {self.text[:50]}{"..." if len(self.text) > 50 else ""},\n'
            f'  JSON: {self.json_data}\n'
            f')'
        )


class Client:
    """Class to manage API client sessions and send HTTP requests."""

    def __init__(self, base_url: str, use_session: bool = False) -> None:
        """
        Initialize the Client with a base URL and optional session usage.

        Args:
            base_url (str): The base URL for all API requests.
            use_session (bool, optional): Boolean flag to enable/disable session usage. Defaults to False.
        """
        self.base_url: str = base_url
        self.session: Session | None = Session() if use_session else None

    @step(title='Send request: {method} {endpoint}')
    def send_request(self, method: str, endpoint: str, **kwargs) -> ApiResponse:
        """
        Send an HTTP request to the specified endpoint.

        Args:
            method (str): The HTTP method (e.g., GET, POST, PUT, DELETE).
            endpoint (str): The API endpoint to send the request to.
            **kwargs: Additional parameters for the request (e.g., headers, data, json).

        Returns:
            ApiResponse: An ApiResponse object containing the response details.
        """
        url: str = f'{self.base_url}{endpoint}'
        headers = kwargs.get('headers', {})
        data = kwargs.get('data', None)
        json_payload = kwargs.get('json', None)

        # Log request details
        with step(f'Request details: {method} {url}'):
            request_details: str = (
                f'Method: {method}\n'
                f'URL: {url}\n'
                f'Headers: {headers}\n'
                f'Data: {data}\n'
                f'JSON Payload: {json_payload}'
            )
            attach(
                body=request_details,
                name='Request Details',
                attachment_type=attachment_type.TEXT
            )

        # Send the request
        try:
            if self.session:
                response: requests.Response = self.session.request(method=method, url=url, **kwargs)
            else:
                response = request(method=method, url=url, **kwargs)
        except Exception as e:
            error_message = f'Error during request: {e}'
            attach(
                body=error_message,
                name='Request Error',
                attachment_type=attachment_type.TEXT
            )
            raise

        # Log response details
        with step(f'Response details: Status Code={response.status_code}'):
            response_details: str = (
                f'Status Code: {response.status_code}\n'
                f'Headers: {dict(response.headers)}\n'
                f'Body: {response.text}'
            )
            attach(
                body=response_details,
                name='Response Details',
                attachment_type=attachment_type.TEXT
            )

            # Attach JSON response if available
            try:
                json_response = response.json()
                attach(
                    body=str(json_response),
                    name='Response JSON',
                    attachment_type=attachment_type.JSON
                )
            except ValueError:
                pass  # Ignore if response is not JSON

        return ApiResponse(response=response)

    def close(self) -> None:
        """
        Close the session if it is being used.
        """
        if self.session:
            self.session.close()
