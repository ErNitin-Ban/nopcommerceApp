#For Logs
import logging

class LogGen():

    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                        format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p'
                        )

        Logger = logging.getLogger()
        Logger.setLevel(logging.INFO)
        return Logger