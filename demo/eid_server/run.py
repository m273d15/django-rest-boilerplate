from procbridge import procbridge
import time

if __name__ == '__main__':

    host = '0.0.0.0'
    port = 8877

    personal_data = 0

    # define request handler
    def request_handler(api: str, arg: dict) -> dict:

        if api == 'storeNPAData':
            print(arg)
            return arg
        else:
            raise Exception('unknown api')

    # start socket server
    server = procbridge.ProcBridgeServer(host, port, request_handler)
    server.start()
    print('listening...')

    while True:
        time.sleep(1)

    server.stop()
    print('bye!')