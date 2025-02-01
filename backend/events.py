from get_database import get_database
dbname = get_database()
collection_name = dbname["events"]

item_1 = {
  "name" : "James' cool bball tournament",
  "type" : "Basketball Tournament",
  "location" : "Nelson Fitness Center",
  "time" : ["2/2/2025", "12:30pm"],
  "description" : "Come for the coolest basketball tournament you've ever seen.",
  "roster" : ["LeBron James", "Ash Ketchum"],
  "audience" : ["Feddy Fazbear"],
  "pot": 15
}

item_2 = {
  "name" : "Pizza Security Guard Night Shift",
  "type" : "Survive",
  "location" : "Freddy's Pizzeria",
  "time" : ["2/3/2025", "12:00am"],
  "description" : "Hello? Hello, hello? Uh, I wanted to record a message for you to help you get settled in on your first night...",
  "roster" : ["LeBron James"],
  "audience" : ["Feddy Fazbear"],
  "pot": 1000
}

item_3 = {
  "name" : "Pokemon Tournament",
  "type" : "Pokemon Tournament",
  "location" : "Scili",
  "time" : ["2/2/2025", "6am"],
  "description" : "Time for the best pokemon showdown ever. I will be using all my legendary pokemon and you can't stop me.",
  "roster" : ["Feddy Fazbear", "Ash Ketchum", "LeBron James"],
  "audience" : [],
  "pot": 3
}

collection_name.insert_many([item_1,item_2,item_3])