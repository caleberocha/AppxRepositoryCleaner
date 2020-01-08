from packages import get_packages, remove_package
from users import get_user, remove_user
from utils import print_list

sid = "S-1-5-21-3564065959-1144881430-2590147535-1003"

print(f'User: {sid}')
print('\n')

print('Packages')
p = get_packages(sid)
print_list(p)
print('\n')

# print('UserId')
# u = get_user_id(sid)
# print_list(u)
# print('\n')

print('Removing user')
r = remove_user(sid)
print(r)
print('\n')

print('Packages')
p = get_packages(sid)
print_list(p)
print('\n')

# print('Triggers')
# t = get_deltriggers("PackageUser", "Package")
# print_list(t)
# print('\n')

# print('Removing user packages')
# rem = remove_user_packages(sid)
# print(rem)
