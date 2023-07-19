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


def generate_id(source):
    sourceID = source.replace(' ', '_')
    sourceID = sourceID.replace('-', '_')
    sourceID = sourceID.replace('\'', '_')
    print(sourceID)
    if sourceID[0].isdigit():
        sourceID = '_' + sourceID
    return sourceID


# Открываем файл CSV и читаем данные
with open('out.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    nodes = set()

    for row in reader:
        source = row['Target']
        target = row['Source']
        distance = row['distance']

        # Создаем соединение с базой данных
        with driver.session() as session:
            if source not in nodes:
                sourceID = generate_id(source)

                mergeStr = "MERGE (" + sourceID + ":s {name: $source})"

                session.run(mergeStr, source=source)
                nodes.add(source)
                print(source)

            if target not in nodes:
                targetID = generate_id(target)

                mergeStr = "MERGE (" + targetID + ":s {name: $target})"

                session.run(mergeStr, target=target)
                nodes.add(target)
                print(target)

            # Создаем связи между узлами Source и Target с заданным значением distance
            session.run("MATCH (s {name: $source}) "
                        "MATCH (t {name: $target}) "
                        "MERGE (s)-[:TO {dist: $distance}]->(t)",
                        source=source, target=target, distance=distance)

# Закрываем соединение с базой данных Neo4j
driver.close()
