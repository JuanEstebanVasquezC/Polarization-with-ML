
def get_lines(Script:any, app:any) -> list[any]:

    lines = Script.SearchObject('Lines.SetSelect').GetAll('ElmLne')

    if len(lines) == 0:
        app.PrintPlain('Atención: Ninguna Linea seleccionada')
        
    return lines