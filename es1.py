def is_pari(n):
  '''ritorna vero se e pari senno ritorna falso'''
      if type(n/2)==float:
        return False
      else:
        return True
      
    numero=int(input('dammi un numero: '))

    result=is_pari(numero)

    print(result)
