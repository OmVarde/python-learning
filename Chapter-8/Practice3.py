# Open a file called report.txt in write mode

file = open("Chapter-8/report.txt","w")
store = file.write("Learning python step by step with practice questions")
file.close()
# "w" will overwrite everytime

#hence "a", append is use to add the sentence
filefile = open("Chapter-8/report.txt","a")
store = file.write("\nWith intersting projects")
file.close()