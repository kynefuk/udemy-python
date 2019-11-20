

print('{}, {}, {}'.format('a', 'b', 'c'))

print('{0}, {1}, {2}'.format('a', 'b', 'c'))

print('{2}, {1}, {0}'.format('a', 'b', 'c'))

print('{family}, {name}'.format(family='a', name='b'))

d = {'family': 'a', 'name': 'b'}

# **d と渡すと, family='a', name='b'と展開して渡される
print('{family}, {name}'.format(**d))


print('{:<30}'.format('< is left'))

print('{:^30}'.format('^ is center'))

print('{:>30}'.format('> is right'))

print('{:*^30}'.format('center'))

print('{name:{fill}{align}{width}}'.format(name='center', fill='$', align='^', width=30))
