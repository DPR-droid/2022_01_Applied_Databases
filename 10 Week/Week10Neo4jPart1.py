from neo4j import GraphDatabase

# Neo4j Python Read

driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "neo4j1"), max_connection_lifetime=1000)


def get_students_studying_module(tx, user_module):
    query = 'MATCH (m:Module{name:$module})<-[:STUDIES]-(s) RETURN s.name'
    names = []
    results = tx.run(query, module = user_module)
    for result in results:
        names.append(result['s.name'])
    return names

def main():
    connect()
    user_module = input("Enter Module: ")
    with driver.session() as session:
        values = session.read_transaction(get_students_studying_module, user_module)
        if (len(values) == 0):
            print("No Student modules")
        else:
            print("Students Studying module")
            print("--------------------------")
            for x in values:
                print(x)

if __name__ == "__main__":
    main()