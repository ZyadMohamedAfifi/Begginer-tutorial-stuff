alphabet_shift = {
    'a': 'b',
    'b': 'c',
    'c': 'd',
    'd': 'e',
    'e': 'f',
    'f': 'g',
    'g': 'h',
    'h': 'i',
    'i': 'j',
    'j': 'k',
    'k': 'l',
    'l': 'm',
    'm': 'n',
    'n': 'o',
    'o': 'p',
    'p': 'q',
    'q': 'r',
    'r': 's',
    's': 't',
    't': 'u',
    'u': 'v',
    'v': 'w',
    'w': 'x',
    'x': 'y',
    'y': 'z',
    'z': 'a'
}

alphabet_unshift = {
    'b': 'a',
    'c': 'b',
    'd': 'c',
    'e': 'd',
    'f': 'e',
    'g': 'f',
    'h': 'g',
    'i': 'h',
    'j': 'i',
    'k': 'j',
    'l': 'k',
    'm': 'l',
    'n': 'm',
    'o': 'n',
    'p': 'o',
    'q': 'p',
    'r': 'q',
    's': 'r',
    't': 's',
    'u': 't',
    'v': 'u',
    'w': 'v',
    'x': 'w',
    'y': 'x',
    'z': 'y',
    'a': 'z'
}

Sentence = input ("Enter your message").strip().lower()
def Encode():
   Encoded= ""
    
   for char in Sentence:
     if char in alphabet_shift:
      Encoded += alphabet_shift[char]
     else:
       Encoded += char
 
   print("encoded message", Encoded)
   return

def Decoding():
  Decoded= ""
  
  for char in Sentence:
   if char in alphabet_unshift:
     Decoded += alphabet_unshift[char]
   else:
     Decoded += char
  print("Decoded message", Decoded)


    

   




Decision= input("Decode or Encode").lower().strip()
if Decision == "encode":
  Encode()
else :
  Decoding()















