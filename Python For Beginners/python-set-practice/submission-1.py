from typing import List

def contains_duplicate(words: List[str]) -> bool:
    unique = set(words)

    for target in unique:
        targetCount = 0
        for word in words:
            if word == target:
                targetCount += 1
        if targetCount > 1:
            return True
    
    return False
    

            

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
