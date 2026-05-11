def get_voltages(terminal:str,line:any) -> tuple[float,float]:
    analyzed_bus = line.GetAttribute(terminal).GetParent()
    voltages = (analyzed_bus.GetAttribute('m:U0'), 
                analyzed_bus.GetAttribute('m:U2l')) # (V0, V2)
    return voltages