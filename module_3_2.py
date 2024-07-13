def send_email(message, recipient, sender="university.help@gmail.com"):
    send_right = False
    send_self = False
    send_default = False
    send_form = ['@', '.com', '.ru', '.net']
    for i in send_form:
        if recipient.__contains__(i):
            for i in send_form:
                if sender.__contains__(i):
                    send_right = True
    if sender == recipient:
        send_self = True
    if sender == "university.help@gmail.com":
        send_default = True

    if send_right == False:
        print("Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient + ".")
    elif send_self == True:
        print('Нельзя отправить письмо самому себе!')
    elif send_default == True:
        print("Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient + ".")
    elif send_default == False:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient + ".")
    else:
        return


send_email('this is not spam', 'ololo.com', 'univesity.help@gmail.com')