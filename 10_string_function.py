# String functions in python

# 1. len() => to find length of the string

print("To calculate length of the string by len() function:")
name = "shailesh"
length = len(name) 
print("Length of the string:",length)


# 2 . string.replace(old word , new word) -> can replace the word , character or string

print("\nreplace() function:") 
name = name.replace("h" , "a")
print("After replacing h with a ",name)

name = 'hello word'
print("After replacing word with world:",name.replace("word","world"))
print("Actually not changed in string:",name)    # -> this is remain same as the hello word string
# to replace it in name we have to make changes in name itself
# name = name.replace("word","world")
print("Actual change in string:",name)


# 3. find() -> to find word , spaces , string , etc
print("\nfind() function : ")
IndexOfFoundword = name.find("word")
print("Index of the found 'word' : ",IndexOfFoundword)
