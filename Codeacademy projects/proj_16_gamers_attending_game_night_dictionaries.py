gamers = []


#Adds gamer to germs_list
def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
        

add_gamer({"name": "Jeff", "availability": "Monday"}, gamers)



kimberly = {"name": "kimberly", "availability": ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)



add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


#Builds daily frequency_table to make life easier
def build_daily_frequency_table():
    return {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday":0, "Saturday": 0, "Sunday": 0}
count_availability1 = build_daily_frequency_table()

#Calculates what days people are available
def calculate_availability(gamers_list, available_frequency):
    print(gamers_list)
    for gamer in gamers_list:
        for day in gamer["availability"]:
            if type(gamer["availability"]) == list:
                available_frequency[day] = available_frequency.get(day) +1

            else: 
                available_frequency[gamer["availability"]] = available_frequency.get(gamer["availability"]) +1
                break
        
#Finds best night, where most people are available         
def find_best_night(availability_table):
    highest_value = 0
    for key, value in availability_table.items():
        if value > highest_value:
            highest_value = value
            highest_value_key = key
    return highest_value_key


                
calculate_availability(gamers, count_availability1)

print(count_availability1)

game_night = find_best_night(count_availability1)


#Creates list of the people who are available
def available_on_night(gamers_list, day):
    gamers_free = []
    game_night = day
    for gamer in gamers_list:
        for key, value in gamer.items():
            if game_night in value:
                gamers_free.append(gamer)
                break

    return gamers_free


attending_game_night = available_on_night(gamers, game_night)

print(attending_game_night)


form_email = "{name},{day_of_week},{game}"

#Sends email to people attending
def send_email(gamers_who_can_attend, day, game):

    for gamer in gamers_who_can_attend:
        print(form_email.format(name = gamer["name"], day_of_week = day, game = game))

send_email(attending_game_night, game_night, "Abruptly Goblins!")


#People who couldn't attend

unable_to_attend_best_night = [gamer for gamer in gamers if gamer not in attending_game_night]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)
print(second_night)

available_second_game_night = available_on_night(gamers, second_night)

send_email(available_second_game_night, second_night, "Abruptly Goblins")