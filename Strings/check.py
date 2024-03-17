# Program to check whether the specified character is available in a string or not without using
# builtin functions.

def is_char_in_string(char, string):

  for c in string:
    if c == char:
      return True
  return False

string = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
char = 'o'

if is_char_in_string(char, string):
  print(f"The character '{char}' is present in the string.")
else:
  print(f"The character '{char}' is not present in the string.")
