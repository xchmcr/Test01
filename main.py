import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

import os

load_dotenv()

def connect_to_database():
    connection_str = f'mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_SCHEMA')}'
    connection = create_engine(connection_str)
    return connection


def read_data(connection):
    sql = """
            SELECT * FROM user_data
          """
    df = pd.read_sql_query(sql=sql, con=connection)
    return df


def main():
    while True:
        nombre = input("Inserte el nombre: ")  
        fecha = input("Inserte la fecha (DD/MM/YY): ")  
        talla = float(input("Inserte la talla (cm): "))
        peso = float(input("Inserte el peso (kg): "))

        print("% de grasa")
        biceps = float(input("Inserte % de grasa biceps: "))
        triceps = float(input("Inserte % de grasa de triceps: "))

        print("Perímetros")
        torax = float(input("Inserte medida de tórax: "))
        cintura = float(input("Inserte medida de cintura: "))
        cadera = float(input("Inserte medida de cadera: "))

        print("Anotaciones")
        anotaciones = input("¿Algo que anotar? (escriba 'no' para terminar): ") 

        
        print("\nDatos ingresados:")
        print(f"Nombre: {nombre}")
        print(f"Fecha: {fecha}")
        print(f"Talla: {talla} cm")
        print(f"Peso: {peso} kg")
        print(f"% de grasa biceps: {biceps}")
        print(f"% de grasa triceps: {triceps}")
        print(f"Medida de tórax: {torax} cm")
        print(f"Medida de cintura: {cintura} cm")
        print(f"Medida de cadera: {cadera} cm")
        print(f"Anotaciones: {anotaciones}\n")

        if anotaciones.lower() == "no":
            print("Terminado")
            break
        
if __name__ == '__main__':
    # main()
    cnxn = connect_to_database()
    df = read_data(cnxn)
    print(df)

