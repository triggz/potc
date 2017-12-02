port_list = ['Adamsborough', 'Agropolis', 'Citti Di Passeri', 'Cotters Bay', 'Dordefoort', 'Guadalquivera',
             'Harbourtown', 'Harlenhoven', 'Houndsmouth', 'Isla de Rosas', 'Lombardo', 'Lutetia', 'Morchester',
             'New Morchester', 'Oldcastle', 'Ottenborg', 'Porto de Soto', 'Potterdam', 'Saint Adelaide','San Raphael',
             'Stallervik', 'Sur Seine', 'Trodholm', 'Ville de Biscay', 'Windward Cove']

almond = {'best': 'Guadalquivera'}
cacao = {'best':' Porto de Soto'}
cactus = {'best': 'Houndsmouth'}
camel = {'best': 'San Raphael'}
carpet = {'best': 'Lombardo'}
cinnamon = {'best': 'Stallervik'}
clove = {'best':' Lombardo'}
coffee = {'best': 'Stallervik'}
copper = {'best': 'Houndsmouth'}
coral = {'best': 'Porto de Soto'}
ginger = {'best': 'Madiz'}
glass = {'best': 'Trodholm'}
honey = {'best': 'Agropolis'}
horse = {'best': 'Stallervik'}
iron = {'best': 'Agropolis'}
ivory = {'best': 'Houndsmouth'}
marble = {'best': 'Harbourtown'}
oak = {'best': 'Citta Di Passeri'}
olive = {'best': 'Madiz'}
pearl = {'best': 'Guadalquivera'}
pepper = {'best': 'San Raphael'}
peppermint = {'best': 'Agropolis'}
perfume = {'best': 'Citta Di Passeri'}
picture = {'best': 'Morchester'}
potato = {'best': 'Houndsmouth'}
pottery = {'best': 'Los Pesadilla'}
red_pepper = {'best': 'Citta Di Passeri'}
rubber = {'best': 'Guadalquivera'}
ruby = {'best': 'Harlenhoven'}
salt = {'best': 'Lombardo'}
silk = {'best': 'Harlenhoven'}
statue = {'best': 'Los Pesadilla'}
sugar = {'best': 'Porto de Soto'}
tea = {'best': 'Porto de Soto'}
tulip = {'best': 'Stallervik'}
vanilla = {'best': 'Porto de Soto'}
velvet = {'best': 'Porto de Soto'}
wine = {'best': 'Madiz'}
wool = {'best': 'Lombardo'}
yarn = {'best': 'Stallervik'}

def run():
    print('PotC Manual Trade App by TRF Gambit')
    while True:
        user_input = input('Enter the name of the trade good or x to quit: ')
        if user_input.lower() == 'almond':
            print('The best port to sell Almond is {}'.format(almond['best']))
        elif user_input.lower() == 'cacao':
            print('The best port to sell Cacao is {}'.format(cacao['best']))
        elif user_input.lower() == 'cactus':
            print('The best port to sell Cactus is {}'.format(cactus['best']))
        elif user_input.lower() == 'camel':
            print('The best port to sell Camel is {}'.format(camel['best']))
        elif user_input.lower() == 'carpet':
            print('The best port to sell Carpet is {}'.format(carpet['best']))
        elif user_input.lower() == 'cinnamon':
            print('The best port to sell Cinnamon is {}'.format(cinnamon['best']))
        elif user_input.lower() == 'clove':
            print('The best port to sell Clove is {}'.format(clove['best']))
        elif user_input.lower() == 'coffee':
            print('The best port to sell Coffee is {}'.format(coffee['best']))
        elif user_input.lower() == 'copper':
            print('The best port to sell Copper is {}'.format(copper['best']))
        elif user_input.lower() == 'coral':
            print('The best port to sell Coral is {}'.format(coral['best']))
        elif user_input.lower() == 'ginger':
            print('The best port to sell Ginger is {}'.format(ginger['best']))
        elif user_input.lower() == 'glass':
            print('The best port to sell Glass is {}'.format(glass['best']))
        elif user_input.lower() == 'honey':
            print('The best port to sell Honey is {}'.format(honey['best']))
        elif user_input.lower() == 'horse':
            print('The best port to sell Horse is {}'.format(horse['best']))
        elif user_input.lower() == 'iron':
            print('The best port to sell Iron is {}'.format(iron['best']))
        elif user_input.lower() == 'ivory':
            print('The best port to sell Ivory is {}'.format(ivory['best']))
        elif user_input.lower() == 'marble':
            print('The best port to sell Marble is {}'.format(marble['best']))
        elif user_input.lower() == 'oak':
            print('The best port to sell Oak is {}'.format(oak['best']))
        elif user_input.lower() == 'olive':
            print('The best port to sell Olive is {}'.format(olive['best']))
        elif user_input.lower() == 'pearl':
            print('The best port to sell Pearl is {}'.format(pearl['best']))
        elif user_input.lower() == 'pepper':
            print('The best port to sell Pepper is {}'.format(pepper['best']))
        elif user_input.lower() == 'peppermint':
            print('The best port to sell Peppermint is {}'.format(peppermint['best']))
        elif user_input.lower() == 'perfume':
            print('The best port to sell Perfume is {}'.format(perfume['best']))
        elif user_input.lower() == 'picture':
            print('The best port to sell Picture is {}'.format(picture['best']))
        elif user_input.lower() == 'potato':
            print('The best port to sell Potato is {}'.format(potato['best']))
        elif user_input.lower() == 'pottery':
            print('The best port to sell Pottery is {}'.format(pottery['best']))
        elif user_input.lower() == 'red pepper':
            print('The best port to sell Red Pepper is {}'.format(red_pepper['best']))
        elif user_input.lower() == 'rubber':
            print('The best port to sell Rubber is {}'.format(rubber['best']))
        elif user_input.lower() == 'ruby':
            print('The best port to sell Ruby is {}'.format(ruby['best']))
        elif user_input.lower() == 'salt':
            print('The best port to sell Salt is {}'.format(salt['best']))
        elif user_input.lower() == 'silk':
            print('The best port to sell Silk is {}'.format(silk['best']))
        elif user_input.lower() == 'statue':
            print('The best port to sell Statue is {}'.format(statue['best']))
        elif user_input.lower() == 'sugar':
            print('The best port to sell Sugar is {}'.format(sugar['best']))
        elif user_input.lower() == 'tea':
            print('The best port to sell Tea is {}'.format(tea['best']))
        elif user_input.lower() == 'tulip':
            print('The best port to sell Tulip is {}'.format(tulip['best']))
        elif user_input.lower() == 'vanilla':
            print('The best port to sell Vanilla is {}'.format(vanilla['best']))
        elif user_input.lower() == 'velvet':
            print('The best port to sell Velvet is {}'.format(velvet['best']))
        elif user_input.lower() == 'wine':
            print('The best port to sell Wine is {}'.format(wine['best']))
        elif user_input.lower() == 'wool':
            print('The best port to sell Wool is {}'.format(wool['best']))
        elif user_input.lower() == 'yarn':
            print('The best port to sell Yarn is {}'.format(yarn['best']))
        elif user_input.lower() == 'x':
            break
        else:
            print('Could not find the trade good: {}'.format(user_input))










if __name__ == '__main__':
    run()


