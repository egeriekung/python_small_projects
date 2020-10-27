email = input("what is your email address: ").strip()
indexEc = email.index('@')
user = email[:indexEc]
email = email.strip(user)
user = user.replace('.',' ')
user = user.title()
indexDomain = email.index('@') + 1
indexdot = email.index(".")
domain = email[indexDomain:indexdot]
print(user)
print(domain)
print('Hello {} from {}!'.format(user,domain))