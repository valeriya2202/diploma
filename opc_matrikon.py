# # Импорт пакетов для подключения OPC сервера
from openopc2 import da_client
import pywintypes


if __name__ == '__main__':
    # #ПОДКЛЮЧЕНИЕ к OPC серверу
    # #Создать клиентский объект OPC DA
    pywintypes.datetime = pywintypes.TimeType
    opc = da_client.OpcDaClient()

    # #Поиск серверов OPC DA
    servers = opc.servers(opc_host='localhost')
    print(servers)

    # #Подключение к OPC DA-серверу
    opc.connect('Matrikon.OPC.Simulation.1')
    aliases = opc.list()
    print(aliases)

    # #Используйте list() для поиска доступных элементов
    groups = opc.list('Simulation Items.Random')
    print(groups)

    # Pass on tag group to read and write method
    opc.read('Random.Int4')

    opc.close()
