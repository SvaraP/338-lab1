
import timeit 

doc = 'pg2701.txt'

with open(doc, 'r', encoding='utf8') as file:
    content = file.read()
    
#print(content)


def vowel_count (word):
    vowels = 'aeiouy'
    word = word.lower()
    sum = 0 
    
    for char in word:
        if char in vowels:
            sum +=1
    return sum         

#print (vowel_count('svara'))

def vowel_total():
    num_vowel = 0 
    num_words = 0 
    
    #content divides into words
    words = content.split()
    
    for word in words:
        num_vowel += vowel_count(word)
        num_words += 1
    
    vowel_avg = num_vowel/num_words
    return vowel_avg


overall_time = timeit.timeit(lambda:vowel_total, number = 100)
avg_time = overall_time/100

print('On average the number of vowels per word:',vowel_total())
print('Average time for the code to run:', avg_time)
