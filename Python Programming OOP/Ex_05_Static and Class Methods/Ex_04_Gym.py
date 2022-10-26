"""
Output:

2
Subscription <1> on 14.05.2020
Customer <1> John; Address: Maple Street; Email: john.smith@gmail.com
Trainer <1> Peter
Equipment <1> Treadmill
Plan <1> with duration 20 minutes
"""
from Ex_04_project.customer import Customer
from Ex_04_project.equipment import Equipment
from Ex_04_project.exercise_plan import ExercisePlan
from Ex_04_project.gym import Gym
from Ex_04_project.subscription import Subscription
from Ex_04_project.trainer import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
