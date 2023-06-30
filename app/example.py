#Si no queremos que al importar se ejecute todo un módulo, solo lo invocado, para eso tenemos que modularizarlo, una forma es embeber en una función, para ejecutarlo explícitamente.

import main

print('example =>', main.data_countries)
main.run()

#Si  quiero controlar desde example.py la ejecución de main o elementos de este módulo, pero a la vez la dualidad de ejecutar main.py como script desde la terminal, usamos el entry point:

'''if __name__ == '__main__':
  run()'''

#Este if o entry point le dice al main.py que si se ejecuta como script desde la terminal, este se ejecuta con normalidad, pero si se ejecuta desde otro archivo como módulo, este no se ejecutará.