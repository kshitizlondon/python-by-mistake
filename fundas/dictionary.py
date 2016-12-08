import inspect


def whoami():
    return inspect.stack()[1][3]


def create_new_person():
    return {
        'name': 'John',
        'age': 17,
        'friends': ['Ram', 'Sham', 'Deny', 'Kartik']
    }


def add_more_about_person(person, **kwargs):
    for more_detail in kwargs:
        person[more_detail] = kwargs[more_detail]

    return person


def add_friends(person, *args):
    if 'friends' in person:
        for new_friend in args:
            person['friends'].append(new_friend)

    return person


def remove_age_detail(person):
    if 'age' in person:
        del person['age']

    return person


def person_details():
    person = create_new_person()
    person = add_more_about_person(person, address='London', status='Single')
    person = add_friends(person, 'Marry', 'Martin')
    person = remove_age_detail(person)

    for about_person in person:
        print(about_person, person[about_person])


if __name__ == '__main__':
    person_details()
