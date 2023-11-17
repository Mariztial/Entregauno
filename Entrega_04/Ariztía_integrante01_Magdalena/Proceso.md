# Documentación del proceso para crear la visualización

*Visualización 1*: Regulación según país
1. Explicación de cómo se realizó el proceso de visualización:
- Primero, cargué la BASE DATOS 1, y usé la biblioteca pandas para leer el archivo CSV, y luego mostré las primeras filas del DataFrame resultante usando head()
- Segundo, definí las variables que serían necesarias para construir las visualizaciones. En este caso fueron tres variables, porque decidiría más adelante qué tipo de visualizsción quería, por lo que deseaba tener la mayor cantidad de opciones.
- Tercero, dejé todos los datos de las variables en mayúscula, ya que habían datos en minúscula y otras en mayúscula, y se repetían en las vizualizaciones.
- Cuarto, ordené los datos correspondientes a la variable de aplicación. Dejé que los datos que se repetían más de una vez aparecieran, y aquellos que se repitían solo una vez, los agrupé en la categoría de "Otros".
- Quinto, para la variable de Country, puse sólo los países que se repetían más de tres veces (preocupándome de que quedaran representados varios continentes y distintos niveles de desarrollo).
- Sexto, cree la variable de "repetidos", correspondiente a los países que se repitían.
- Séptimo, cree las variables para poder hacer la visualización, combinando los tipos de leyes con los países.
- Octavo, puse los datos que utilizaría para el gráfico.
- Noveno, puse los códigos para crear el gráfico.
- Décimo, definí los ejes.
- Por último, cree el código para que se guardara y poder descargarlo como imagen.

*Visualización 2*: Tipos de regulación existentes
- A continuación, hice un resumen de los tipos de leyes que existían, y vi cuáles eran las más usadas.
- Luego, utilicé un gráfico de matplotlib.
- Por último, cree el código para que se guardara y poder descargarlo como imagen.

2. Base de datos seleccionada:
La base de datos utilizada fue BASE DATOS 1.csv, proveniente de https://plasticpollutioncoalitionresources.org/, que es una organización que lucha contra la contaminación. La seleccionamos, ya que nos permite  visualizar el escenario mundial frente a la eliminación del plástico. A partir de esa base, la transformamos a csv, y le sacamos las comillas, para que el Colab lo leyera. 

Luego la limpiamos gracias a Colocamos lo siguiente: import pandas as pd datos=pd.read_csv("/content/drive/MyDrive/Colab_Notebooks/BASEDEDATOS1/db_load.csv") #print(datos) datos.drop(["Hyperlink to Ordinance"], axis=1, inplace=True) datos.drop(["Ordinance"], axis=1, inplace=True) datos df_filtered = datos[datos["Product Type"] != "Straw"] df_filtered.

Para esta entrega, le cambiamos los datos de las variables que nos interesaban a letras mayúsculas (Ya que se repetía la misma información porque algunos datos estaban en mayúscula y otros en minúscula).

3. Qué pueden responder las visualizaciones:

¿Cómo se encuentra la legislación actual del país (en cuanto a las bolsas plásticas), en relación al resto del mundo, y comparándolo con los países más desarrollados? 
Con los ejemplos y experiencias del resto del mundo, podemos ver qué es lo que han hecho otras autoridades, y de esta forma, hacernos una idea de la utilidad y aplicación de la norma aplicada en el escenario internacional.
Ambos gráficos nos permiten concluir, que en muchos lugares, el uso de bolsas plásticas está prohibido, o existen repercusiones por hacerlo.