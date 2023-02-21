# # Импорт пакетов для подключения OPC сервера
import time

from openopc2 import da_client
import pywintypes
from openopc2.config import OpenOpcConfig
from openopc2.da_client import OpcDaClient
from openopc2.gateway_proxy import OpenOpcGatewayProxy


def get_opc_da_client(config: OpenOpcConfig = OpenOpcConfig()) -> OpcDaClient:
    if config.OPC_MODE == "gateway":
        opc_da_client = OpenOpcGatewayProxy(config.OPC_GATEWAY_HOST, config.OPC_GATEWAY_PORT).get_opc_da_client_proxy()
        print("OpenOPC in gateway mode")
    else:
        opc_da_client = OpcDaClient(config)
        print("OpenOPC in com mode")

    opc_da_client.connect(config.OPC_SERVER, config.OPC_HOST)
    return opc_da_client


if __name__ == '__main__':
    open_opc_config = OpenOpcConfig()
    paths = "*"
    open_opc_config.OPC_SERVER = "Matrikon.OPC.Simulation"
    open_opc_config.OPC_GATEWAY_HOST = "localhost"
    open_opc_config.OPC_CLASS = "Graybox.OPC.DAWrapper"
    open_opc_config.OPC_MODE = 'com'

    opc_client = get_opc_da_client(open_opc_config)
    tags = opc_client.list(paths=paths, recursive=False, include_type=False, flat=True)
    tags = [tag for tag in tags if "@" not in tag]
    # print(tags)

    print("TAGS:")
    for n, tag in enumerate(tags):
        print(f"{n:3} {tag}")

    print("READ:")
    for n, tag in enumerate(tags):
        start = time.time()
        read = opc_client.read(tag, sync=False)
        print(f'{n:3} {time.time()-start:.3f}s {tag} {read}')
