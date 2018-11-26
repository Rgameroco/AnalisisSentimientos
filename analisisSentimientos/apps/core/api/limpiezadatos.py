import pandas as pd
import numpy  as np
import analisisSentimientos.apps.core.api
def limpiarData():
    df = pd.read_csv('analisisSentimientos/apps/core/api/datoskeiko.csv')
    df.head()