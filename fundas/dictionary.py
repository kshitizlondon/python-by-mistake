import inspect


def whoami():
    return inspect.stack()[1][3]


def create_new_person():
    return {
        'name': 'John',
        'age': 17,
        'friends': set(['Ram', 'Sham', 'Deny', 'Kartik'])  # set avoids any duplicate values.
    }


def add_more_details_about_person(person, **kwargs):
    for more_detail in kwargs:
        person[more_detail] = kwargs[more_detail]

    return person


def add_friends(person, *args):
    if 'friends' in person:
        for new_friend in args:
            person['friends'].add(new_friend)

    return person


def remove_age_detail(person):
    if 'age' in person:
        del person['age']

    return person


def add_subjects(person, **kwargs):
    """ added more elements to the dictionary """
    if 'subjects' in person:
        person['subjects'].update(kwargs)
        #  if using a list instead of set.
        #  person['subjects'].update(kwargs)
    else:
        person['subjects'] = kwargs

    return person


def get_average_marks(all_subjects):
    return float(sum(all_subjects[d] for d in all_subjects)) / len(all_subjects)


def get_person_marks(person, desc=True):
        return sorted(person['subjects'].items(), key=lambda x: -x[1] if desc else x[1])

        # another way of doing this same
        # return sorted(person['subjects'].items(), key=lambda x: -x[1] * (-1 if desc else 1))


def person_details():
    person = create_new_person()
    person = add_more_details_about_person(person, address='London', status='Single')
    person = add_friends(person, 'Marry', 'Martin', 'Martin')
    person = remove_age_detail(person)
    person = add_subjects(person, English=25, Maths=75)
    person = add_subjects(person, Science=100, Marketing=50)

    for about_person in person:
        print(about_person, person[about_person])

    try:
        print(get_person_marks(person, True))
        print('Marks Average in all subjects: {}'.format(get_average_marks(person['subjects'])))
    except KeyError as e:
        print('There is no such key: {}'.format(e))


if __name__ == '__main__':
    person_details()
