from database import Database
from family import Family

db = Database("bolt://44.203.249.152:7687", "neo4j", "quarter-doorsteps-ways")
#db.drop_all()
family_db = Family(db)

# returns someone's children
children = family_db.get_children({"key": "nome", "value": "Amanda"})
for value in children:
    print("Amanda's child", value)

# returns someone's spouse
spouse = family_db.get_spouse({"key": "nome", "value": "Pedro"})
for value in spouse:
    print("Pedro's spouse", value)

# returns a pet's owner
owner = family_db.get_owner({"key": "nome", "value": "Salem"})
for value in owner:
    print("Salem's spouse", value)

db.close()
