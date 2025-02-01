from get_database import get_database
dbname = get_database()
 
# Create a new collection
collection_name = dbname["events"]
 
# Create an index on the collection
location_index = collection_name.create_index("location")