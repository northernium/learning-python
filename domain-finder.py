'''Domain Finder'''
email = input('Input email addreas: ')
at = email.find('@')
space = email.find (' ',at)
domain = email[at+1 : space]
print (domain)
