# # Бесконечные генераторы
# # yield
#
# def gen():
#     yield 1
#     yield 5
#     yield 'hello!'
# for a in gen():
#     print(a)
#
# def gen1(get_second):
#     yield 1
#     if get_second:
#         yield 5
#     yield 'hello!'
# for a in gen1(True):
# #     print(a)
#
# def gen2():
#     for a in range(10):
#         yield a
#
# g = gen2()
# print(next(g))
#
# for a in gen2():
#     print(a)
#

