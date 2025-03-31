def change():
    expense = 23.75
    money = 100
    turned = money - expense
    turned_int = int(turned)
    turned_d = int((turned-turned_int) * 100)

    print(f'Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n\nVuelto\n\nPesos:\n{turned_int}\nCentavos:\n{turned_d}')
    

change()