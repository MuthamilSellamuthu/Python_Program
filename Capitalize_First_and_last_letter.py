/*You are designing a tool that capitalizes only the first and last letter of each word in a string, but before performing this task, the string should be reversed. For each word:
Reverse the word first.
Capitalize the first and last letter of the reversed word.
All other characters should remain unchanged.
Create a class named TextAnalyzer with the following attributes:
An attribute text that stores a string provided by the user.
Create a class named CapitalizeFirstLastAfterReverse that inherits from TextAnalyzer and has the following characteristics:
A method inputText() that takes user input for the text attribute.
A method capitalizeFirstLastAfterReverse() that reverses each word and then capitalizes only the first and last letter of each word.

Input Format:
A single line of input representing the string to analyze.

Output Format:
A string where the words are reversed, and only the first and last letters of each reversed word are capitalized.
*/

class TextAnalyzer:
  def __init__(self):
    self.text=""
class CapitalizeFirstLastAfterReverse(TextAnalyzer):
  def inputText(self):
    self.text=input()
  def capitalizeFirstLastAfterReverse(self):
    self.text=self.text.split(" ")
    res=""
    for i in self.text:
        rev=i[::-1]
        if len(rev)>1:
          rev=rev[0].upper()+rev[1:-1]+rev[-1].upper()
        else:
          rev=rev.upper()
        res+=rev+" "
      return res.strip()
pattern=CapitalizeFirstLastAfterReverse()
pattern.inputtext()
print(pattern.capitalizeFirstLastAfterReverse())
