#8-14. Cars: Write a function that stores information about a car in a diction-
#ary. The function should always receive a manufacturer and a model name. It
#should then accept an arbitrary number of keyword arguments. Call the func-
#tion with the required information and two other name-value pairs, such as a
#color or an optional feature. Your function should work for a call like this one:
#car = make_car('subaru', 'outback', color='blue', tow_package=True)
#Print the dictionary that’s returned to make sure all the information was
#stored correctly.

def car_info(make, model, **car_info):
    car = {}
    car['make'] = make
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car = car_info('geo', 'metro',release='quick release',make_money_with='true')
print(car)
