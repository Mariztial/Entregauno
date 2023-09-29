# Ficha técnica BASE 1

**Características de los datos**

Los datos son de tipo cualitativo. 

**Alcance metodológico**

La base de datos permite saber en qué países (y específicamente sobre qué sectores), rigen leyes que prohíben o no, el uso de bolsas plásticas. Esto con el objetivo de plantear un escenario internacional sobre el avance de la eliminación de plástico.

**Variables incorporadas**

Las variables incorporadas corresponden a 
- país (se nmuestran distintos países del mundo)
- alcance: nacional/estado/local
- jurisdicción: sobre qué territorios en específico rige la ley (se muestran territorios a lo largo de todo el mundo).
- Tipo de ley: si es que es una ley obligatoria/libre/otro
- Tipo de producto: bolsa (dejamos solamente esa variable, ya que es la que nos interesa para nuestra investigación)
- Aplicación: para qué se utiliza el producto (bolsa), que puede ser para retail/se desconoce/manufactura/distribución/importación.

**Observaciones**

En la mayoría de los países la ley es obligatoria y uno de los usos más preponderantes que se les da a las bolsas, es en el retail.

**Para la limpieza**

Se utilizó: (explicados en el archivo readme.md)
import pandas as pd
datos=pd.read_csv("/content/drive/MyDrive/Colab_Notebooks/BASEDEDATOS1/db_load.csv")
#print(datos)
datos.drop(["Hyperlink to Ordinance"], axis=1, inplace=True)
datos.drop(["Ordinance"], axis=1, inplace=True)
datos
df_filtered = datos[datos["Product Type"] != "Straw"]
df_filtered






