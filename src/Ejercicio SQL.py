from sqlalchemy import create_engine
import pandas as pd

# 1) Connect to the database here using the SQLAlchemy's create_engine function
import psycopg2

conect = psycopg2.connect(database= 'd1369ivrs3iieu', 
                        user = 'jebbugmwikkedw',
                        password= '8e17f676d3d78c22bdf604bed2553da3d0a6ec48df060fafadb8e514fc273a87',
                        host = 'ec2-54-80-123-146.compute-1.amazonaws.com',
                        port = 5432)

cursor = conect.cursor()
conect.commit()
#conect.close()
# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
cursor.execute("CREATE TABLE Poblacion_Uruguay(Capital VARCHAR(25) PRIMARY KEY, poblacion_total INT NOT NULL, poblacion_infantil INT NOT NULL,poblacion_mayor INT NOT NULL,ProP_Mujeres VARCHAR(4));")

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
cursor.execute("INSERT INTO Poblacion_Uruguay(Capital, poblacion_total, poblacion_infantil, poblacion_mayor,ProP_Mujeres) values('Montevideo',3500000, 1200000,1000000, '47%');")
# 4) Use pandas to print one of the tables as dataframes using read_sql function
import pandas as pd 
data = pd.read_sql('SELECT*FROM Poblacion_Uruguay;',conect)
print(data)

#conect.commit()
#conect.close()