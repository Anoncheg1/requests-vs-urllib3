import requests
import json

texts1 = """
Добрый день, могу я услышать?
Звонок из «РУСНАРБАНКа» Меня зовут…»
Вы оставляли Заявку на автокредит?
Актуальна ли для Вас заявка/ Еще рассматриваете вопрос о приобретении автомобиля?»
Удобно будет сверить сейчас данные по анкете?
Вам сейчас удобно разговаривать?
Вы можете уделить время для проверки данных по анкете»?
Информируем Вас о том, что ведется запись телефонных переговоров.»
Назовите Ваши ФИО, дату рождения и количество полных лет.
По какому адресу зарегистрированы и проживаете?
Состоите ли в барке?
Назовите ФИО и дату рождения супруги (Если клиент состоит в браке)
Какой автомобиль планируете приобрести (марка, модель, год выпуска), стоимость выбранного ТС и первоначальный взнос.
Трудоустроены ли Вы на данный момент?
Как называется организация, в которой Вы работаете? Уточните, пожалуйста, должность и уровень заработной платы.
Сможете ли Вы оплачивать по кредитным обязательствам в полном объеме с учетом сложившейся экономической ситуации в стране?
Чьи контактные данные оставляли в анкете?
"""

texts2 = """
Добрый день, могу я услышать ?
Звонок из «РУСНАРБАНКа» Меня зовут…
Вы оставляли Заявку на автокредит?
Актуальна ли для Вас заявка
Еще рассматриваете вопрос о приобретении автомобиля?
Удобно будет сверить сейчас данные по анкете?
Вам сейчас удобно разговаривать?
Вы можете уделить время для проверки данных по анкете?
Информируем Вас о том, что ведется запись телефонных переговоров
Назовите Ваши ФИО.
Ваша дата рождения, количество полных лет.
По какому адресу зарегистрированы/проживаете?
Кто проживает вместе с вами?
В чьей собственности находится недвижимость?
По какой причине недавно меняли паспорт
По какой причине не по сроку меняли паспорт
Состоите ли в барке?
Есть ли у Вас на иждивении дети?
Назовите ФИО и дату рождения супруги
Уточните место работы супруги и доход?
Какой автомобиль планируете приобрести?
Какова стоимость автомобиля? Какой первоначальный взнос планируете внести?
С какой целью приобретаете автомобиль?
Кто будет пользоваться автомобилем, и для кого приобретается автомобиль?
На какой ежемесячный платеж по кредиту рассчитываете?
Трудоустроены ли Вы на данный момент?
Как называется организация, в которой вы работаете?
По какому адресу находится организация?
Какая сфера деятельности организации?
Отобразилась ли сложившаяся экономическая ситуация в стране на деятельности Вашей организации?
Ваша должность? Стаж работы?
Уточните, пожалуйста, ФИО Вашего непосредственного руководителя?
Уточните, пожалуйста, ФИО Ген. Директора?
Какой у вас ежемесячный доход?
Из чего складывается ваш ежемесячный доход
Из чего складывается ваш доход по основному месту работы,
Из чего складывается ваш доход по месту работы по совместительству,
Из чего складывается иные источники дохода)?
Чей рабочий телефон оставляли?
Оформляли ли вы ранее кредитные карты?
Оформляли ли вы ранее кредиты?
Когда обращались за кредитом? Уточнить год, по возможности месяц или хотя бы сезон: весна, лето, осень, зима.
В какой банк?
На какой лимит оформляли кредит?
На какую сумму оформляли кредит?
Возникали ли у Вас просрочки по кредитам?
По какой причине допускались просрочки?
С чем связано несвоевременное погашение кредита
Чьи контактные телефоны Вы предоставляли в заявке?
Можете назвать примерный остаток задолженности по кредиту.
"""
texts3 = """Добрый день
Добрый вечер
Доброе утро
оставляли Заявку на автокредит
Актуальна ли для Вас заявка
рассматриваете вопрос о приобретении автомобиля
данные по анкете
сейчас удобно разговаривать
можете уделить время для проверки данных по анкете
ведется запись разговора
ведется запись телефонных переговоров
Назовите Ваши ФИО, дату рождения и количество полных лет
По какому адресу зарегистрированы и проживаете
Состоите ли в барке
Назовите ФИО и дату рождения супруги
Какой автомобиль планируете приобрести
Трудоустроены на данный момент
Как называется организация, в которой Вы работаете
должность и уровень заработной платы
экономической ситуации в стране
чьи контактные данные оставляли в анкете?"""


