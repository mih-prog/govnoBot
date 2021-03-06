



defaultConfig = {
    "token":None,
    "version":.01,
    "prefix":"D.",
    "developersId":[755068631771119617, 482206701131399178],
    "adminsId":[755068631771119617, 482206701131399178],
    "modersId":[562314036323287063],
    "managersId":[],
    "invitationMainGildUrl":"https://discord.gg/nv4CbNyutE",
    "logChannelld":811826259213549588,
    "LogFileName":"log.txt",
    "colors":{
        "green" : 0x6DFC03,
        "red" : 0xFC0E03,
        "blue" : 0x1E90FD,
        }

}


class Utils():
    def __init__(self, config):
        self.config = config
    
    def userIsPersonal(self, userId):
        return userId in list(self.config.get("modersId")+self.config.get("adminsId")+self.config.get("developersId"))

    def checkConfigs(self, correction = False):
        chechResult = {}
        for index in defaultConfig:
            value = defaultConfig[index]
            if self.config.get(index) is None:
                if correction:
                    self.config.set(index, value)
                    chechResult[index] = True
                else:
                    chechResult[index] = None
            else:
                chechResult[index] = True
        return chechResult