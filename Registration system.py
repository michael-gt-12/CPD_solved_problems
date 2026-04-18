n = int(input())
word_map = {}
for _ in range(n):
    word = input()
    val = word_map.get(word,0)
    if val == 0:
        word_map[word] = 1
        print("OK")
    else:
        word_map[word] = val + 1
        print(f"{word}{val}")
    
