columnas_a_eliminar = ['Origen materia prima', 'Fin de vida', 'c/utilizada 2013', 'c/utilizada 2014', 'c/utilizada 2015', 'c/utilizada 2016', 'Respiración de inorgánicos [Kg PM2.5 eq.]', 'Radiación ionizante [Kg Bq Co-60 eq.]', 'Eutrofización agua fresca [Kg P eq.]', 'Eutrofización marina [Kg N eq.]']
- impacto_ambiental = impacto_ambiental.drop(columnas_a_eliminar, axis=1)
- print("\nimpacto_ambiental después de eliminar las columnas:")
- print(impacto_ambiental)