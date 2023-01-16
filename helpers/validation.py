
from fastapi import HTTPException
import re

# for validating an Email
def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, email)


def validate(data, rules = []):
    result = []
    for key, values in rules:
        res = []
        for value in values:
            validator = value.split(':')
            if validator[0] == 'email' and not check_email(getattr(data, key)):
                res.append("{} Not Valid".format(key))
            if validator[0] == 'required' and getattr(data, key) == '':
                res.append("{} Required".format(key))
            if validator[0] == 'lt' and not getattr(data, key) < int(validator[1]):
                res.append("{} Must be less than {}".format(key, validator[1]))
            if validator[0] == 'lte' and not getattr(data, key) <= int(validator[1]):
                res.append("{} Must be less than or same as {}".format(key, validator[1]))
            if validator[0] == 'gt' and not getattr(data, key) > int(validator[1]):
                res.append("{} Must be greater than {}".format(key, validator[1]))
            if validator[0] == 'gte' and not getattr(data, key) >= int(validator[1]):
                res.append("{} Must be greater than or same as {}".format(key, validator[1]))
            if validator[0] == 'min' and len(getattr(data, key)) < int(validator[1]):
                res.append("{} Length Must be Longer than or same as {}".format(key, validator[1]))
            if validator[0] == 'max' and len(getattr(data, key)) > int(validator[1]):
                res.append("{} Length Must be Shorter than or same as {}".format(key, validator[1]))
            if validator[0] == 'equal' and len(getattr(data, key)) > int(validator[1]):
                res.append("{} Length Must be same as {}".format(key, validator[1]))
        if len(res) > 0:
            result.append({key: res})
    if len(result) > 0:
        raise HTTPException(status_code=422, detail=result)
