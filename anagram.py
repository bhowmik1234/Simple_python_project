def check_anagram():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the seocod word: ")
    L1 = list(word1)
    L2 = list(word2)
    sort_word1 = sorted(L1)
    sort_word2 = sorted(L2)

    if(sort_word2 == sort_word1):
        print(word1," and ", word2, " is Anagram")
    else:
        print(word1," and ", word2, " is not a Anagram")

check_anagram()