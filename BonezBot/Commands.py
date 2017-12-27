import pkgutil
import inspect


def call_module_function(dirname, function, bot):
    for loader, name, is_pkg in pkgutil.walk_packages([dirname]):
        module = loader.find_module(name).load_module(name)

        for name, value in inspect.getmembers(module):
            if name.startswith('__'):
                continue

            if inspect.isfunction(value) and name == function:
                # print(name, "|", value)
                value(bot)


def load_all_modules(dirname, bot):
    call_module_function(dirname, "add_to_bot", bot)


def remove_all_modules(dirname, bot):
    call_module_function(dirname, "remove_from_bot", bot)


def update_all_modules(dirname, bot):
    remove_all_modules(dirname, bot)
    load_all_modules(dirname, bot)