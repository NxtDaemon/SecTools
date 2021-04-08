# Psuedo

1. Input either local (handle file alloc) Or using pwntools remote which allows better handling than socket module 
2. Input the Amount of Chars to init with or Automatic mode which starts with 10000
3. Start on 10000 halve the value on each iteration / take appropriate action on
4. find the overwrite sector 

# Considerations

1. Maybe use pwntools [Check ironst0ne's writeups]
2. maybe use multiprocessing in order to maximise productivity as code awaits standard processing not user input
