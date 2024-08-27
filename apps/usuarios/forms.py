from django import forms

class UsuarioForms(forms.Form):


    nome_login = forms.CharField(
        label = "Nome de login",
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={"class": "form-control", "placeholder":"Ex.: João Silva"},

        )

    )

    senha= forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs= {"class" : "form-control", "placeholder": "Digite Sua Senha"},

        )



    )



class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: João Silva"},

        )

    )

    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: JoãoSilva@xpto.com"},

        )

    )

    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite Sua Senha"},

        )

    )

    senha_2 = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite Sua Senha Novamente"},

        )

    )

    def clean_nome_cadastro(self):

        nome = self.cleaned_data.get("nome_cadastro")

        if nome:

            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possível  inserir espaços dentro do Nome de cadastro")

            else:
                return nome

    def clean_senha_2(self):

        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")


        if senha_2 and senha_1:
            if senha_2 != senha_1:

                raise forms.ValidationError("Senhas não compatíveis")

            else:
                return senha_2