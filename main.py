# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""#####################################################################
#! @ file:                   main.py
#  @ projekt:                LED_ClockRing
#  @ created on:             2026-06-01
#  @ author:                 R. Gräber
#  @ Target:                 esp32
#  @ version:                E01
#  @ history:                -
#  @ brief                  : erstellt mit Hilfe von Gemini,
#                             einem KI-Tool von OpenAI, um die
                              Entwicklung zu beschleunigen.
                              E01 board umgestellt auf YF-ESP32-23
#####################################################################"""

"""#####################################################################
# Includes
#####################################################################"""
import utilities
import logging
"""#####################################################################
# Informations
#####################################################################"""

"""#####################################################################
# Declarations
#####################################################################"""

"""#####################################################################
# Constant
#####################################################################"""

"""#####################################################################
# Global Variable
#####################################################################"""
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)
"""#####################################################################
# local Variable
#####################################################################"""

"""#####################################################################
# Constant
#####################################################################"""



"""#####################################################################
#! @fn           async def main()
#  @ brief       main task
#  @ param       none
#  @ exception   none
#  @ return      none
#####################################################################"""
async def main():
    # task1 = asyncio.create_task(web_server.start())
    # await task1

    # Automatische Aktivierung nach Bootup
    # await asyncio.sleep(20)

    """await asyncio.gather(
        # task_hid.evdev_loop(),
        # web_server.start(),
        #read_cdc_uart()
        esp_now_master_server()
        #asyncio.sleep(30)
    )"""

"""#####################################################################
#! @fn           update_peer(old_mac_bytes, new_mac_bytes)
#  @ brief       add mac to esp network
#  @ param       old_mac_bytes
#  @ param        new_mac_bytes
#  @ exception   none
#  @ return      none
#####################################################################"""

"""#####################################################################
#! @fn           mac_str_to_bytes(mac_str)
#  @ brief       Wandelt '24:0A:C4:00:00:01' in Bytes um
#  @ param       none
#  @ exception   none
#  @ return      none
#####################################################################"""


"""#####################################################################
#! @fn           int main(){
#  @ brief       start up function
#  @ param       none
#  @ exception   none
#  @ return      none
#####################################################################"""
if __name__ == "__main__":
    print(f"Starting {__name__} Application")
    logger = utilities.setup_logger()
    logger.info("Logger erfolgreich eingerichtet.")
    logger.info("Main loop")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
