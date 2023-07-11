def solution(myString):
    
    mystringlen = len(myString)
    
    if not myString.isalpha():
        return false
    if not mystringlen >= 1 and mystringlen <= 100000:
        return false
    
    return myString.lower()
