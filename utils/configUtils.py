defaultConfig = {
    "token":None,
    "version":.01,
    "prefix":"D.",
    "adminsId":[755068631771119617, 482206701131399178],
    "modersId":[562314036323287063],
    "managersId":[],

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
    