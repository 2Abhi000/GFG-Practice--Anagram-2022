#Anagram of string
def count_operations(str1,str2):
   m = {}
   count = 0
   for i in str2:
       if i in m:
           m[i] += 1
       else:
           m[i] =1
   for i in str1:
       if i in m:
           if m[i] == 1:
               m.pop(i)
               continue
           m[i] -= 1
       else:
           count += 1
   s = 0
   for key in m:
       s += m[key]
   return count + s
s=input("Enter the s1: ")
ss=input("Enter the s2: ")
ans=count_operations(s,ss)
print(ans)