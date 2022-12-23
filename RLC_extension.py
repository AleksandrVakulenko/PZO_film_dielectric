import pyvisa as visa
import time


class LCRmeter:
    __resource_manager = visa.ResourceManager()
    __device: __resource_manager.open_resource

    def __init__(self):
        self.__device = self.__connect()
        self.set_voltage(0.01)
        self.set_frequency(1000)

    def __del__(self):
        self.__disconnect()

    def set_voltage(self, volt=0.01):
        # TODO: add return of real values
        self.__device.write(':VOLTage:LEVel ' + str(volt))
        time.sleep(0.2)

    def set_frequency(self, freq=1000):
        # TODO: add return of real values
        self.__device.write(':FREQuency:CW ' + str(freq))
        time.sleep(0.2)

    def get_c_d_r_x(self) -> list[float]:
        z = self.__device.query(':FETCh:IMPedance:FORmatted?')
        values_arr_c_d = z.split(',', 2)
        z = self.__device.query(':FETCh:IMPedance:CORrected?')
        values_arr_r_x = z.split(',', 2)
        c_d_r_x = [float(values_arr_c_d[0]),
                   float(values_arr_c_d[1]),
                   float(values_arr_r_x[0]),
                   float(values_arr_r_x[1])]
        return c_d_r_x

    # -----------------------------------PRIVATE PART---------------------------------------
    def __find_rlc(self):
        rm_list = self.__resource_manager
        for adr in rm_list:
            # print(name)
            try:
                instrument = self.__resource_manager.open_resource(adr)
                idn = instrument.query('*IDN?')
                instrument.close()
                if idn == "Keysight Technologies,E4980AL,MY54305367,B.07.01\n":
                    return adr
            except:
                pass
        return 0

    def __connect(self):
        rlc_adr = self.__find_rlc()
        if rlc_adr != 0:
            device = self.__resource_manager.open_resource(rlc_adr)
            idn = device.query('*IDN?')
            print('RLC device connected:\n' + idn + '\n')
            return device
        else:
            print('\nno RLC device found\n')
            exit(-1)


    def __disconnect(self):
        self.__device.close()
        print('RLC device disconnected')








