from discount import KillHungerApp, RegularUser, PremiumUser
# Import Driver_code from where your FoodApp logic resides
from food_ordering_system import Driver_code

if __name__ == "__main__":

    # If you specifically need to use the KillHungerApp object
    # to maintain the class structure used in source 2:

    # 1. Keep the polymorphism demo
    print("=" * 50)
    print("[ Polymorphism Demo — same method, different output ]")
    for u in [RegularUser(), PremiumUser()]:
        print(f"  {u.__class__.__name__}.get_discount() -> {u.get_discount()}%")
    print("=" * 50)

    # 2. Call the driver code instead of .run()
    Driver_code()

    print('THANK YOU VISIT AGAIN :')
