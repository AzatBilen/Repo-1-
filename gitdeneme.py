kullanicilar=[
    {
        "name":"Berivan",
        "username":"berivan",
        "şifre":"1234",
        "bakiye":20000
    },

    {
        "name":"Mizgin",
        "username":"mizgin47",
        "şifre":"12345",
        "bakiye":15000
    },

    {
        "name":"kerem",
        "username":"saygılar",
        "şifre":"4380",
        "bakiye":1
    }
]

while True:
    kullanici=input("kullanici adinizi giriniz")
    for user in kullanicilar:
        if user["username"]==kullanici:
            password=input("lütfen şifrenizi giriniz")
            if user["şifre"]==password:
                print("kullanıcı giriş yaptı")