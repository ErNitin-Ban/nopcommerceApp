import configparser

config = configparser.RawConfigParser()
# To read config.ini files
config.read(".\\Configurations\\config.ini")


class ReadConfig():
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

