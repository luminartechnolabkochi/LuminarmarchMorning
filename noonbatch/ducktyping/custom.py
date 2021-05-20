def chk_age(age):
    if age<18:
        raise Exception("invalid age")
    else:
        pass

try:
    chk_age(17)
except Exception as e:


