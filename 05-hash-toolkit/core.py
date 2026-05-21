import hashlib
import base64
import urllib.parse
import html
import math
import collections
import json

def hash_text(text: str) -> dict:
    md5 = hashlib.md5(text.encode()).hexdigest()
    sha1 = hashlib.sha1(text.encode()).hexdigest()
    sha256 = hashlib.sha256(text.encode()).hexdigest()
    sha512 = hashlib.sha512(text.encode()).hexdigest()
    blake2b = hashlib.blake2b(text.encode()).hexdigest()
    freqs = collections.Counter(text)
    total = sum(freqs.values())
    entropy = -sum((freq / total) * math.log2(freq / total) for freq in freqs.values())
    entropy = round(entropy, 2)
    return {
        "md5": md5,
        "sha1": sha1,
        "sha256": sha256,
        "sha512": sha512,
        "blake2b": blake2b,
        "entropy": entropy
    }

def encode_text(text: str) -> dict:
    base64_encoded = base64.b64encode(text.encode()).decode()
    hex_encoded = text.encode().hex()
    url_encoded = urllib.parse.quote(text)
    html_encoded = html.escape(text)
    return {
        "base64": base64_encoded,
        "hex": hex_encoded,
        "url_encoded": url_encoded,
        "html_encoded": html_encoded
    }

def decode_base64(encoded: str) -> dict:
    try:
        decoded = base64.b64decode(encoded).decode()
        return {
            "success": True,
            "decoded": decoded,
            "error": None
        }
    except Exception as e:
        return {
            "success": False,
            "decoded": None,
            "error": str(e)
        }

if __name__ == "__main__":
    text = 'Hello, CyberScan AI!'
    hash_result = hash_text(text)
    print(json.dumps(hash_result, indent=2))
    encode_result = encode_text(text)
    print(json.dumps(encode_result, indent=2))
    base64_encoded = encode_result["base64"]
    decode_result = decode_base64(base64_encoded)
    print(json.dumps(decode_result, indent=2))