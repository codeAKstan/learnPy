import re
def validate_email(email):
    pattern = r'^[a-zA-Z][\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(validate_email('tes.t@example.com'))
print(validate_email('invalid-email')) 
