"""Restaurant rating lister."""

def read_ratings(file_path):

    restaurant_details = open(file_path)

    restaurants = {}

    for line in restaurant_details:

        line = line.rstrip()
        details = line.split(":")
        restaurant_name, restaurant_rating = details

        restaurants[restaurant_name] = restaurant_rating

    #ask user for input = name
    name = input("What restaurant do you want to add? ")
    name = name.title()
    #ask user for input = score
    rating = input("What is the rating? ")
    #take input and add into dict
    restaurants[name] = rating
    #print in alphabetical order
    
    #list = sorted(dict)
    alpha_rests = sorted(restaurants)
    #loop through list
    for restaurant in alpha_rests:
        print(f"{restaurant} is rated at {restaurants[restaurant]}.")
    # print rname and dict[rname]=rating

    restaurant_details.close()

    


read_ratings("scores.txt")




