import curlparser
from bomber import bomber
from urllib.parse import urlparse, parse_qsl


def process(text):
    text = text.replace("--compressed", "")

    result = curlparser.parse(text)

    parsed = urlparse(result.url)
    args = parse_qsl(parsed.query)

    headers = {}

    json_data = {
        "method": result.method,
        "url": result.url,
        "headers": headers,
    }

    if args:
        json_data["url"] = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        json_data["params"] = {k: v for k, v in args}

    if result.header:
        headers = {k.lower(): v.strip() for k, v in result.header.items()}
        
        json_data["headers"].update(headers)

        if "user-agent" in headers:
            del headers["user-agent"]

    if result.data:
        content_type = headers.get("content-type", "").strip()
        if content_type.startswith("application/x-www-form-urlencoded"):
            json_data["data"] = dict(parse_qsl(result.data))
        else:
            json_data["json"] = result.data

    return json_data


def main():
    print("Enter request data: (Press Ctrl+D (on Linux/Mac) or Ctrl+Z (on Windows) to finish input)")

    user_input = []
    try:
        while True:
            user_input.append(input())
    except EOFError:
        pass

    data = process('\n'.join(user_input))
    bomber(data)


if __name__ == "__main__":
    main()
