N = 7

a = [[(-N+1+i+j)*(i!=N-1-j) for i in range(N)] for j in range(N)]

for r in a:
    formatted_row = []
    for element in r:
        if element >= 0:
            formatted_row.append(f" {element}")#якщо елемент >=0 то дадтково друкується пробіл перед числом
        else:
            formatted_row.append(f"{element}")#якщо елемент менше 0, то просто виводимо число
    print(" ".join(formatted_row))
