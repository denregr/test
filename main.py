#1_в_ожидании нового года
def newYearTimeCount(m,n):
    n = 1440 - (n + m * 60)
    m, n = n // 60, n % 60
    return m, n
# Куб со спицами
def cubes():
    pass

#отгадай слово
def world():
    pass

print(newYearTimeCount(int(input()),int(input())))
