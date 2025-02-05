

def countVowel(content):
    vowels = "aeiouy"
    numVowel = 0
    numWord = 0
    start_counting = False
    
    for line in content:
        if not (start_counting):
            if("CHAPTER 1. Loomings." in line):
                start_counting = True
            continue
        
        lowerVer = line.lower()
        numVowel += sum(lowerVer.count(vowel) for vowel in vowels)
        numWord += len(line.split())

    if numWord == 0:
        return 0
    
    avgVowel = numVowel / numWord
    return avgVowel

def printTxt(average):
    print("There are an average number of", average, "vowels per word in the text.")

contentArr = []
with open("pg2701.txt") as file:
    contentArr = file.readlines()

avgVowel = countVowel(contentArr)
printTxt(avgVowel)

    

    
    



