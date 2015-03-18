#!/usr/bin/python
 
words = ['SEM',
'eat your own dog food']

plop = {}

for word in words:
  length = len(word)
  yooniecode = 'uniE601'
  string = ''
  glue = ''
  firstletter = ''

  if length < 6:
    yooniecode = 'uniE602'
  if length > 11:
    yooniecode = 'uniE600'
  for i, letter in enumerate(word):
    if i == 0:
      firstletter = letter
    else:
      # TODO: 5 ---> five etc.
      if letter is ' ':
        letter = 'space'
      string += glue + str(letter)
      glue = ','

  line = '  <Ligature components="' + string + '" glyph="' + yooniecode + '"/>' + "\n"

  if firstletter in plop:
    plop[firstletter] += line
  else:
    plop[ firstletter ] = line

for ltr in plop:
  print '<LigatureSet glyph="' + ltr + '">' + "\n"
  print plop[ltr]
  print '</LigatureSet>' + "\n"
