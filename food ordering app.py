#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[88]:


class food_items():
    def __init__(self,id,name,quantity,price,discount):
        self.id=id
        self.name=name
        self.quantity=quantity
        self.price=price
        self.discount=discount
        
food1=food_items( '1','veg biryani','1 plate','Rs.220','5%')    
food2=food_items('2','butter nan','1 pieces','Rs.20','5%')
food3=food_items('3', 'chilli chicken','1 Plate', 'Rs.260','5%')
food4=food_items("4",'fanta','750 ml','1 bottle','5%')
print(food1.id,food1.name,food1.quantity,food1.price,food1.discount)
print(food2.id,food2.name,food2.quantity,food2.price,food2.discount)
print(food3.id,food3.name,food3.quantity,food3.price,food3.discount)
print(food3.id)


def stock (stock):
    if stock >=50 :
        return "stock availaible"
    else: 
        return"stock unavailaible"
a =stock(60)
print(a)
class list_of_food_items():
    print("\nview list of all food__")
    
    foods=['veg biryani','chilli chicken','butter nan','fanta']   

    for i in foods:
        print(i)
    
def removing_item_from_list():
    My_foods_list=['tandoori chicken','tandoori roti', 'Vegan Burger']   
    food=My_foods_list.pop(0)
print(food)
print('\nremoving_item_from_list__')
print(food)
class user():
    def registration(self,full_name,phone_number,email,address,password,):
        self.full_name=full_name
        self.phone_number=phone_number
        self.email=email
        self.address=address
        self.password=password
        return "\nregistration completed succesfull"
       
    def login(self,full_name,password):
        if  self.full_name==full_name:
            if self.password==password:
                return'\nuser logged in to application' 
            else:
                return'\nwronge password or full_name'

user1=user()

print(user1.registration('azhar',12345678,'azharajju175@gmail.com','hyderabad','ajju'))
print(user1.login('azhar','ajju'))


            

class user_options():
     def neworder(self,place_neworder,order_history,update_profile):
            self.order_history=order_history
            self.update_profile=update_profile
            self.place_neworder=place_neworder
print("place_new_order\n order_history \n update_profile")
            

foods=[{'name':'tandoori chicken',}, {'name': 'Vegan Burger',}] 
for i in foods:
    print("your new order",f"{foods.index(i)+1}. {i['name']}")

class restaurent():
    print("\nlist of the food items:::")
    def list(self,list):
        self.list=list
my_dict=[{ 1:'Tandoori Chicken','qut':'4 pieces' ,'INR': 240},{2: 'Vegan Burger','qut': "1 Piece", 'INR': 320},
  {3: 'Truffle Cake','qut': 500, 'INR': 900}]
for key  in my_dict:
     print(key)
        


        
def history(self,order_history):
    self.order_history==order_history
foods=[{'name':'tandoori chicken',}, {'name': 'Vegan Burger',}]
print("\nyour order history")
for i in foods:
    print(f"{foods.index(i)+1}. {i['name']}")


    
      
    def update_profile(update_profile):
        if "azhar ajju" != "cheruvu azhar":
            return "\nprofile  updated"
        if 'azhar ajju'=='cheruvu azhar':
            return '\nyour profile not  updated'
        
        
s1=update_profile('azhar ajju')
print(s1)


# In[ ]:




