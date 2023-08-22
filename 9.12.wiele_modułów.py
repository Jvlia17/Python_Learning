# 9.12 Wiele modułów. Klasę User umieść w jednym module, natomiast Priviliges i Admin w oddzielnym.
from admin import Admin

admin = Admin('julia', 'rzepka', 19, 'czarny')
admin.priviliges.show_priviliges()
