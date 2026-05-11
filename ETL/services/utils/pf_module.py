import os
import sys

from config import DEBUG1, DEBUG2, r_PF, r_PY, project_name, script_name

def pf_module():
        if DEBUG1:
            try:
                os.environ["PATH"] = fr'{r_PF}' + ';' + os.environ["PATH"]
                sys.path.append(fr'{r_PY}')
                import powerfactory as pf #type: ignore
                app = pf.GetApplicationExt()

            except Exception as e:
                print("No fue posible importar PF: ", e)
                return
            
            # Activar el proyecto
            app.ActivateProject(project_name)
            print("DB activated") if app.ActivateProject(project_name)==0  else print("Cannot activate DB")

            if DEBUG2:
                app.Show() # Open PowerFactory
                print('DS Opened')

            # Obtener el script con los sets llenados por el usuario
            Scripts_folder = app.GetProjectFolder('lib') # Data object: Folder
            Script = Scripts_folder.GetContents('Scripts')[0].GetContents(script_name)[0] # Data object: Script
            
        else:
            import powerfactory as pf #type:ignore
            app = pf.GetApplication()
            Script = app.GetCurrentScript()
        return app, Script