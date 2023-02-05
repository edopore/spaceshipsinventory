# Reto Técnico para ingreso a Training Leagues
## Aplicación de inventario para naves espaciales

Este repositorio es una pequeña aplicación de inventario para naves espaciales usando python para lógica y SQLite para persistencia y almacenamiento de datos.

Esta es una aplicación de consola que permite navegación entre menús para realizar creación de naves espaciales de tres tipos (Lanzadera, Naves no tripuladas y Naves tripuladas) en las cuales se puede almacenar el nombre de la nave espacial, el año en el que inicia operación, el tipo de nave espacial (definido anteriormente), el tipo de combustible que usa la nave espacial, el pais de fabricación o uso y la cantidad de tripulantes que puede albergar en el caso que sirva como medio de transporte.

Para su funcionamiento se requiere de lo siguiente:
- Python 3.10.5
- Archivo database.db (que se encuentra en este repositorio)

Este repositorio está compuesto de un archivo main.py encargado de la ejecución del programa y de un archivo starship.py donde se define la clase StarShip de la cual se obtiene la nave espacial, quien a su vez esta clase es heredada para las subclases Launcher, crew y noncrew que sirven para definir las naves espaciales tipo Lanzadora, Nave tripulada y Nave no tripulada respectivamente

Este repositorio es de la autoría de Eduardo José Maya Rodriguez
