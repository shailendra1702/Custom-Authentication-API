from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self,email,mobile,password = None, **extra_fields):
        
        if not email:
            raise ValueError('Email is required')
        if mobile is None:
            raise ValueError('Mobile number is required')
        email = self.normalize_email(email)
        
        user = self.model(email = email, mobile= mobile, **extra_fields)
        user.set_password(password)
        user.save(using = self._db) 
        return user
    
    def create_superuser(self,email, mobile,password = None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        # extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff True')
        
        return self.create_user(email, mobile,password, **extra_fields)