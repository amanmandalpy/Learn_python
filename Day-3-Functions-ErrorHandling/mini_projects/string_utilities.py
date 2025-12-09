# palindrome, vowels, reverse_words

def is_palindrome(s: str) -> bool:
    t = ''.join(ch.lower() for ch in s if ch.isalnum())

    return t == t[::-1]

def count_vowels(s: str) -> int:
    return sum(1 for ch in s.lower() if ch in 'aeiouAEIOU')

def reverse_words(s: str) -> str:
    return ' '.join(reversed(s.split()))

if __name__ == "__main__":
    s = input("Enter string: ")

    print("Palindrome: ", is_palindrome(s))
    print("Vowels: ", count_vowels(s))
    print("Reversed words: ", reverse_words(s))