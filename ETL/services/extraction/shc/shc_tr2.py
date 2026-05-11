from services.extraction.utils.get_currents import get_currents
from services.extraction.utils.get_voltages import get_voltages
from services.extraction.utils.get_impedance_angles import get_impedance_angles

def shc_tr2(line:any, elm: any, Shc:any, direction:str, terminal:str,data: list[dict[str:float | str]]) -> dict[str, float]:

    Shc.iopt_mde = 3 # Completo
    Shc.iopt_allbus = 0 # User selection
    Shc.shcobj = elm.buslv.GetParent() # Fault in the element

    r_faults = list(range(0, 51, 5))
    for fault_type in ['spgf','2pgf']:
        Shc.iopt_shc = fault_type
        for r in r_faults:
            Shc.Rf = r
            
            Shc.Execute()
            row = {
                'name': line.loc_name,
                'rated_voltage': line.Unom,
                'z1': line.Z1,
                'phiz1': line.phiz1,
                'sc_element': elm.loc_name,
                'fault_type': fault_type,
                'porcentage': 'none',
                'fault_resistance': r,
                'v0': get_voltages(line=line,terminal=terminal)[0],
                'v2': get_voltages(line=line,terminal=terminal)[1],
                'i0': get_currents(line=line,terminal=terminal)[0],
                'i2': get_currents(line=line,terminal=terminal)[1],
                'phiz0': get_impedance_angles(line=line,terminal=terminal)[0],
                'phiz2': get_impedance_angles(line=line,terminal=terminal)[1],
                'dir':direction}
            print(f'            fault type: {fault_type} Rf: {r} ', end='\r', flush=True)
            data.append(row)
