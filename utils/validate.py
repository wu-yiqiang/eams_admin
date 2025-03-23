
import re

def isStrongPassword(password: str) -> bool:
    regex = re.compile(r'.*(?=.{6,16})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$')
    result = regex.match(password)
    return result


def isEmail(email: str) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    result = regex.match(email)
    return result
