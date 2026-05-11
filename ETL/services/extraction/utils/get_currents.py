def get_currents(line: any, terminal: str) -> tuple[float,float]:
    currents = (line.GetAttribute(f'm:I0:{terminal}'),
                line.GetAttribute(f'm:I2:{terminal}'))
    return currents