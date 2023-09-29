Recopilé datos sobre el impacto ambiental de siente tipos de bolsas diferentes; BIOBOLSAS, BOLSAS PAPEL, BOLSAS PEAD, BOLSAS PEBD, BOLSAS PP, OTRAS BOLSAS PLÁSTICAS para poder comparar el impacto de cada una, y luego analizar la ley "Chao Bolsas". Pse fusionaron dos bases de tablas, una que menciona las características de la bolsa y cantidad de uso segun el año y otra que presenta el impacto ambiental de cada uno. Junto con eso se hizo un proceso de limpieza de datos y de elminaron las siguiente columnas 
•Origen materia prima
•Fin de vida
•c/utilizada 2013
•c/utilizada 2014
•c/utilizada 2015
•c/utilizada 2016
•Respiración de inorgánicos [Kg PM2.5 eq.]
•Radiación ionizante [Kg Bq Co-60 eq.]
•Eutrofización agua fresca [Kg P eq.]
•Eutrofización marina [Kg N eq.]

## Con el siguiente código: 

- columnas_a_eliminar = ['Origen materia prima', 'Fin de vida', 'c/utilizada 2013', 'c/utilizada 2014', 'c/utilizada 2015', 'c/utilizada 2016', 'Respiración de inorgánicos [Kg PM2.5 eq.]', 'Radiación ionizante [Kg Bq Co-60 eq.]', 'Eutrofización agua fresca [Kg P eq.]', 'Eutrofización marina [Kg N eq.]']
- impacto_ambiental = impacto_ambiental.drop(columnas_a_eliminar, axis=1)
- print("\nimpacto_ambiental después de eliminar las columnas:")
- print(impacto_ambiental)

1.	Busqué muchos informes en los que se hablara sobre: la contamiación de las bolsas plásticas, el uso de bolsas de papel, variables de contaminates, origen de los tipos de bolsas, entre otras variables.
2.	Seleccioné los datos que me parecieran más útiles para nuestro informe.
3.	Fusioné los datos de dos tablas en las que se proporcionaban datos por región.
4.	Eliminé la columna en la que habían datos que no eran relevantes en lo que estamos indagando.
•	¿Las bolsas plásticas son mas contaminate que las otras?
•   ¿De que manera le afecta al planeta la existencias de estas bolsas?


Los datos fueron obtenidos de: data entregada por Magdlena Ariztía