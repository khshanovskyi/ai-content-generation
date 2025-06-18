

def print_request(endpoint: str, request_data: dict, headers: dict):
    """Pretty print the request details."""
    print("\n" + "="*50 + " REQUEST " + "="*50)
    print(f"🔗 Endpoint: {endpoint}")

    print("\n📋 Headers:")
    safe_headers = headers.copy()
    if "api-key" in safe_headers:
        api_key = safe_headers["api-key"]
        safe_headers["api-key"] = f"{api_key[:8]}...{api_key[-4:]}" if len(api_key) > 12 else "***"

    for key, value in safe_headers.items():
        print(f"  {key}: {value}")

    print("\n📝 Request Body:")
    messages = request_data.get("messages", [])
    other_params = {k: v for k, v in request_data.items() if k != "messages"}

    if messages:
        print("  Messages:")
        for i, msg in enumerate(messages):
            role = msg.get("role", "unknown")
            content = msg.get("content", "")
            content_preview = content[:100] + "..." if len(content) > 100 else content
            print(f"    [{i+1}] {role.upper()}: {content_preview}")

    if other_params:
        print("\n  Parameters:")
        for key, value in sorted(other_params.items()):
            print(f"    {key}: {value}")

    print("="*107)