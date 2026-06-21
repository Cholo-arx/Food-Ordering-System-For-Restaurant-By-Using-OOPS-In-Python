LINK of original code: https://github.com/Pkamble19/Food-Ordering-System-For-Restaurant-By-Using-OOPS-In-Python
credit:Pkamble19

food_ordering_system.py
    the base class holding all core data and CRUD
    behaviour, plus a standalone Driver_code() for running this file by
    itself (not used by main.py, which goes through abstraction.py/
    discount.py instead).

abstraction.py
    an abstract layer over FoodApp that forces
    concrete subclasses to supply their own register()/login() behaviour,
    and supplies the run() menu loop that drives the whole program.

        AbstractApp(ABC, FoodApp) class
            This defines the class AbstractApp, which inherits from ABC 
            (to enable abstract method enforcement) and FoodApp (to maintain compatibility with the base system). 
            This is the contract that ensures any custom app implementation follows the base system's structure.
            
        @abstractmethod and @abstractmethod
            These are strict requirements for any child class. By defining these here without logic, you force 
            the developer to write custom register and login methods in their specific application version, 
            ensuring the system remains functional even when extended.
            
        def run(self) - This is the primary application entry point, displaying the first welcome screen and a 
        top-level menu that allows the user to pick ADMIN, USER, or close the application. It serves as the main control loop for the entire system.

        def _admin_menu(self) - This function manages the administrative access flow. It allows an administrator to 
        create a new account, log into an existing account, or return to the main menu. If the login is successful, the administrator is directed to the food management interface.

        def _admin_food_menu(self) - This creates a working dashboard for administrators to execute CRUD (Create, Read, Update, and Delete) actions on the 
        food inventory. It uses interactive prompts to capture food details such as name, price, and stock levels, and it controls menu logic for changing or removing specific products.

        def _user_menu(self) - This serves as the user's gateway, displaying a menu with options to register for a new account or login. 
        It checks user credentials against stored data before directing authenticated users to their personal account management dashboard.

        def _user_account_menu(self) - This is the major navigation hub for logged-in users, with options to go to the order menu, see history, access profile settings, and edit personal information.

        def _order_menu(self): This manages the user's shopping experience. It allows customers to browse the available food list, 
        add particular things to their digital cart, remove items from the basket, or view their current cart status before checking out.

        def _add_to_kart_flow(self) - This function implements the logic for batch-adding items to the user's cart using given IDs. 
        It also functions as an intermediary sub-menu, allowing users to examine their cart or confirm their order after adding items.

        def _show_kart_and_checkout(self) - This function handles the final step of the ordering process. It displays the current cart contents to 
        the user and offers a checkout option to confirm the order, record the order history, and clear the cart for future usage.
        
discount.py

        Defines a small discount-tier class hierarchy and KillHungerApp, the
        concrete app used by main.py.
        
        User class
        get_discount(self) - Serves as the base interface, returning a default discount of zero.
        
        RegularUser(User) class
            get_discount(self) - Overrides the basic method and returns 5, which represents the 5% discount rate for regular users.
        
        PremiumUser(User) class
            get_discount(self) - Overrides the base function by returning 20, which represents the higher 20% discount rate for premium users.


KillHungerApp(AbstractApp) class
    Also an EXAMPLE of INHERITANCE within the same file

        __init__(self) - Constructor; initializes the parent application logic and defaults the user discount level to RegularUser.

        register(self) - Concrete implementation; sends registration requests to the administrative registration method defined in the parent class.
        
        login(self, email, password) - Concrete implementation that sends the login request to the administrator login function defined in the parent class.
        
        user_reg(self) - Overrides the base registration, prompting the user to choose an account type (Regular or Premium), updating the self.user_type object, and displaying the associated discount.
        
        show_kart(self) - Overrides the base cart display by calculating the total price of items, retrieving the discount percentage based on the active user_type, and printing the discounted total.



main.py

        Just entry point to call the system. Creates a KillHungerApp, runs a quick polymorphism demo
        (get_discount() on a RegularUser and a PremiumUser), then calls
        obj.run() to start the interactive menu, finishing with a goodbye
        message.

====================================================================================================
Abstraction: AbstractApp forces every concrete app to define its
own register()/login(), while still inheriting all of FoodApp's
ready-made behaviour.

Inheritance: KillHungerApp extends AbstractApp (which extends
FoodApp); RegularUser/PremiumUser extend User.

Polymorphism: get_discount() behaves differently depending on
whether self.user_type is a RegularUser or PremiumUser, and
run() calls self.register()/self.login() without knowing which
concrete implementation it's invoking.

Encapsulation: In food_ordering_system.py, the FoodApp class encapsulates 
the application's state by initializing core dictionaries—such as self.food and 
self.user_details—within the __init__ constructor, ensuring that this data is only 
managed by the class's functions. Furthermore, using a leading underscore in method names 
(_admin_menu(), _user_menu(), _order_menu()) is a standard Python convention that indicates 
that these are internal helper methods, effectively hiding complex system navigation logic from 
external modules and exposing only a clean, simplified interface for interaction between users.
====================================================================================================
