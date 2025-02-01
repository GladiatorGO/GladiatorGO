from get_database import get_database
dbname = get_database()
collection_name = dbname["profiles"]

item_1 = {
  "name" : "LeBron James",
  "email" : "lebronbron@brown.edu",
  "password" : "12345",
  "bio" : "It's me, LeBron James.",
  "credits" : 340,
  "location" : "Providence, Rhode Island",
  "match history" : "idk how to represent this yet"
}

item_2 = {
  "name" : "Feddy Fazbear",
  "email" : "fivenights@gmail.com",
  "password" : "bonnie-chica-foxy",
  "bio" : "Was that the bite of 87!?",
  "credits" : 10,
  "location" : "San Francisco, California",
  "match history" : "idk how to represent this yet"
}

item_3 = {
  "name" : "Ash Ketchum",
  "email" : "pikachuIchooseyou@yahoo.com",
  "password" : "UseThunderbolt",
  "bio" : "Gotta catch 'em all!",
  "credits" : 1000,
  "location" : "Lumiose City, Kalos Region",
  "match history" : "idk how to represent this yet"
}

collection_name.insert_many([item_1,item_2,item_3])