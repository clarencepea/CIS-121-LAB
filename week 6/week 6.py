'''
def hailstone_seq(number):
    output_list = []
    while number >= 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = (3 * number) + 1
        
        print(number)

        output_list.append(number)

    return output_list




print(f"{hailstone_seq(25)}")

'''
'''
cards = [5, 9, 10, 3, "j", "a", 4, 8, 5]
for cards in cards:
    if temp_card in ["2", "3", "4", "5", "6"]:
        point += 1
    elif temp_card in ['10', 'j', 'q', 'k', 'a']

print(f"Total count : {count{cards}}")

'''

def is_acronym(s, words):
    if len(s) != len(words):
        return False
    for i in range(0, len(words)):
        if words[i] == "":
            return False
        if

    
    return True

s = "abc"
words = ["alice", "bob", "charlie"]

print(f"{is_acronym{s, words}}")