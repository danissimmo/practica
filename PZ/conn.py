from neo4j import GraphDatabase
import csv

# Настройки подключения к базе данных Neo4j
uri = "bolt://localhost:7687"
# username = "neo4j"
# password = "wy7RKQfoOF7KgTVajafzyN2F7OF77HshQGZqnWv7R50"

# Путь к CSV-файлу с данными
# csv_file_path = "out.csv"

# Инициализация драйвера базы данных Neo4j
driver = GraphDatabase.driver(uri, auth=("neo4j", "Fedoseev2002"))

# Открываем файл CSV и читаем данные
with open('out.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        print(row)
        source = row['Source']
        target = row[' Target']
        distance = row[' distance']

        # Создаем соединение с базой данных
        with driver.session() as session:
            # Создаем узлы для каждого уникального значения Source и Target
            session.run("MERGE (s:source {name: $source}) "
                        "MERGE (t:target {name: $target})",
                        source=source, target=target)

            # Создаем связи между узлами Source и Target с заданным значением distance
            session.run("MATCH (s:source {name: $source}) "
                        "MATCH (t:target {name: $target}) "
                        "MERGE (s)-[:TO {dist: $distance}]->(t)",
                        source=source, target=target, distance=distance)

# Закрываем соединение с базой данных Neo4j
driver.close()
