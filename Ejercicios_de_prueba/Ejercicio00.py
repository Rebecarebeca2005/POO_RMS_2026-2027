def analizar_referencias() -> None: 
    a = [1, 2] 
    b = a 
    c = [1, 2] 
 
    print("a:", a) 
    print("b:", b) 
    print("c:", c) 
 
    print("id(a) == id(b):", id(a) == id(b)) 
    print("a is b:", a is b) 
    print("a == c:", a == c) 
    print("a is c:", a is c) 
 
    a.append(3) 
    print("Después de a.append(3):") 
    print("a:", a) 
    print("b:", b) 
    print("c:", c) 
 
    x = 10 
    y = x 
    print("id(x) == id(y):", id(x) == id(y)) 
 
    x += 1 
    print("x:", x) 
    print("y:", y) 
    print("id(x) == id(y):", id(x) == id(y)) 
 
    print("type(a):", type(a)) 
    print("type(x):", type(x)) 
    print("type(analizar_referencias):", type(analizar_referencias)) 
 
 
if __name__ == "__main__": 
    analizar_referencias() 