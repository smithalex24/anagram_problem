#ANAGRAM DETECTOR:
#Write a function called is_anagram that takes two string parameters and returns true if they are anagrams of one another; false otherwise. For example, "Mary" and "Army" inputs should return true, inputs "Hello" and "Bye" should return false. An additional requirement is case-insensitivPart 1: Dep ity.
#BONUS: ignore spaces, punctuation and anything besides alphanumeric.

#test case: "Mary" "Army" --> true
#test case: "Lamo", "Alamo" --> false
#test case (bonus): "I am Bobby B. Bobbington!!" "Bobby B. Bobbington, I am."




def is_anagram(str1, str2):
  if len(str1) != len(str2):
    return False
  for letter in str1.lower():
    if letter not in str2.lower():
      return False
  for letter in str2.lower():
    if letter not in str1.lower():
      return False
  return True

print(is_anagram("Mary", "Army"))
print(is_anagram("Lamo", "Alamo"))
print(is_anagram("Alex", "Jared"))
print(is_anagram("I am Bobby B. Bobbington!!", "Bobby B. Bobbington, I am."))