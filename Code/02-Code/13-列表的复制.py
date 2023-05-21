

a = 12
b = a

print('修改前，a=%x,b%x' % (id(a),id(b)))
a = 10
print(b)
print(a)
print('修改后，a=%x,b%x' % (id(a),id(b)))




nums1 = [100, 200, 300]
nums2 = nums1
print('修改前, nums1=%x,nums2=%x' % (id(nums1),id(nums2)))
nums1[0] = 1
print(nums2)
print('修改后, nums1=%x,nums2=%x' % (id(nums1),id(nums2)))

#   不可变的数据类型： 数字，字符串，元组 （内存地址会发生变化）
#   可变的数据类型： 列表， 字典， 集合  （内存地址不会发生变化）

x = [100, 200, 300]

y = x   # x 和 y 指向了同一个内存空间

z = x.copy() # copy 方法，可以复制一个列表

x[0] = 1

print(y) # [1, 200, 300]

print(z)

print('0x%X,0x%X,0x%X' % (id(x),id(y),id(z)))
