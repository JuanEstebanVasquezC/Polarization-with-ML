from services.extraction.utils.get_lines import get_lines
from services.extraction.parameters.shc_parameters import sc_parameters

import pandas as pd

def extraction(Script: any, app: any):

    # Shenanigans for performance <off>
    app.ClearOutputWindow()
    app.EchoOff()
    app.SetUserBreakEnabled(0)

    # Get the lines form the set select
    lines = get_lines(Script=Script, app=app)

    # Get df with shorcircuit parameters
    df = sc_parameters(lines=lines,app=app)

    # Shenanigans for performance <on>
    app.SetUserBreakEnabled(1)
    app.EchoOn()
    
    return df