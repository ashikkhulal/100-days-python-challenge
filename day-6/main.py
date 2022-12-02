## Defining and calling python functions:

# in built functions: https://docs.python.org/3/library/functions.html

## Defining function:
# def my_function():
#     print("Hello")
#     print("Bye")


## Calling the defined function:
# my_function()

## Reborg's world: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

## Exercise-1:
# Hurdle challenge in Reborg's world: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def one_hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# for run in range(6):
#     one_hurdle()

## Indentation in python:
# https://peps.python.org/pep-0008/

## While loops in python:

# while something_is_true:
#     #Do something repeatedly

# number_of_hurdles = 6
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def one_hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while number_of_hurdles > 0:
#     one_hurdle()
#     number_of_hurdles -= 1

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def one_hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# hurdles = 6
# while hurdles > 0 :
#     one_hurdle()
#     hurdles -= 1
#     if at_goal():
#         hurdles = 0

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     elif front_is_clear:
#         move()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def opposite_l():
#     turn_right()
#     move()
#     turn_right()
#     move()
      
# while not at_goal():
#     if wall_in_front():
#         turn_left()
#         move()
#     elif right_is_clear() and is_facing_north():
#         opposite_l()
#     elif wall_on_right and is_facing_north():
#         move()
#     elif front_is_clear:
#         move()



