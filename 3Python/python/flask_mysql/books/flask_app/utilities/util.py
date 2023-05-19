DEBUG = True

@staticmethod
def callout(data, offset=3, bannerCharacter='-', force=False):
    if( force == True or DEBUG == True):
        print('\n'*offset + bannerCharacter*15)
        print(data)
        print(bannerCharacter*15 + '\n'*offset)

