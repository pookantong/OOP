def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii') 
        except UnicodeDecodeError:
        return False
    else:
        return True
print(isEnglish(input()))