from phonenumbers import PhoneNumberFormat, parse as phone_parse, format_number as phone_format

def trata_telefone(telefone):
    try:
        phone = phone_format(phone_parse(telefone, 'BR'), PhoneNumberFormat.E164)

        # adiciona 9 depois do DDD
        if len(phone) == 13:
            phone = phone[:5] + "9" + phone[5:]
            return [True, phone]
        # se está com 14 digitos, verifica se o 6º digito é 9
        elif len(phone) == 14 and phone[5] == "9":
            return [True, phone]
        # telefone sem ddd ou com outro numero no lugar do 9
    except:
        return [False, "Telefone inválido"]
