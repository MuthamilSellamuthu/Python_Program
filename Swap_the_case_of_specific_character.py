/* 6. Kyathi is given a string where she needs to swap the case of all characters that appear after the letter 'z' in the alphabet string. If the string does not contain 'z', then no changes should be made.

Input Format:
A single line containing the string text.

Output Format:
Print the string after swapping the case of all characters that follow 'z'.
*/

  str=input(
  print(str[0:str.find('z')+1]+str[str.find('z')+1:].swapcase())
