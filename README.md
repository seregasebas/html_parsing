парисинг музыкального сайта(рок-музыкантов) : https://www.last.fm/ru/tag/rock/artists

парсинг ведется по всем страницам сайта с рок-музфкантами(всего 48 стр)

На выходе получаем json файл со следующими данными:
1. Название группы
2. ссылка на группу - переходишь и наслаждаешься любимой музыкой
3. описание группы - краиткое описание группы

telegram_bot_parser: 
/start:
1. Запускает бота и предлагает участнику провести парсинг сайта
2. В чат высылает файл текстовый со списком групп
3. Предлагает выбрать группу из списка
4. После написания названии группы юзером бот выдает крткое описание группы и ссылку на прослушивание песен данной группы на сайте https://www.last.fm/ru
/all: если запрос делает админ, то в чат высылается результаты парсинга в json формате, если не админ, то получает сообщение:"Извините, у вас нет прав доступа(("
/help: описание команд и функционала бота