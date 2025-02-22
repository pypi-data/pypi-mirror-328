# Mock IT Adapter

A Python library for interacting with Mock IT API.

## Installation

```bash
pip install mock-it-adapter
```
## Usage

```doctest
from mock_it_adapter import MockITClient

client = MockITClient(base_url="http://localhost:20000")

resource = client.create_mock(
    method="POST",
    endpoint="/new_mock_endpoint",
    response_body="{\"json_body\": \"example mock response body\"}"
)
```