def transcribe(file_path: str) -> str or None:
    # curl -X 'POST' \
    #   'http://127.0.0.1:8081/transcribe'n \
    #   -H 'accept: application/json' \
    #   -H 'Content-Type: multipart/form-data' \
    #   -F 'file=@1670162239-2022-12-04-16_57.mp3;type=audio/mpeg'
    rid = None
    with open(file_path, 'rb') as file:

        r = requests.post('http://127.0.0.1:8081/transcribe', files={'file': file})
        # requests.
        # r.request()

        if r.status_code != 200:
            print(r.status_code, r.text, r.json())
            exit()
        d = r.json()
        print('response:')
        print(type(d), r.text)
        print(d, r.text)
        print(r.headers)
        rid = d['id']
        for x in d['channel1']:
            print(x['text'])
    return rid


def sequences(rid, sentences):
    # curl -X 'POST' \
    #   'http://127.0.0.1:8081/transcribe/4ec75e1d/find_sentence?sentences=%D0%B4%D0%BE%D0%B1%D1%80%D1%8B%D0%B9%20%D0%B4%D0%B5%D0%BD%D1%8C&sentences=%D1%80%D1%83%D1%81%D0%BD%D0%B0%D1%80%D0%B1%D0%B0%D0%BD%D0%BA&sentences=string' \
    #   -H 'accept: application/json' \
    #   -d ''
    p = requests.Request('POST', f'http://127.0.0.1:8081/transcribe/{rid}/find_sentence', params={'sentences': sentences})
    # p = p.prepare()
    # p.prepare_headers(p.headers)
    # print(p.prepare().__dict__)
    from requests import Session
    p = Session().prepare_request(p)
    [print(x) for x in p.__dict__.items()]
    # exit()
    p = requests.post(f'http://127.0.0.1:8081/transcribe/{rid}/find_sentence', params={'sentences': sentences})
    print("----request:")
    [print(x) for x in p.request.__dict__.items()]
    print("----response:")
    [print(x) for x in p.__dict__.items()]

    assert p.status_code == 200
    # print(p.status_code, p.json())
    p.encoding = 'UTF-8'
    return p.json()


if __name__ == '__main__':
    import time
    import re

    # -- transcribe audio
    # rid = transcribe('/home/u2/Downloads/89676550013_record.mp3')
    # assert rid is not None
    # print(rid)
    # exit()
    rid = '78264309'  # '88d03281'
    # for i, texts in enumerate([texts3]):
    for i, texts in enumerate([texts1, texts2, texts3]):
        # for i, texts in enumerate([texts3]):

        # -- start timer
        start = time.time()
        # -- log file
        with open(f'{i}.txt', 'w') as file:
            # -- prepare sentences for search in transcription
            texts = texts.split('\n')
            print(texts)
            texts = [x.lower() for x in texts]
            texts = [re.sub(r'[^А-Яа-я ]', '', x) for x in texts if len(x) > 0]
            texts = [x for x in texts]
            print(texts)
            for x in texts:
                file.write(x)
                file.write('\n')
            sentences = texts
            # -- request search for seantences
            r = sequences(rid, sentences)
            # -- save result of search in file

            resp = json.dumps(r, indent=4, ensure_ascii=False)
            print(resp)
            file.write(resp)
            file.write('\n')
            # -- how much time it takes?
            file.write(f'seconds:{round(time.time() - start)}')
