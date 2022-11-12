import queue
from connection import *


#Acceso rolee administrador

#Registrar cuenta()
# 
class id:

    def __init__(self,id,name, email, password, role):
        self.id = id
        self.name = name
        self.email = email
        self.password =password
        self.role = role
        
    

    def __str__(self):
        return f"{self.name} - {self.email} - {self.role}"
        

formulario = [ {
                'id' : 1,
                'name': 'Federico',
                'email': 'fedes77@gmail.com',
                'password': 'passwordsegura',
                'role_user':1
                } 
]
for id in formulario:
    id = id.get('id')
    name = id.get('name')
    email = id.get('email')
    password = id.get('password')
    role_user = id.get('role_user')  

dao = Dao()
#-------------------------------------

# dao.createUser((name,email,password,rolee_user))

#-------------------------------------







datos_actualizados = [ {
                'id' : 1,
                'name': 'Alan',
                'email': 'fedes66@gmail.com',
                'password': 'passwordmassegura',
                'role_user':1
                } 
]
for id2 in datos_actualizados:
    
    if id2.get('name') != name:
        name = id2.get('name')        
    if id2.get('email') != email:
        email = id2.get('email')
    if id2.get('password') != password:
        password = id2.get('password')
    if id2.get('role_user') != role_user:
        role_user = id2.get('role_user')  

#-------------------------------------

# dao.updateUser((name,email,password,role_user,id))

#-------------------------------------







#-------------------------------------

# dao.deleteUser(id)

#-------------------------------------





#devuelve todos los ids

def showUsers(users):
    for user in users:
        q = f"{user[0]} | {user[1]} | {user[2]} | {user[3]} | {user[4]} "
        print(q)

# ids = dao.getAllUsers()

# showUsers(ids)





#-------------------------------------
#devuelve id especifico

id = dao.getUser((id,))
showUsers(id)


#-------------------------------------

#Editar cuenta()

#Eliminar cuenta()

#Recuperar password()



#Acceso rol administrador

#Registrar cuenta()

#Editar cuenta()

#Eliminar cuenta()

#Recuperar contraseña()

