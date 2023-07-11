import time
import asyncio
import subprocess
from azureClient import azureClient

class moduleInstance():

    def __init__(self):
        self.azure_client = azureClient(self)

        # getting the initial twin
        asyncio.gather(self.azure_client.connect())

if __name__ == '__main__':
    module_client = moduleInstance()
    while True:
        temps = {}
        result = subprocess.run('sensors', stdout=subprocess.PIPE)
        for line in result.stdout.decode('utf-8').split('\n'):
            if line.startswith('Package') or line.startswith('Core'):
                index = line.index(':')
                name = line[:index]
                temp = line[index + 1:].split()[0]
                tempVal = float(temp[:-2])
                temps[name] = tempVal
        asyncio.run(module_client.azure_client.send_message('output', temps))
        time.sleep(10)


