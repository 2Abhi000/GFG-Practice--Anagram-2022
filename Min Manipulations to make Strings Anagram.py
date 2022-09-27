#Min Manipulations to make Strings Anagram
def minManipulation(s1,s2): 
    def isanagram(stri,strin):
        if len(stri) == len(strin) and sorted(stri)==sorted(strin):
            return True
        else:
            return False
    if (isanagram(s1,s2)):
        print("Both the strings are already anagrams.")
    else:
        se=set(s1)
        se2=set(s2)
        if se.intersection(se2):
            anss=se.intersection(se2)
        print(len(anss))
st=input("Enter the string: ")
st2=input("Enter the string 2: ")
ans=minManipulation(st,st2)

