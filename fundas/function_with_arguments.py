import inspect


def whoami():
    return inspect.stack()[1][3]


def function_with_normal_arguments(some_arg1, some_arg2, *args):
    print('Results from {}:'.format(whoami()))
    return some_arg1, some_arg2, args


def function_with_normal_and_unknown_arguments(some_arg1, some_arg2, *args):
    print('Results from {}:'.format(whoami()))
    return some_arg1, some_arg2, args


def function_with_normal_and_unknown_arguments_plus_key_value_args(
        some_arg1, some_arg2, *args, **kwargs):
    print('Results from {}:'.format(whoami()))
    return some_arg1, some_arg2, args, kwargs


def function_together(some_arg1, some_arg2, *args, **kwargs):
    print('Results from {}:'.format(whoami()))

    print('printing normal args:')
    print(some_arg1, some_arg2)

    print('printing normal *args:')
    for argument in args:
        print(argument)

    print('printing normal **kwargs:')
    for key in kwargs:
        print(key, kwargs[key])


if __name__ == '__main__':

    print(function_with_normal_arguments('apple', 'mango'))

    print(function_with_normal_arguments(
        'apple', 'mango',  # passing *args, will be printed in tuple
        'apple_args', 'mango_args')
    )

    print(function_with_normal_and_unknown_arguments_plus_key_value_args(
        'apple', 'mango',  # passing normal arguments
        'apple_args','mango_args',  # passing *args, will be printed in tuple
        first_name="John", last_name="Doe")  # passing *kwargs, will be printed in dict
    )

    function_together(
        'apple', 'mango',  # passing normal arguments
        'apple_args', 'mango_args',  # passing *args
        first_name="John", last_name="Doe"  # passing *kwargs
    )
