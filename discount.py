from abstraction import AbstractApp


class User:
    def get_discount(self):
        return 0


class RegularUser(User):
    def get_discount(self):
        return 5   # 5% discount


class PremiumUser(User):
    def get_discount(self):
        return 20  # 20% discount


class KillHungerApp(AbstractApp):

    def __init__(self):
        super().__init__()
        self.user_type = RegularUser()  # default

    # Implementing abstract methods from AbstractApp
    def register(self):
        self.admin_reg()

    def login(self, email, password):
        return self.admin_login(email, password)

    # Override user_reg to ask for user type
    def user_reg(self):
        super().user_reg()
        print("\nSelect Your Account Type:")
        print("1. Regular User (5% discount)")
        print("2. Premium User (20% discount)")
        utype = input("Enter choice: \n")
        if utype == '2':
            self.user_type = PremiumUser()
        else:
            self.user_type = RegularUser()
        print(
            f"Account Type Discount: {self.user_type.get_discount()}% off on orders!\n")

    # Override show_kart to apply discount
    def show_kart(self):
        if len(self.foodkart) > 0:
            total_price = 0
            for i in self.foodkart:
                print(
                    f" ID={i} | NAME: {self.foodkart[i]['NAME']} | PRICE: {self.foodkart[i]['PRICE']} | QUANTITY : {self.foodkart[i]['QTY']} | TOTAL : {self.foodkart[i]['TOTAL']}")
                total_price += self.foodkart[i]['TOTAL']
            discount = self.user_type.get_discount()
            discounted = total_price * (discount / 100)
            final_price = total_price - discounted
            print(f"\n Subtotal     : {total_price}")
            print(f" Discount ({discount}%) : -{discounted:.2f}")
            print(f" Final Total  : {final_price:.2f}")
        else:
            print("Kart is Empty now add something")

    # Override show_user_profile to display discount
    def show_user_profile(self):
        super().show_user_profile()
        print(f" Account Discount: {self.user_type.get_discount()}%\n")
