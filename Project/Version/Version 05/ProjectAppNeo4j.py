from distutils.log import error
from pickle import TRUE
from sqlalchemy import false, true
from neo4j import GraphDatabase
from neo4j import exceptions
import logging


# Neo4j connection details
driver = None

def connect():
    global driver
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "neo4j1"), max_connection_lifetime=1000)
    # driver = GraphDatabase.driver(uri, auth=("neo4j", "neo4j"), max_connection_lifetime=1000)


# Neo4j Python Read to 
# Get Manager
def get_manager(tx, user_module):
    query = 'MATCH (n:Department{did:$module}) <-[:MANAGES]-(p:Employee) Return p.eid'
    names = []
    results = tx.run(query, module = user_module)
    for result in results:
        names.append(result['p.eid'])
    return names


def get_Neo_Results(DEPTID):
    connect()
    with driver.session() as session:
        try:
            values = session.read_transaction(get_manager, DEPTID)
            if (len(values) == 0):
                # print("No one manages " + DEPTID)
                return true
            else:
                for x in values:
                    return x
        except TypeError as e:
            print(e)
            pass
    driver.close()



# Add Link 

def add_link(tx, eid, deptname):
    query1 = 'MERGE(e:Employee{eid:$eid});'
    tx.run(query1, eid=eid)

    query2 = 'MERGE(d:Department{did:$deptname});'
    tx.run(query2, deptname=deptname)

    query3 = 'MATCH(e{eid:$eid}) MATCH(d1{did:$deptname}) MERGE(e)-[:MANAGES]->(d1);'
    tx.run(query3, eid=eid, deptname=deptname)
  
    


def add_manages(EID, DEPTID):
    connect()
    with driver.session() as session:
        try:
            node_id = session.write_transaction(add_link, EID, DEPTID)
        except exceptions.ConstraintError as e:
            logging.warning(str(e))
            print("\nError: ", e.message)
        except exceptions.ClientError as e:
            logging.warning(str(e))
            print("\nError: ", e.message)
        except exceptions.DatabaseError as e:
            logging.warning(str(e))
            print("\nError: ", e.message)
        except NameError as e:
            logging.warning(str(e))
        except Exception as e:
            logging.warning(str(e))
    driver.close()
    
            
                