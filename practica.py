from neo4j import GraphDatabase
import csv

# Настройки подключения к базе данных Neo4j
uri = "neo4j+s://88e2b798.databases.neo4j.io"
username = "neo4j"
password = "wy7RKQfoOF7KgTVajafzyN2F7OF77HshQGZqnWv7R50"

# Путь к CSV-файлу с данными
csv_file_path = "C:\Study\MAI\practica\log.csv"

# Инициализация драйвера базы данных Neo4j
driver = GraphDatabase.driver(uri, auth=(username, password))

# Открытие сессии
with driver.session() as session:
    # Создание индекса на уникальное поле (если требуется)
    session.run("CREATE CONSTRAINT ON (n:NodeLabel) ASSERT n.unique_field_name IS UNIQUE")

    # Открытие CSV-файла и чтение данных
    with open(csv_file_path, "r") as file:
        csv_reader = csv.DictReader(file)

        # Импорт данных в базу данных
        for row in csv_reader:
            # Используйте значения из CSV-файла для создания узлов или связей
            query = "CREATE (n:NodeLabel {property1: $value1, property2: $value2})"
            parameters = {"value1": row["column1"], "value2": row["column2"]}
            session.run(query, parameters)