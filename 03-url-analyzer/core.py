import urllib.parse
import re
import json

def analyze_url(url: str) -> dict:
    result = {
        'valid': False,
        'scheme': '',
        'domain': '',
        'path': '',
        'risk_score': 0,
        'risk_level': '',
        'risks': [],
        'has_ip_host': False,
        'has_suspicious_tld': False,
        'is_shortened': False,
        'subdomain_count': 0
    }
    try:
        parsed_url = urllib.parse.urlparse(url)
        result['valid'] = True
        result['scheme'] = parsed_url.scheme
        result['domain'] = parsed_url.netloc
        result['path'] = parsed_url.path

        if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', result['domain']):
            result['has_ip_host'] = True
            result['risk_score'] += 30
            result['risks'].append('IP host')

        suspicious_tlds = ['.xyz', '.tk', '.ml', '.ga', '.cf', '.top', '.click', '.download']
        for tld in suspicious_tlds:
            if result['domain'].endswith(tld):
                result['has_suspicious_tld'] = True
                result['risk_score'] += 25
                result['risks'].append('Suspicious TLD')

        shortened_domains = ['bit.ly', 'tinyurl.com', 't.co', 'goo.gl', 'ow.ly']
        for domain in shortened_domains:
            if result['domain'] == domain:
                result['is_shortened'] = True
                result['risk_score'] += 20
                result['risks'].append('Shortened URL')

        subdomains = result['domain'].split('.')
        result['subdomain_count'] = len(subdomains) - 2
        if result['subdomain_count'] > 3:
            result['risk_score'] += 15
            result['risks'].append('Multiple subdomains')

        if result['scheme'] == 'http':
            result['risk_score'] += 10
            result['risks'].append('HTTP scheme')

        if any(word in result['path'] for word in ['login', 'admin', 'bank']):
            result['risk_score'] += 20
            result['risks'].append('Path risk')

        if result['risk_score'] <= 20:
            result['risk_level'] = 'Safe'
        elif result['risk_score'] <= 40:
            result['risk_level'] = 'Low'
        elif result['risk_score'] <= 60:
            result['risk_level'] = 'Medium'
        elif result['risk_score'] <= 80:
            result['risk_level'] = 'High'
        else:
            result['risk_level'] = 'Critical'
    except ValueError:
        pass
    return result

if __name__ == '__main__':
    test_cases = [
        'https://google.com/search?q=test',
        'http://192.168.1.1/admin',
        'https://free.money.win.tk/click/now/login',
        'https://bit.ly/abc123'
    ]
    for test_case in test_cases:
        result = analyze_url(test_case)
        print(json.dumps(result, indent=2))