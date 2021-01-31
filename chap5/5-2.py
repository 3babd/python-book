girl_age = 20

print(girl_age > 18)

if (girl_age > 18):
    print("you can come to the party")

boy_age = 19

print(girl_age > boy_age)

if(girl_age > boy_age):
    print("The girl is older than the boy")

boys_names = ['Fred', 'Johnson', 'Frank', 'Satoshi']

print(boys_names[0] == 'Fred')
print(boys_names[0].lower() == 'fred')

print(5 < 7)
print(8 >= 8)
print(3 > 1)
print(1 < 10)
print(5 <= 2)

crypto = ['bitcoin', 'monero', 'ethereum', 'zcash']

print(crypto[0] == 'bitcoin')
print(crypto[1] == 'monero')
print(crypto[2] == 'ethereum')
print(crypto[3] == 'zcash')


defi = ['yfi', 'aave', 'alpha', 'link']

print(defi[0] == 'aave')
print(defi[1] == 'alpha')
print(defi[2] == 'link')
print(defi[3] == 'yfi')

privacy_coins = ['monero', 'zcash']

if ('monero' in privacy_coins) and ('monero' in defi) == True:
    print("Monero is privacy defi")
else:
    print("Sorry, monero is not privacy defi")

if ('monero' in crypto) and ('monero' in privacy_coins) == True:
    print("Monero is a privacy crypto")

if ('bitcoin' in crypto) or ('bitcoin' in defi) == True:
    print("bitcoin is either a cryptocurrency or a defi token")

if ('zcash' in crypto) == True:
    print("Zcash is a cryptocurrency")

if ('zcash' not in defi) == True:
    print("Zcash is not a defi token")
