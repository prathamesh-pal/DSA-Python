target = 10
position =[6,8]
speed =    [3,2]

cars = list(zip(position, speed))

cars.sort(reverse=True)
fleet =0 
max_time = 0

for position , speed  in cars:
    time = (target - position) / speed

    if time > max_time :
        fleet +=1 
        max_time  = time

print(fleet)