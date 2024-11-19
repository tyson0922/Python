# def getTotalPage(m, n):
#     totalPage = (m // n) + 1
#     print(totalPage)
#
#
# getTotalPage(35, 10)

# def getTotalPage(m, n):
#     totalPage = (m // n) + 1
#
#     return totalPage
#
# print(getTotalPage(35, 10))

def getTotalPage(m, n):

    if m%n == 0:
        totalPage = m // n
    else :
        totalPage = (m // n) + 1

    return totalPage

print(getTotalPage(40, 10))
