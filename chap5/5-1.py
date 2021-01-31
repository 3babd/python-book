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

if ('monero' in privacy_coins) == True:
    print("Monero is a privacy coin")

if ('zcash' in privacy_coins) == True:
    print("Zcash is a privacy coin")
