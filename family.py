
class Family:
    def __init__(self, database):
        self.db = database

    def get_children(self, query_filter: dict) -> [list, None]:
        query = f"MATCH(p1:Pessoa)-[f:FILHO_DE]->(p2:Pessoa)" \
                f"WHERE p2.{query_filter['key']} = '{query_filter['value']}'" \
                f" RETURN p1 AS pessoa"
        results = self.db.execute_query(query)
        if results:
            return results
        else:
            return None

    def get_spouse(self, query_filter: dict) -> [list, None]:
        query = f"MATCH(p1:Pessoa)-[f:CASADO_COM]->(p2:Pessoa)" \
                f"WHERE p2.{query_filter['key']} = '{query_filter['value']}'" \
                f" RETURN p1 AS pessoa"
        results = self.db.execute_query(query)
        if results:
            return results
        else:
            return None

    def get_owner(self, query_filter: dict) -> [list, None]:
        query = f"MATCH(p1:Pessoa)-[f:DONO_DE]->(p:Pet)" \
                f"WHERE p.{query_filter['key']} = '{query_filter['value']}'" \
                f" RETURN p1 AS pessoa"
        results = self.db.execute_query(query)
        if results:
            return results
        else:
            return None
