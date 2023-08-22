# 9.11 Zaimportowana klasa Admin. Pracę rozpocznij od ćwiczenia 9.8. W jednym module umieść klasy User, Priviliges i Admin.
from admin import Admin

admin = Admin('julia', 'rzepka', 19, 'czarny')
admin.priviliges.show_priviliges()