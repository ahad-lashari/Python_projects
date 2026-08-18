"""Word Counter"""
print(__doc__)
while True:
    word=input("Enter any Word:")
    if word.isalpha():
        print(f"Length of the Word is {len(word)}")
        break
    else:
        print(f"{word} is not a Alphabetic word Enter Alphabetic word")
        continue
    