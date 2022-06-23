import inspect


def open_browser(arg1, arg='text'):
    pass


def go_to_company_name_homepage(arg2, arg3):
    pass


def find_registration_button_on_login_page(arg4, arg5, arg6):
    pass


def print_func(*args):
    for func in args:
        arguments = inspect.signature(func)
        func_name = func.__name__
        func_list = func_name.split('_')
        func_str = " ".join(func_list)
        arguments_str = str(arguments)
        print(f'Функция: "{func_str.title()}", с аргументами:', arguments_str.strip('()'))


print_func(open_browser, go_to_company_name_homepage, find_registration_button_on_login_page)
