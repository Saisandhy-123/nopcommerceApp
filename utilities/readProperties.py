import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Readconfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url


    @staticmethod
    def getUseremail():
        Username=config.get('common info','Username')
        return Username

    @staticmethod
    def getPassword():
        Password=config.get('common info','Password')
        return Password