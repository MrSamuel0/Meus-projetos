import datetime

segunda = ['Lógica para computação', 'Fundamentos de tecnologia da computação']
terca = ['Experiência e interface com o usuário', 'Construção de software para web']
quarta = ['Construção de software para web']
quinta = ['Lógica para computação', 'Design e desenvolvimento de banco de dados 1']
sexta = ['Design e desenvolvimento de banco de dados 1']

data = datetime.date.today()
dia_semana = datetime.date.weekday(data)

def aula(dia):
    match(dia):
        case 0:
            print('hoje é segunda-feira, e você tem aula de: ')
            for i in segunda:
                print(i)
        case 1:
            print('Hoje é terça-feira, e você tem aula de: ')
            for i in terca:
                print(i)
        case 2:
            print('Hoje é quarta-feira, e você tem aula de: ')
            for i in quarta:
                print(i)
        case 3:
            print('Hoje é quinta-feira, e você tem aula de: ')
            for i in quinta:
                print(i)
        case 4:
            print('Hoje é sexta-feira, e você tem aula de: ')
            for i in sexta:
                print(i)
        case 5:
            print('Hoje é sábado, e você não tem nenhuma aula. Aproveite para descançar e revisar os conteúdos estudados na semana.')
        case 6:
            print('Hoje é domingo, descanse bastante e se organize para a semana.')

aula(dia_semana)
       





