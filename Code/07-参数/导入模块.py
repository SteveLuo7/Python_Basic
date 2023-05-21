#   在python里的一个py文件，就可以理解为模块
#   不是所有的py文件能够被导入，模块名字必须要遵守命名规则
#   如果想要让一个py文件能够被导入，模块名字必须要遵守命名规则
#   Python为了方便我们开发，提供了很多内置模块

import time # 使用import + 模块名字直接导入一个模块
from random import randint #    from 模块名 import 函数名
from math import * #    导入这个模块中的所有方法
import datetime as dt #     导入一个模块，并起一个别名
from copy import deepcopy as dp #   from 模块名 import 函数名 as 别名

print(dp(['hello', 'good', [1, 2, 3, 4], 'hhi']))


print(dt.MAXYEAR)

print(pi)

print(time.time())

print(randint(0, 2))

