def get_response_content_from_execution_response(execution_response: dict) -> str:
    return execution_response.get('content', '')

def get_response_object_from_execution_response(execution_response: dict) -> dict:
    return execution_response.get('response', {})

def get_stop_reason_from_response_object(response_object: dict) -> str:
    return response_object['choices'][0]['finish_reason']

def get_stop_reason_from_execution_response(execution_response: dict) -> str:
    return get_stop_reason_from_response_object(get_response_object_from_execution_response(execution_response))

def is_max_tokens_stop_reason(stop_reason: str) -> bool:
    return stop_reason == "length"
