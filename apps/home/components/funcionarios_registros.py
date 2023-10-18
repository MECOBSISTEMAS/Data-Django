from django_unicorn.components import UnicornView, QuerySetType
from django.contrib.auth.models import User
from apps.access.models import Acesso


class FuncionariosRegistrosView(UnicornView):
    usuarios:QuerySetType[User] = User.objects.none()
    nome:str = ""
    email:str = ""
    senha:str = ""
    username:str = ""
    permissao:str = "alimentacao"
    
    def novo_usuario(self):
        if self.permissao == "superuser":
            User.objects.create_superuser(
                username=self.username,
                email=self.email,
                password=self.senha,
                first_name=self.nome,
            )
        else:
            user = User.objects.create_user(
                username=self.username,
                email=self.email,
                password=self.senha,
                first_name=self.nome,
            )
            Acesso.objects.create(
                user=user,
                permissao=self.permissao
            )
        self.filtrar_usuarios()
    
    def mount(self):
        self.usuarios = User.objects.all()
    
    def filtrar_usuarios(self):
        self.usuarios = User.objects.all()
