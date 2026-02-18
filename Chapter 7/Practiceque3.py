# write a function that takes a string and returns the count of the vowels and 
# consonants separetely


def vowConso(VowCon):
    #define vowels
    vowels = "aeiouAEIOU"
    countvowel = 0
    countconso = 0

    for eachchar in VowCon:
        if eachchar.isalpha():
            if eachchar in vowels:
                countvowel +=1
            else:
                countconso +=1
    return countvowel,countconso


vowel , Consonant = vowConso("Om Varde")
print (vowel , Consonant)