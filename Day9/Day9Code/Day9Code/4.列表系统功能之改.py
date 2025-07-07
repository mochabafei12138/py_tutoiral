# 1.list.reverse()翻转/反转/逆序列表中元素   ******
list1 = [34,6,87,9,34,6,8,12]
print(list1)
list1.reverse()
print(list1)

# 2.list.sort(key=None,reverse=False)对原列表进行排序       ******
# 注意：如果要对列表中的元素进行排序，一定要先保证列表中的元素是可以比较大小的
# a.升序
list1 = [34,6,87,9,34,6,8,12]
print(list1)
list1.sort()
print(list1)

# b.降序
list1 = [34,6,87,9,34,6,8,12]
print(list1)
list1.sort(reverse=True)
print(list1)



