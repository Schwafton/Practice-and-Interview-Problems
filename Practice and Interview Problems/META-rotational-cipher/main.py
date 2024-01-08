# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input, rotation_factor):
  # Write your code here
  cipher = ""
  if rotation_factor >= 10:
    num_factor = rotation_factor%10
  else:
    num_factor = rotation_factor

  if rotation_factor >= 26:
    alpha_factor = rotation_factor%26
  else:
    alpha_factor = rotation_factor

  for c in input:
    if c.isalnum():
      if c.isalpha():
        if c.islower():
          if (ord(c) + alpha_factor) > 122:
            cipher += chr(ord(c) + alpha_factor - 26)
          else:
            cipher += chr(ord(c) + alpha_factor)
        else:
          if (ord(c) + alpha_factor) > 90:
            cipher += chr(ord(c) + alpha_factor - 26)
          else:
            cipher += chr(ord(c) + alpha_factor)
      if c.isnumeric():
        if (ord(c) + num_factor) > 57:
          cipher += chr(ord(c) + num_factor - 10)
        else:
          cipher += chr(ord(c) + num_factor)
    else:
      cipher += c
  print(cipher)
  return cipher

input = "Zzz-999"
rotation_factor = 1
rotationalCipher(input, rotation_factor)