# python3
#Anastasija Andrjuscenko 221RDB170

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
  return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
  opening_brackets_stack = []
  for i, next in enumerate(text):
    if next in "([{":
      opening_brackets_stack.append(Bracket(next, i))
      pass
 
    if next in ")]}":
      if not opening_brackets_stack:
        return(i+1)
      if are_matching(opening_brackets_stack[-1].char, next):
        opening_brackets_stack.pop()
      elif not are_matching(opening_brackets_stack[-1].char, next):
        return(i+1)
  if opening_brackets_stack:
    return(opening_brackets_stack[0].position+1)
  else:
    return "Success"
    
def main():
  ievade = input()
  if ievade[0] == "I":
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    
if __name__ == "__main__":
  main()
