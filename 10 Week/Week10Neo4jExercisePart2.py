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


def add_movie(tx, t, y, tag):
    query = "CREATE(m:Movie{released:$yr, tagline:$tag, title:$title})"
    tx.run(query, title=t, yr=y, tag=tag)
    

def main():
    connect()
    title  = input("Enter Movie Title: ")
    year = int(input("Enter Release Year: "))
    tagline = input("Enter the Tagline: ")
    with driver.session() as session:
        try:
            node_id = session.write_transaction(add_movie, title, year, tagline)
            print("Movie: ", title, " added to db")
        except exceptions.ConstraintError as e:
            print("\nError: ", e.message)
        except exceptions.ClientError as e:
            print("\nError: ", e.message)

if __name__ == "__main__":
    main()