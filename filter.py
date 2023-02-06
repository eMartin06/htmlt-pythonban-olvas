from bleach import clean
import re

whitelist = ['ul','li','ol','strong','b','br','p']

def clean_spaces_and_newlines(src):
   # match characters, ,.!, and new line: \w+[,.!]?\\n?
   # match opening tags: <\w+>
   # match closing tags: </\w+>
   # combine them with ppe | (or) symbol
   
   result = re.findall("\w+[,.!]?\\n?|<\w+>\\n?", src)
   return result
      
with open('goldi2.html','r', encoding='utf-8') as html_file:
    html = html_file.read()
    
    html_cleaned = clean(html, strip=True, tags=whitelist,)
    
    print(html_cleaned) 
    
    