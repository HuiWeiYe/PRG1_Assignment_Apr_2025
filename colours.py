def clr(colour,text):
    reset = "\033[0m"
    colour_list = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "purple": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m"
    }
    colour = colour.lower()
    if colour in colour_list:
        colour_code = colour_list[colour]
    else:
        colour_code = colour_list['white']
    
    return colour_code + text + reset