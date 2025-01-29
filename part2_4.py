import timeit

def countVowel(content):
    vowels = "aeiouy"
    index = 0
    numVowel = 0
    numWord = 0
    for i, l in enumerate(content):
        if "CHAPTER 1. Loomings." in l:
            index = i
            
            
    for ind, line in enumerate(content):
        if(ind >= index):
            lower = line.lower()
            numVowel += sum(lower.count(vowel) for vowel in vowels);
            numWord += len(content[ind].split())

    avg = numVowel / numWord
    return avg

def printTxt(average):
    print("There are an average number of", average, "vowels per word in the text.")

contentArr = []
with open("pg2701.txt") as file:
    contentArr = file.readlines()

avgVowel = countVowel(contentArr)
printTxt(avgVowel)

elapsed_time = timeit.timeit(lambda : countVowel(100), number=1)
print(f'Elapsed time: {elapsed_time} seconds')

    
    



