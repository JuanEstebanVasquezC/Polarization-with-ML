def get_impedance_angles(line:any, terminal: str) -> tuple[float,float]:
    angles = (line.GetAttribute(f'm:phiu0i0:{terminal}'),
                line.GetAttribute(f'm:phiu2i2:{terminal}'))
    return angles