from random import randint
from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573 )

fake = Faker('pt-BR')
#prints (signature(fake.random_number))

def make_recipes():
    return {
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_word=12),
        'preparatio_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit':'Porção',
        'preparation_step':fake.text(3000),
        'created_at':fake.date_time(),
        'author':{
            'first_name':fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category':{
            'name':fake.word()
        },
        'cover':{
            'url': 'https://loremflickr.com/%s/%s/food,cook'% rand_ratio(),
        }
    }

if __name__ == 'main':
    from pprint import pprint
    pprint(make_recipes())