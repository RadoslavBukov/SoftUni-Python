from pyfiglet import figlet_format
from termcolor import colored

print(
    figlet_format("Python", font="isometric1")
)

print(
    figlet_format("Rado", font="isometric1")
)

print(
    figlet_format("Rado", font="isometric1")
)

print(
    colored("Rado", 'green', attrs=['bold'])
)

print(
    colored("Rado", 'green', attrs=['underline'])
)

print(
    colored("Rado", 'green', attrs=['underline', 'bold'])
)

text = colored("Rado", 'green', attrs=['underline', 'bold'])

print(
    figlet_format(
        text,
        font="isometric1"
    )
)