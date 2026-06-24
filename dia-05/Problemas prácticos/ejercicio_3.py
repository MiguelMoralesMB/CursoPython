def devolver_true(*args):
    contador = 0
    
    for numero in args:
        
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador +1] == 0:
            return True
        else:
            contador += 1
            
    return False

        
print(devolver_true(0,6,7,2,1,0,0,6,0,3))