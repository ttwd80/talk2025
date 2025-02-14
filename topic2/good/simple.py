def water(celcius):
    if celcius < 0:
        return "ice"
    elif celcius > 100:
        return "steam"
    else:
        return "water"
