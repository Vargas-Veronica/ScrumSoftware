class employee :
    id = ""
    name = ""
    user = ""
    password = ""
    role = ""
    canEdit = ""

    def __init__(self, id, name, user, password, role, canEdit):
         self.id = id
         self.name = name
         self.user = user
         self.password = password
         self.role = role
         self.canEdit = canEdit
         

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id



    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name



    def get_user(self):
        return self.user
   
    def set_user(self, user):
        self.user = user
     
     
    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

        
    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role= role  
      
    def get_canEdit(self):
        return self.canEdit

    def set_canEdit(self, canEdit):
        self.canEdit = canEdit  
      
class role:
    def __init__(self,id,role_name):
        self.id = id
        self.role_name = role_name
    
    def __str__(self):
        return f"{self.id} - {self.role_name}" 
        
                         
    
    