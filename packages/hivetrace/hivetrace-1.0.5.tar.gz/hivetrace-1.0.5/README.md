# Hivetrace SDK

## Description
Hivetrace SDK is designed for integration with the Hivetrace service, providing monitoring of user prompts and LLM responses.
The SDK automatically loads the configuration and sends data to the API

## Installation

Install the SDK via pip:

```sh
pip install hivetrace
```

## Usage

```python
from hivetrace.hivetrace import HivetraceSDK
```

Create a hivetrace_config.json with the contents:
```json
{
  "hivetrace_url": "https://your-hivetrace-instance.com"
}
```
Specify the path to the config

```python
hivetrace_config_path = "your/path/hivetrace_config.json"
```

# Initialize the SDK
hivetrace = HivetraceSDK(hivetrace_config_path)

```python
# Send a user prompt
response = hivetrace.send_in(
    application_id="123",
    message="The monitoring user prompt is sent here",
    additional_parameters={
        "user_id": "1"
    }
)

# Send a response from your LLM
response = hivetrace.send_out(
    application_id="123",
    message="The monitoring llm response is sent here",
    additional_parameters={
        "agent_id": "2"
    }
)
```

## API

### `monitor_user(application_id: str, message: str, additional_parameters: dict = None) -> dict`
Sends a user prompt to the Hivetrace

- `application_id` - application identifier
- `message` - user prompt
- `additional_parameters` - dictionary of additional parameters (optional)

#### Response Example for monitor_user()
```json
{
    "status": "processed",
    "total_user_monitoring_result": [
        {
            "is_toxic": true,
            "type_of_violation": "injection"
        }
    ]
}
```

### `monitor_llm(application_id: str, message: str, additional_parameters: dict = None) -> dict`
Sends an LLM response to the Hivetrace

- `application_id` - application identifier
- `message` - LLM response
- `additional_parameters` - dictionary of additional parameters (optional)

#### Response Example for monitor_llm()
```json
{
    "status": "processed",
    "llm monitoring result": {
        "is_toxic": false,
        "type_of_violation": "safe"
    }
}
```

## Additional Parameters
The `additional_parameters` argument is a flexible dictionary that allows passing extra metadata along with requests

## Configuration

The SDK loads configuration from the client file. The allowed domain (`hivetrace_url`) is automatically retrieved from the configuration.
If the domain is not specified, the SDK raises a `HostNotFound` error

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

