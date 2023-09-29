# *Ficha técnica:* Base de datos 2
### María Paz Naudon

La infomación incluida  en  esta base de datos se caracterizan por demostrar el impacto ambiental que tiene cada una de los siete tipos de bolsas incluidos. BIOBOLSAS, BOLSAS PAPEL, BOLSAS PEAD, BOLSAS PEBD, BOLSAS PP, OTRAS BOLSAS PLÁSTICAS.   

En esta se menciona la materialidad, como se transportan y cómo se producen cada tipo bolsa,con el fin de contextualizar entre que se está comprando. Para efectos de esta base de dato se eliminó la información sobre el origen y el fin de los tipos de bolsas usando estos código:

- columnas_a_eliminar = ['Origen materia prima', 'Fin de vida', 'c/utilizada 2013', 'c/utilizada 2014', 'c/utilizada 2015', 'c/utilizada 2016', 'Respiración de inorgánicos [Kg PM2.5 eq.]', 'Radiación ionizante [Kg Bq Co-60 eq.]', 'Eutrofización agua fresca [Kg P eq.]', 'Eutrofización marina [Kg N eq.]']
- impacto_ambiental = impacto_ambiental.drop(columnas_a_eliminar, axis=1)
- print("\nimpacto_ambiental después de eliminar las columnas:")
- print(impacto_ambiental)

Cómo se puede apreciar no se tomo la decisión de eliminar solo esas dos columnas (origen de materia prime y fin de vida). Támbien preferimos considerar los datos de los últimos cinco años que teniamos, por lo tanto usando ese código aprovechamos de incluir las columnas entre en el año 2013 y 2016 que demuestran la cantidad bolsas plásticas utilizadas según su año (c/utilizada 2013, c/utilizada 2014, c/utilizada 2015, c/utilizada 2016). 

Con el fin de tener una base de datos más precisa y aterrizada quisimos agregar el impacto que tienen los tipos de bolsas según; El Potencial de Calentamiento Global, Ecotoxicidad marina, El Potencial de Acidificación, Consumo de agua, Agotamiento de ozono. Convencidas de que con esos datos nos bastaba para una comparación entre los siete tipos de bolsas ateriormente mensionado y con la inteción de no confundir al lector eliminamos de la tabla los datos de; radición ionizate, Respiración de inorgánicos, Eutrofización agua fresca y de agua marina. Usando el código anterior. 

Para la elaboración de la base de datos se fusionaron dos tablas (tipo de bolsa y coantidad de uso + impacto ambiental)

GWP100 es una medida que se usa para cuantificar y comparar el impacto climático de diferentes gases de efecto invernadero en relación con el dióxido de carbono durante un tiempo de 100 años

Se puede apreciar que las bolsas PP  (bolsas de polipropeno) tienen el valor más bajo, seguido por otras bolsas de plástico; esto indica que el gas en cuestión es menos potente como gas de efecto invernadero que el CO2 a lo largo de un siglo y en comparación a los gases que emiten el resto de las bolsas. Los gases con valores de GWP100 bajos se consideran menos preocupantes en términos de su contribución al calentamiento global a largo plazo en comparación a los que tienen valores de GWP100 más altos, que en este caso serían las bolsas PPEBD, De polietileno de baja densidad Las que tienen el valor más alto.

La ecotoxicidad se mide en relación con un estándar o una sustancia de referencia conocida. En este caso la unidad de medida utilizada en este contexto es el kilogramo de 1,4-DCB equivalente (Kg 1,4-DCBeq.).
Cuanto menor sea el valor de ecotoxicidad marina en Kg 1,4-DCBeq., menor será el potencial de la sustancia para dañar a los organismos marinos y los ecosistemas acuáticos.
En esta columna se demuestra que las bolsas de basura plástica es el tipo de bolsa emite menos ecotoxicidad marina, mientras que las BOLSAS PEBD de polietileno de baja densidad son las más contaminantes. 

La acidificación del suelo y el agua puede tener efectos negativos para  los ecosistemas y la vegetación puede acidificar cuerpos de agua y afectar negativamente a los organismos acuáticos. la bolsas plásticas son las con menos potencial de acidificación. 

El consumo de agua es una variable muy importante a la ahora de analizar el impacto ambiental de cada tipo de bolsa en esta tabla podemos ver que las BOLSAS PP de polipropileno son las que menos consumen seguidad de las bolsas plásticas y que las biobolsas y las bolsas de papel son las que mas consumen. 

es importante mencionar que el agotamiento de la capa ozono tambíen es una variable de importnacia a considerar ya que El ozono en la estratosfera es vital para proteger a la Tierra de la radiación ultravioleta (UV) dañina del sol. Según los datos las BOLSAS PP  De polipropileno son las que menos daño hacen, la bolsa de papel se pociciona en el tercer lugar de menos dañina y la bolsa plástica como la mas perjudicial. 

Con toda esta información nos damos cuenta que las bolsas plásticas no son las mas dañinas, si bien, claramente no son beneficiosas, tampoco son la peor alternativa. Esto nos hace pensar y seguir cuestionandos la medida de la Ley "Chao Bolsas"