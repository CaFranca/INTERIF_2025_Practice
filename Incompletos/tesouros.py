N = int(input())
vertices = [tuple(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())

def lado(x1, y1, x2, y2, x3, y3):
    return (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

positivo = negativo = False

for i in range(N):
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i + 1) % N]
    val = lado(x1, y1, x2, y2, x, y)
    if val > 0:
        positivo = True
    elif val < 0:
        negativo = True
    if positivo and negativo:
        print("FORA")
        break
else:
    print("DENTRO")
