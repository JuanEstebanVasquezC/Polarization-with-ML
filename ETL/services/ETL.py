from services.utils.pf_module import pf_module

from services.extraction.extraction import extraction
from services.transformation.transformation import transformation
from services.load.load import load

def main():

    # app and Script adquisition
    app, Script = pf_module()

    # Extraction
    df = extraction(Script=Script, app=app)

    # Transformation
    df = transformation(df=df)

    # Load
    load(df=df, output_path='output/polarization.csv')






