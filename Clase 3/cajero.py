menu=input()

while menu !='4':
    print('-----------------------\n Bienvenidosal cajero \n-----------------------')

    print('1 Depositos ')

    print('2 Extraer ')

    print('3 Transferencias ')
    
    print('4 Salir \n')
    
    
    menu = input('Elige una Opcion : ')

    if menu =='1':
        input('ingrese monto a depositar:')
    elif menu =='2':    
        input('ingrese monto a extraer:')
        
    elif menu =='3':    
        input('ingrese monto a transferir:')
  
    elif menu =='4':
        input('Gracias por utlizar el cajero')
    break