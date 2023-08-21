from time import sleep
import psutil as ps
from os import system

# Iniciando o script
print('Developed by ~ Bruno Gallotte')
print('Inicializando script...')
sleep(1)

# Função para verificar os processo que estão rodando
def analisaProcessos():
    print('Analisando processos [wait]')
    sleep(0.4)
    print('==='*10)

    def contarProcessos():
        count = 0
        for process in ps.process_iter():
            count += 1
        return count
    
    total_processos = contarProcessos()
    print(f'Existem {total_processos} processos rodando!')

    sleep(1)
    print('==='*10)
    sleep(0.2)
    
    FivemProcessID = None
    FivemProcessName = None
    
    for proc in ps.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == 'FiveM.exe':
            FivemProcessID = proc.info['pid']
            FivemProcessName = proc.info['name']
            break  # Saia do loop assim que encontrar o processo

    if FivemProcessID is not None:
        print(f'Process ID: {FivemProcessID} Name: {FivemProcessName}')
    else:
        print('Processo inexistente, tente novamente!')

analisaProcessos()

