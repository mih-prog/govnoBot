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
    "colors":{
        "green" : 0x6DFC03,
        "red" : 0xFC0E03,
        "blue" : 0x1E90FD,
        }

}


def checkConfigs(config, correction = False):
    chechResult = {}
    for index in defaultConfig:
        value = defaultConfig[index]
        if config.get(index) is None:
            if correction:
                config.set(index, value)
                chechResult[index] = True
            else:
                chechResult[index] = None
        else:
            chechResult[index] = True
    return chechResult
    