import pandas as pd

from services.extraction.shc.shc_elms import shc_elms

def sc_parameters(lines:list[any], app:any):
    data = []
    k=1
    for line in lines:
        print('======================')
        print(line.loc_name, f'{k}/{len(lines)}')
        print('======================')
        k=k+1
        # terminal i & j
        for terminal in ['bus1','bus2']:
            print('**********************')
            print(terminal)
            print('**********************')

            #Shortcircuito object
            app.ResetCalculation()
            Shc = app.GetFromStudyCase('ComShc')

            # Local bus (reverse)
            print('-> Reverse elements')
            local_bus = line.GetAttribute(terminal).GetParent()
            reverse_elms = [c.obj_id for c in local_bus.GetContents() if c.obj_id != line]
            shc_elms(elms=reverse_elms, direction='reverse',line=line, Shc=Shc, data=data,terminal=terminal)
            print('✓ Reverse Ok')

            # remote bus (forward)
            print('-> Forward elements')
            remote_bus = line.GetAttribute(f'bus{int(2/int(terminal[-1]))}').GetParent()
            forward_elms = [c.obj_id for c in remote_bus.GetContents()]
            shc_elms(elms=forward_elms, direction='forward',line=line, Shc=Shc, data=data,terminal=terminal)
            print('✓ Forward ok')
            
    df = pd.DataFrame(data)
    return df
