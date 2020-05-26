#kamen, škare, papir, gušter, spock

IgračA = input('Unesi kamen, škare, papir, gušter, spock: ')
IgračB = input('Unesi kamen, škare, papir, gušter, spock: ')

if IgračA == 'kamen' and IgračB == 'papir':
    print('Pobjeda Igrača B')
elif IgračA == 'kamen' and IgračB == 'škare':
    print('Pobjeda Igrača A')
elif IgračA == 'kamen' and IgračB == 'kamen':
    print('Neriješeno')
elif IgračA == 'kamen' and IgračB == 'gušter':
    print('Pobjeda Igrača A')
elif IgračA == 'kamen' and IgračB == 'spock':
    print('Pobjeda Igrača A')

if IgračA == 'papir' and IgračB == 'kamen':
    print('Pobjeda Igrača A')
elif IgračA == 'papir' and IgračB == 'škare':
    print('Pobjeda Igrača A')
elif IgračA == 'papir' and IgračB == 'papir':
    print('Neriješeno')
elif IgračA == 'papir' and IgračB == 'gušter':
    print('Pobjeda Igrača B')
elif IgračA == 'papir' and IgračB == 'spock':
    print('Pobjeda Igrača A')

if IgračA == 'škare' and IgračB == 'papir':
    print('Pobjeda Igrača A')
elif IgračA == 'škare' and IgračB == 'kamen':
    print('Pobjeda Igrača B')
elif IgračA == 'škare' and IgračB == 'škare':
    print('Neriješeno')
elif IgračA == 'škare' and IgračB == 'gušter':
    print('Pobjeda Igrača A')
elif IgračA == 'škare' and IgračB == 'spock':
    print('Pobjeda Igrača B')

if IgračA == 'gušter' and IgračB == 'papir':
    print('Pobjeda Igrača A')
elif IgračA == 'gušter' and IgračB == 'škare':
    print('Pobjeda Igrača B')
elif IgračA == 'gušter' and IgračB == 'gušter':
    print('Neriješeno')
elif IgračA == 'gušter' and IgračB == 'kamen':
    print('Pobjeda Igrača B')
elif IgračA == 'gušter' and IgračB == 'spock':
    print('Pobjeda Igrača A')

if IgračA == 'spock' and IgračB == 'papir':
    print('Pobjeda Igrača B')
elif IgračA == 'spock' and IgračB == 'škare':
    print('Pobjeda Igrača B')
elif IgračA == 'spock' and IgračB == 'spock':
    print('Neriješeno')
elif IgračA == 'spock' and IgračB == 'gušter':
    print('Pobjeda Igrača B')
elif IgračA == 'spock' and IgračB == 'kamen':
    print('Pobjeda Igrača A')   

ponovo = input("Ponovite igru? (Da/Ne)")