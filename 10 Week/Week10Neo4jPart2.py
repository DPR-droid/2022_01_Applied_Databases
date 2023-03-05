from neo4j import GraphDatabase
from neo4j import exceptions

# Neo4j Python Write

driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "neo4j1"), max_connection_lifetime=1000)


def add_student(tx, sid, name):
    query = 'CREATE(s:Student{sid:$sid, name:$x})'
    tx.run(query, sid=sid, x=name)


def main():
    connect()
    sid  = input("Enter sid: ")
    name = input("Enter name: ")
    with driver.session() as session:
        try:
            node_id = session.write_transaction(add_student, sid, name)
            print("Student: ", sid, ",", name, " added to DB")
        except exceptions.ConstraintError as e:
            print("\nError: ", e.message)
        except exceptions.ClientError as e:
            print("\nError: ", e.message)

if __name__ == "__main__":
    main()