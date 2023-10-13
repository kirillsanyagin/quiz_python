notes = {}
PATH = 'notes.txt'

def open_file(note: dict):
   with open(PATH , 'r', encoding='UTF-8') as file:
      data = file.readlines()
   for i,record in enumerate(data, 1):
      record = record.strip().split(';')
      note[i] = record

def save_file(note: dict):
   all_notes = []
   for record in note.values():
      all_notes.append(';'.join(record))
   with open(PATH, 'w', encoding='UTF-8') as file:
      file.write('\n'.join(all_notes))

def show_notes(note: dict, message: str):
   print('\n' + '='*110)
   if note:
      for i,record in note.items():
         print(f'{i:>3}.{record[0]:<30} {record[1]:<20} {record[2]:<30} {record[3]:<20}')
   else:
      print(message)
   print('='*110 + '\n')

def add_new_note(note: dict ,new: list):
   cur_id = max(note.keys()) + 1
   note[cur_id] = new

def find_note(note: dict, search: str):
   result = {}
   for i , record in note.items():
      for field in record:
         if search.lower() in field.lower():
            result[i] = record
            break
   return result

def func_search(note : dict):
   search = input('Что будем искать? ')
   result =  find_note(note, search)
   show_notes(result, f'Заметка, содержащий {search} не найдена!')

def change_note(note: dict, cid: int):
   id, name, comment, data_created = note.get(cid)
   ch = []
   for item in ['Введите порядковый номер: (или оставьте пустым , чтобы не изменять): ',
                'Введите название заметки:(или оставьте пустым , чтобы не изменять) ',
                'Введите коммент: (или оставьте пустым , чтобы не изменять)',
                'Введите дату создания: (или оставьте поле пустым, чтобы не изменять)']:
      ch.append(input(item))
   note[cid] = [ch[0] if ch[0] else id, ch[1] if ch[1] else name, ch[2] if ch[2] else comment,ch[3] if ch[3] else data_created]
   return ch[0] if ch[0] else id



def delete_contact(note: dict, cid: int):
   name = note.pop(cid)
   return name[0]



def menu():
   menu_points = ['Открыть заметки',
                  'Сохранить записи',
                  'Посмотреть все записи',
                  'Добавить заметку ',
                  'Найти заметку',
                  'Изменить запись',
                  'Удалить запись',
                  'Выход '] 
   print('Главное меню')
   [print(f'\t{i}. {item}') for i , item in enumerate(menu_points, 1)]
   choice = int(input('Выберите пункт меню: '))
   return choice

while True:
   choice =  menu()
   match choice: 
         case 1:
            open_file(notes)
            print()
            print('Заметки успешно открыты!\n')
         case 2:
            save_file(notes)
            print()
            print('Заметки успешно сохранены!\n')
         case 3:
           show_notes(notes, 'Заметки пусты или не октрыты!')
         case 4:
            new = []
            for item in ('Введите ID: ','Ввведите название заметки ','Введите коммент: ','Введите дату создания '):
               new.append(input(item))
            add_new_note(notes, new)
            print()
            print(f'Запись {new[0]} успешно добавлена!\n')
         case 5:
           func_search(notes)
         case 6:
            func_search(notes)
            select = int(input('Какую запись будем изменять? '))
            name = change_note(notes,select)       
            print(f'Запись {name} успешно изменена!')
         case 7:
            func_search(notes)
            select = int(input('Какую запись будем удалять? '))
            name = delete_contact(notes,select)        
            print(f'Запись {name} успешно удалена!')
         case 8:
           print('\nПока!')
           break