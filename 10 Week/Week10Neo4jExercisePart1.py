from ast import Return
from platform import release
from neo4j import GraphDatabase
from neo4j import exceptions
from sqlalchemy import values

# Neo4j Python Write

driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "neo4j1"), max_connection_lifetime=1000)


def get_association(tx, p1, p2):
    query = "MATCH(tom:Person{name:$Person1})-->(m:Movie)<--(ron:Person{name:$Person2}) RETURN m.released, m.tagline, m.title"
    results = tx.run(query, Person1=p1, Person2=p2)
    association = []
    for result in results:
        association.append({"title":result["m.title"], "released":result["m.released"], "tag":result["m.tagline"][0:19]})
    return association


def main():
    connect()
    p1  = input("Enter 1st Person: ")
    p2 = input("Enter 2nd Person: ")
    with driver.session() as session:
        try:
            values = session.write_transaction(get_association, p1, p2)
            for value in values:
                print(value["title"], "::", value["released"],"::", value["tag"])
        except exceptions.ConstraintError as e:
            print("\nError: ", e.message)
        except exceptions.ClientError as e:
            print("\nError: ", e.message)

if __name__ == "__main__":
    main()