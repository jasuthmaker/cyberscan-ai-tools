import ipaddress
import json

def classify_ip(ip: str) -> dict:
    try:
        ip_obj = ipaddress.ip_address(ip)
    except ValueError:
        return {
            'valid': False,
            'version': 'Invalid',
            'is_private': False,
            'is_loopback': False,
            'is_multicast': False,
            'is_global': False,
            'ip_class': 'N/A',
            'description': 'Invalid IP address'
        }

    is_private = ip_obj.is_private
    is_loopback = ip_obj.is_loopback
    is_multicast = ip_obj.is_multicast
    is_global = not is_private and not is_loopback and not is_multicast

    if isinstance(ip_obj, ipaddress.IPv4Address):
        version = 'IPv4'
        first_octet = int(str(ip_obj).split('.')[0])
        if first_octet < 128:
            ip_class = 'A'
        elif first_octet < 192:
            ip_class = 'B'
        elif first_octet < 224:
            ip_class = 'C'
        elif first_octet < 240:
            ip_class = 'D'
        else:
            ip_class = 'E'
    elif isinstance(ip_obj, ipaddress.IPv6Address):
        version = 'IPv6'
        ip_class = 'N/A'
    else:
        version = 'Invalid'
        ip_class = 'N/A'

    description = f'{version} address {"(private)" if is_private else "(global)"}'

    return {
        'valid': True,
        'version': version,
        'is_private': is_private,
        'is_loopback': is_loopback,
        'is_multicast': is_multicast,
        'is_global': is_global,
        'ip_class': ip_class,
        'description': description
    }

if __name__ == "__main__":
    ip_addresses = ['192.168.1.1', '8.8.8.8', '127.0.0.1', '::1', '224.0.0.1', '999.999.999.999']
    for ip in ip_addresses:
        result = classify_ip(ip)
        print(json.dumps(result, indent=2))