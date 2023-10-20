def roll_call_dwarves(names):
    for index in range(len(names)):
        print(f'{index + 1}. {names[index]}')

def summon_captain_planet(planeteers):
    return [f'{call.title()}!' for call in planeteers]

def long_planeteer_calls(calls):
    return True if [call for call in calls if len(call) > 4] else False

def find_the_cheese(string_list):
    cheese = ["cheddar", "gouda", "thyme"]
    cheese_list = [item for item in string_list if item in cheese]
    return cheese_list[0] if cheese_list else None
