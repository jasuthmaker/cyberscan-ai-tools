import re
import string
import json

def analyze_password(password: str) -> dict:
    analysis = {
        'length': len(password),
        'has_upper': any(char.isupper() for char in password),
        'has_lower': any(char.islower() for char in password),
        'has_digits': any(char.isdigit() for char in password),
        'has_symbols': any(char in string.punctuation for char in password),
        'score': 0,
        'strength': '',
        'feedback': []
    }

    # Calculate score based on length
    if analysis['length'] >= 16:
        analysis['score'] += 40
    elif analysis['length'] >= 12:
        analysis['score'] += 30
    elif analysis['length'] >= 8:
        analysis['score'] += 20

    # Calculate score based on character types
    if analysis['has_upper']:
        analysis['score'] += 15
    if analysis['has_lower']:
        analysis['score'] += 15
    if analysis['has_digits']:
        analysis['score'] += 15
    if analysis['has_symbols']:
        analysis['score'] += 15

    # Ensure score does not exceed 100
    analysis['score'] = min(analysis['score'], 100)

    # Determine password strength
    if analysis['score'] < 40:
        analysis['strength'] = 'Weak'
    elif analysis['score'] < 60:
        analysis['strength'] = 'Fair'
    elif analysis['score'] < 80:
        analysis['strength'] = 'Strong'
    else:
        analysis['strength'] = 'Very Strong'

    # Provide feedback for improvement
    if not analysis['has_upper']:
        analysis['feedback'].append('Add at least one uppercase letter')
    if not analysis['has_lower']:
        analysis['feedback'].append('Add at least one lowercase letter')
    if not analysis['has_digits']:
        analysis['feedback'].append('Add at least one digit')
    if not analysis['has_symbols']:
        analysis['feedback'].append('Add at least one symbol')
    if analysis['length'] < 8:
        analysis['feedback'].append('Increase password length to at least 8 characters')

    return analysis

if __name__ == '__main__':
    passwords = ['hello', 'Hello123', 'Tr0ub4dor&3', 'correct-horse-battery-staple']
    for password in passwords:
        analysis = analyze_password(password)
        print(json.dumps(analysis, indent=4))