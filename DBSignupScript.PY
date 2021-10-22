
import uuid, hashlib, mysql.connector, os   ##importing mysql.connector to connect the mysql database, uuid is generating random objects of 128 bits as ids
 #haslib tranform the plain text into hashes, os helps to automatically perform operating system tasks.
 

SQLpassword = os.environ.get('db_password')   #our variable  is accessed from a  particular evironment from database passwords
 
con = mysql.connector.connect(          #we put all the configuration steps for connecting to our virtual server in a tuple
  host="127.0.0.1",
  user="root",
  password="Passw0rd",
  
)
 
cur = con.cursor()               #we set a variable for the cursor to facilitate what we nedd to do in the database      
 
cur.execute("SHOW DATABASES")   # the cursor will execute the command that shows all the databases
db = cur.fetchall()              #our variable has the value of all databases that our cursor executed with the fetchall() command
print(db)

  

def get_user_info():        #create a function wich takes the user info to register it
    valid = False         #give the variable the value boolean false so we can run a while loop till we get all the information
    while not valid:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        email = input("Enter an email:")
        if username and password and email:  #if we have the needed info our variable has value boolean true
            valid = True
        #regex username, password, email.
        # 
    return username, password, email 
 
def login_get_info():       #create a function that checks the loging information
        valid = False  # set our variable to bool false so while loop is running till gets the needed infp
        while not valid:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username and password:  #if the info are valid, the variable is set to bool true and 
                valid = True
                print('You are logged in! \n')
        #regex username, password, email.
        
        return username, password
 
def add_to_db(username, hashed_password, email):  #create a function that's adding to the database the user inputs
    try:     #use try and except to make our program still work with an except instead of stopping because error
        sql = f"""INSERT INTO `users` VALUES ('{username}', '{hash_password}','{email}')"""  #we make a query to mysql to add the new values into user table
        cur.execute(sql)   #our command is executed with cursor
        con.commit()   #we commit the current transaction
    except:
        print('Insert was not done!')
    else:
        print('All done :) ')
 
def hash_password(password):   #create a function that will take the input password and hash it using salt as well
    salt = uuid.uuid4().hex  #the salt is equal with a 32 hexadecimal string(base 16) wich is a random uuid
    hashed_password = hashlib.sha256(salt.encode()+password.encode()).hexdigest()+":"+salt   #the hashed password is equal with the secure hash algorithm formed of encoded salt +encoded password the hexadecimal digest and the value of salt variable
 
    return hashed_password
 
def verify_hash(userpass, storedpass):   #Verifies the hash from the user password and the stored paswwords
    try:   #Prevents crash in instance of invalid stored hash
        password,salt=storedpass.split(":") #spl
    except:
        pass
    else:
        data = []  #create an empty list
        data.append(password)  #append the password to the list
        data.append(hashlib.sha256(salt.encode()+userpass.encode()).hexdigest()) #append the sal hashed password on the list
    
    return data[0]==data[1]



# def update_logs(): #function that updates the logs
#     sql=("UPDATE user_info.loggin_info ") #run a query to update the logs
#     cur.execute(sql) #cursor is executing mysql query 
#     db.commit() #our database is commiting the change
#     new_user=input("Type your new user name: ")
#     new_password=input("Type your new password: ")
#     new_email=input("Type your new email: ")
#     print("log updated")

#     return new_user, new_password, new_email

# new_user, new_password, new_email = update_logs() #the new variables are equal with 


def main():
    x = 0    #we set our variable to 0 so while loop is running trough all the option that user have and steps that the user needs to do in each option
    while not x:   #create a loop that will run with the options from the user input
        try:     #we use try and except so our program is still running if user didn't choose a valid option, the program is taking like an exception and not a error, is helping with flow control
            user_choice = int(input('Welcome to the program! Please choose one option:  \n1.Register \n2.Login \n3.Exit: '))
        except:
            print("Please enter a valid choice: either 1, 2 or 3: ")
        else:
            if user_choice == 1:
                username, password, email = get_user_info()  #if user choose to register, we call the functions wich takes user information by user input
                hashed_user_pass = hash_password(password)   #the password that user is using is transformed from plain text into hash(not reversible)
                add_to_db(username, hashed_user_pass, email) #add to database the user info that we get
            elif user_choice == 2:  #if user choose to login than we verify if the details match with what we have in the system
                logged_in = False  #create a logged in variable as false so the while loop runs till all the details are matching
                username, password = login_get_info()  #call the function that takes the user info for loging and check if they are the same as we have in the system already
                while not logged_in:  #run a while loop till the user is succesfully logged in
                        #get username and password from our database
                        sql = f"""SELECT password FROM user WHERE username='{username}'""" # we create a query in our sql to check if the password matches the user
                        cur.execute(sql) #the cursor execute our sql query from above
                        items = cur.fetchone() #create a variable that is equal with a single tuple
                        print(items)
                        if items:   #if the item matches the verified hash, with our password and the password from the database , we have a valid
                            db_password = items[0]
                            match = verify_hash(password, db_password)
                            if match:
                                logged_in = True
                                print('You are now logged in. ')
                            else:
                                print('The password doesnt match')
                        else:
                            print('Sorry, I could not find you ')
 
            elif user_choice == 3:   #user choose to exit and x takes the value of 1 so the loop can stop
                print('Goodbye!')
                x = 1
            else:
                print('Please type 1, 2 or 3 to indicate your choice: ')   # user is asked to choose a valid option

while(1):   #while is set to 1 so it runs all the possible options for the user

 main()









