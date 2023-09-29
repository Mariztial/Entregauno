# BASE DATOS 1

**Elección de la base de datos**

Elegimos esta base de datos, ya que no es útil para visualizar el escenario mundial, frente a la eliminación del plástico. Así, con la aprobación de diversos países, tanto desarrollados, como sub desarrollados, podemos hacernos una idea de qué tan útil es implementar dicha medida para cuidar el medio ambiente, y permite responder a preguntas centrales de nuestra investigación, como por ejemplo, si es que ¿es realmente útil la ley 21.100, que elimina las bolsas plásticas? o ¿Vale el costo de eliminar las bolsas de plástico de los comercios? o ¿Cómo se encuentra la legislación actual del país (en cuanto a las bolsas plásticas), en relación al resto del mundo, y comparándolo con los países más desarrollados? Con los ejemplos y experiencias del resto del mundo, podemos ver qué es lo que han hecho otras autoridades, y de esta forma, hacernos una idea de la utilidad y aplicación de la norma aplicada en el escenario internacional.

**Origen base de datos**

Para esta base, utilizamos una base de daos proveniente de https://plasticpollutioncoalitionresources.org/, que es una organización que lucha contra la contaminación. A partir de esa base, la transformamos a csv, y hubonque sacarle las comillas, para que el Colab lo leyera.

**Limpieza de base de datos**

Colocamos lo siguiente:
import pandas as pd
datos=pd.read_csv("/content/drive/MyDrive/Colab_Notebooks/BASEDEDATOS1/db_load.csv")
#print(datos)
datos.drop(["Hyperlink to Ordinance"], axis=1, inplace=True)
datos.drop(["Ordinance"], axis=1, inplace=True)
datos
df_filtered = datos[datos["Product Type"] != "Straw"]
df_filtered

**Resultados**

Lo que logramos con lo anterior, fue eliminar la columna de "Hyperlink to Ordinance", ya que no nos interesaba para esta investigación, nos basta el escenario general de lo que sucede en cada país/estado/ciudad. Luego eliminamos también la columna de "Ordinance", ya que tampoco era de nuestro interés. Por último, hicimos que en la columna de "Product Type", quedaran solo los productos correspondientes a "bag", ya que es lo que va de acuerdo con nuestra investigación. 

Finalmente, guardamos la base de datos, como archivo CSV, y una vez en la carpeta de escritorio, le cambiamos el nombre a "BASE DATOS 1".