from services.extraction.shc.shc_line import shc_line
from services.extraction.shc.shc_tr2 import shc_tr2

def shc_elms(elms, direction, terminal, line, Shc, data):
    fn_elms = {
        'ElmLne': shc_line,
        'ElmTr2': shc_tr2,
    }
    k=1
    elms_filttered = [e for e in elms if e.GetClassName() in ('ElmLne','ElmTr2')]
    for elm in elms_filttered:
        fn_elm = fn_elms.get(elm.GetClassName())
        if fn_elm is None:
            continue
        print(f'        {elm.loc_name}')

        fn_elm(line=line, elm=elm, Shc=Shc, direction=direction,terminal=terminal,data=data)
        print(f'        {k}/{len(elms_filttered)} ')
        k=k+1
        