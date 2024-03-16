# Implementación de un Buscador Inteligente de Cursos

## online_courses.ipynb

Mediante el uso de *pandas* y *numpy*, limpiamos el dataset *Online_Courses.csv* y generamos un dataset limpio guardado como *courses_data.csv*.

Con los datos limpios, generamos un conjunto sintético de usuarios como conjuntos de skills que pueden tener y un conjunto sintético de recomendaciones para esos usuarios, llamados *users.npy* y *recomendations.npy*.

## model.ipynb

Con los datos sintéticos creados con el notebook anterior, generamos un modelo de Tensorflow con una red neuronal feed-forward que intente predecir las recomendaciones que les puedan servir a los usuarios.

El rendimiento obtenido para la red neuronal es de aproximadamente de un 13%. Que sabiendo que existen aproximadamente 8000 cursos, que acierte un 13% de las veces es relativamente aceptable.

## user_recomendation_parses.ipynb

En este fichero, se crearon varias funciones para parsear los usuarios,representados como listas de unos y ceros, donde cada 1 representa una skill que tienen y 0 que no, en recomendaciones de cursos, que están representadas como un conjunto de filas en una tabla de *pandas*.