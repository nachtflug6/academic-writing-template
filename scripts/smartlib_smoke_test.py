#!/usr/bin/env python3

import json
import os
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


DEFAULT_API_URL = "http://localhost:8001"
DEFAULT_LIMIT = 3
TIMEOUT_SECONDS = 10


def get_api_base_url() -> str:
    return os.getenv("SMARTLIB_API_URL", DEFAULT_API_URL).rstrip("/")


def fetch_json(url: str) -> Any:
    request = Request(url, headers={"Accept": "application/json"})
    with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        charset = response.headers.get_content_charset("utf-8")
        return json.loads(response.read().decode(charset))


def print_json_block(title: str, payload: Any) -> None:
    print(title)
    print(json.dumps(payload, indent=2, ensure_ascii=True))
    print()


def summarize_documents(payload: dict[str, Any]) -> dict[str, Any]:
    documents = payload.get("documents", [])
    preview = []
    for document in documents:
        preview.append(
            {
                "id": document.get("id"),
                "title": document.get("title"),
                "year": document.get("year"),
                "authors": document.get("authors") or [],
            }
        )

    return {
        "total": payload.get("total"),
        "returned": payload.get("returned", len(documents)),
        "limit": payload.get("limit", len(documents)),
        "offset": payload.get("offset", 0),
        "has_more": payload.get("has_more", False),
        "documents_preview": preview,
    }


def main() -> int:
    api_base_url = get_api_base_url()
    health_url = f"{api_base_url}/health"
    documents_url = f"{api_base_url}/api/documents/?{urlencode({'limit': DEFAULT_LIMIT, 'offset': 0})}"

    print(f"Smart Library API smoke test")
    print(f"Base URL: {api_base_url}")
    print()

    try:
        health_payload = fetch_json(health_url)
        print_json_block("Health response:", health_payload)

        documents_payload = fetch_json(documents_url)
        print_json_block(
            "Documents response summary:",
            summarize_documents(documents_payload),
        )
    except HTTPError as error:
        print(f"HTTP error calling Smart Library API: {error.code} {error.reason}", file=sys.stderr)
        return 1
    except URLError as error:
        print(f"Network error calling Smart Library API: {error.reason}", file=sys.stderr)
        return 1
    except TimeoutError:
        print("Timed out waiting for Smart Library API response.", file=sys.stderr)
        return 1
    except json.JSONDecodeError as error:
        print(f"Received invalid JSON from Smart Library API: {error}", file=sys.stderr)
        return 1

    print("Smoke test passed: Smart Library API is reachable and returned valid document data.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())