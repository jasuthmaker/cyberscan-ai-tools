import re
import json

def scan_text(text: str) -> dict:
    result = {
        'word_count': len(text.split()),
        'char_count': len(text),
        'sentence_count': text.count('.') + text.count('!') + text.count('?'),
        'contains_pii': False,
        'pii_found': [],
        'sensitive_keywords_found': [],
        'risk_level': 'Clean',
        'summary': ''
    }

    patterns = {
        'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'phone_us': r'(\d{3})[-.\s]?\d{3}[-.\s]?\d{4}',
        'ssn': r'\d{3}-\d{2}-\d{4}',
        'credit_card': r'\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}',
        'ip_address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    }

    for type, pattern in patterns.items():
        matches = re.finditer(pattern, text)
        for match in matches:
            result['pii_found'].append({
                'type': type,
                'value': match.group(),
                'position': match.start()
            })
            result['contains_pii'] = True

    sensitive_keywords = ['password', 'secret', 'api_key', 'token', 'private_key', 'credential']
    for keyword in sensitive_keywords:
        if keyword in text.lower():
            result['sensitive_keywords_found'].append(keyword)

    if result['contains_pii'] and result['sensitive_keywords_found']:
        result['risk_level'] = 'High'
    elif result['contains_pii'] or result['sensitive_keywords_found']:
        result['risk_level'] = 'Medium' if len(result['pii_found']) > 1 or len(result['sensitive_keywords_found']) > 1 else 'Low'
    elif len(result['pii_found']) > 1 or len(result['sensitive_keywords_found']) > 1:
        result['risk_level'] = 'Low'

    result['summary'] = f'Text contains {result["word_count"]} words, {result["char_count"]} characters, and {result["sentence_count"]} sentences. Risk level: {result["risk_level"]}'

    return result

if __name__ == '__main__':
    texts = [
        'The weather is nice today.',
        'Email john@example.com and call 555-123-4567',
        'api_key=sk_live_abc123 password=hunter2'
    ]
    for text in texts:
        result = scan_text(text)
        print(json.dumps(result, indent=2))