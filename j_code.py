import os

#The song that is going to be played
notes = "piano: b a g r b a g r b8 > b b b a a a a g g g g b < a g r"

#Name of file
test = "Test"
test_object = open(test+".txt","w")
test_object.write(notes)
test_object.close()
os.system("./alda play -f "+test+".txt")
