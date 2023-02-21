# Импорт пакетов для pgSQL
import psycopg2
from psycopg2 import Error

# Импорт пакетов для визуализации таблицы
from tkinter import *
from tkinter import ttk

import queries
# Импорт пакета для задежки времени работы программы
import time

# ПОДКЛЮЧЕНИЕ к БД, где: база данных MGOK_1,
# имя пользователя MGOK, пароль Leonova2001 и host это localhost или 127.0.0.1
# После зададим курсор для операций с БД - cursor
try:
    conn = psycopg2.connect(database="MGOK_1", user="postgres", password="Leonova2001", host="localhost", port="5432")
    # Курсор для выполнения операций с базой данных
    cursor = conn.cursor()
    # Распечатать сведения о pgSQL
    print("Информация о сервере PostgreSQL")
    print(conn.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получение результата
    record = cursor.fetchone()
    print("Вы подключены к базе данных MGOK_1", record, "\n")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        cursor.close()  # закрываем курсор
        conn.close()  # закрываем подключение
        print("Соединение с PostgreSQL закрыто")

# ФЛОТАЦИЯ-МЕДЬ ПЕРВИЧНЫХ СУЛЬФИДОВ
# СОЗДАДИМ ВИЗУАЛЬНОЕ ОТОБРАЖЕНИЕ ТАБЛИЦЫ
root = Tk()
root.title("ФЛОТАЦИЯ")
root.geometry("1500x550")

# СОЗДАДИМ ВКЛАДОКИ
# Создаём набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

# Создадим 5 фреймов для 5 вкладок (5 вкладок = 5 таблиц = 5 типов руды)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)
frame5 = ttk.Frame(notebook)

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)
frame4.pack(fill=BOTH, expand=True)
frame5.pack(fill=BOTH, expand=True)

# Прикрепляем фреймы(вкладки) на основную панель
notebook.add(frame1, text="Медь первичных сульфидов")
notebook.add(frame2, text="Медь вторичных сульфидов")
notebook.add(frame3, text="Медь окисленная")
notebook.add(frame4, text="Медь водорастворимая")
notebook.add(frame5, text="Медь общая")

# 1 ТАБЛИЦА
# ОПРЕДЕЛЯЕМ ДАННЫЕ ДЛЯ ОТОБРАЖЕНИЯ В ВИЗУАЛЕ
# Устанавливаем соединение с pgSQL
conn = psycopg2.connect(database="MGOK_1", user="postgres", password="Leonova2001", host="localhost", port="5432")
# Задаём курсор
cursor = conn.cursor()
# Получаем все данные из таблицы tbl_copper_primary_sulfides
# Столбики от 0 до 67, где 67 - это id
cursor.execute(queries.qSelectAll1_1)
# Присваиваем визуальному отображению
ris_copper_primary_sulfides = cursor.fetchall()
# Закрываем курсор
cursor.close()
conn.close()
print("Соединение с PostgreSQL закрыто")
# Определяем столбцы
columns = ("proces_1l", "power_main_1l", "concentrate_basic_1l", "tails_basic_1l", "food_1cleaning",
           "tails_1cleaning_1l", "food_2cleaning", "concentrate_3cleaning", "tailings", "extraction_1l",
           "cleaning_1", "extraction_technological", "_301_1_solid", "_303_solid", "_306_solid", "_309_solid",
           "_402_solid", "_301_concentration_ph", "_303_concentration_ph", "_306_concentration_ph",
           "Hydro243_flow_volume", "Hydro243_density", "Hydro243_pressure", "Mill_244_circulation",
           "Hydro261_flow_volume", "Hydro261_density", "Circularia305", "SP4_140mn", "SP4_74mn", "SP4_45mn", "SP4_25mn",
           "SP4_15mn", "SP6_140mn", "SP6_74mn", "SP6_45mn", "SP6_25mn", "SP6_15mn", "filter406", "release_Cu",
           "milk_of_lime",
           "sodium_sulfide_301_1_1", "sodium_sulfide_301_1", "sodium_sulfide_303", "xanthate_301_1", "xanthate_301_1_2",
           "xanthate_301_1_3", "xanthate_301_1_4", "xanthate_301_1_5", "aeroflot_301_1", "aeroflot_301_1_3and4",
           "aeroflot_303_1_5and6", "mibk_301_1_1", "liquid_glass_306", "liquid_glass_220_1", "_240and301_1",
           "flocculant",
           "lump_lime", "oil_pine_301_1", "oil_pine_243", "kmc_sump_260", "kmc_sump_240", "lump_lime_602",
           "SP7", "SP11A", "SP12A", "SP13", "id")

tree = ttk.Treeview(frame1, columns=columns, show="headings")

# Определяем заголовки
tree.heading("proces_1l", text="Переработка")
tree.heading("power_main_1l", text="Пит.осн.фл.")
tree.heading("concentrate_basic_1l", text="Концентр.осн.фл.")
tree.heading("tails_basic_1l", text="Хвосты.осн.фл.")
tree.heading("food_1cleaning", text="Питание.1переч.")
tree.heading("tails_1cleaning_1l", text="Хвосты.1пер.")
tree.heading("food_2cleaning", text="Питание.2переч.")
tree.heading("concentrate_3cleaning", text="Концентрат.3переч.")
tree.heading("tailings", text="Отвальн.хвосты")
tree.heading("extraction_1l", text="Извлечение.осн.фл.")
tree.heading("cleaning_1", text="Извлечение.1переч.")
tree.heading("extraction_technological", text="Техн.извлеч.")
tree.heading("_301_1_solid", text="Содерж.тв.301.1.1")
tree.heading("_303_solid", text="Содерж.тв.303")
tree.heading("_306_solid", text="Содерж.тв.306.1")
tree.heading("_309_solid", text="Содерж.тв.309.1")
tree.heading("_402_solid", text="Содерж.тв.402")
tree.heading("_301_concentration_ph", text="pH.301.1")
tree.heading("_303_concentration_ph", text="pH.303.1")
tree.heading("_306_concentration_ph", text="pH.306")
tree.heading("Hydro243_flow_volume", text="Расх.гидро.243")
tree.heading("Hydro243_density", text="Плотн.гидро.243")
tree.heading("Hydro243_pressure", text="Давл.гидро.243")
tree.heading("Mill_244_circulation", text="Мельн.244")
tree.heading("Hydro261_flow_volume", text="Расх.гидро.261")
tree.heading("Hydro261_density", text="Плотн.гидро.261")
tree.heading("Circularia305", text="Расх.циркуляц.")
tree.heading("SP4_140mn", text="Гранул.SP4+140µm")
tree.heading("SP4_74mn", text="Гранул.SP4+74µm")
tree.heading("SP4_45mn", text="Гранул.SP4+45µm")
tree.heading("SP4_25mn", text="Гранул.SP4+25µm")
tree.heading("SP4_15mn", text="Гранул.SP4+15µm")
tree.heading("SP6_140mn", text="Гранул.SP6+140µm")
tree.heading("SP6_74mn", text="Гранул.SP6+74µm")
tree.heading("SP6_45mn", text="Гранул.SP6+45µm")
tree.heading("SP6_25mn", text="Гранул.SP6+25µm")
tree.heading("SP6_15mn", text="Гранул.SP6+15µm")
tree.heading("filter406", text="Прес.фильтр.406")
tree.heading("release_Cu", text="ВыпускCu")
tree.heading("milk_of_lime", text="Изв.молоко.240зум.) ")
tree.heading("sodium_sulfide_301_1_1", text="Серн.натрий.301.1.1")
tree.heading("sodium_sulfide_301_1", text="Серн.натрий.301.1")
tree.heading("sodium_sulfide_303", text="Серн.натрий.303.1")
tree.heading("xanthate_301_1", text="Ксантог.301.1")
tree.heading("xanthate_301_1_2", text="Ксантог.301.1.2")
tree.heading("xanthate_301_1_3", text="Ксантог.301.1.3")
tree.heading("xanthate_301_1_4", text="Ксантог.301.1.4")
tree.heading("xanthate_301_1_5", text="Ксантог.301.1.5")
tree.heading("aeroflot_301_1", text="Аэрофлот.301.1")
tree.heading("aeroflot_301_1_3and4", text="Аэрофлот.301.3-4")
tree.heading("aeroflot_303_1_5and6", text="Аэрофлот.301.5-6")
tree.heading("mibk_301_1_1", text="МИБК 301.1.1")
tree.heading("liquid_glass_306", text="Жидк.стекл.306")
tree.heading("liquid_glass_220_1", text="Жидк.стекл.220.1")
tree.heading("_240and301_1", text=" 240.через.301.1")
tree.heading("flocculant", text="Флокулянт.вода")
tree.heading("lump_lime", text="Известь.комовая")
tree.heading("oil_pine_301_1", text="Сосн.масло.301.1")
tree.heading("oil_pine_243", text="Сосн.масло.243")
tree.heading("kmc_sump_260", text="КМЦ.зумпф.260")
tree.heading("kmc_sump_240", text="КМЦ.зумпф.240")
tree.heading("lump_lime_602", text="Изв.ком.602")
tree.heading("SP7", text="SP7.концент.золото")
tree.heading("SP11A", text="SP11A.конц.ВПК")
tree.heading("SP12A", text="SP12A.пит.осн.фл.")
tree.heading("SP13", text="SP13.хв.2.пер.")
tree.heading("id", text="Номер.строки")

# Выравниваем столбцы
for i in range(1, 68):
    tree.column("#" + str(i), stretch=NO, width=130)

# Добавляем данные
for person in ris_copper_primary_sulfides:
    tree.insert("", END, values=person)

# Добавляем полосу прокрутки(вертикальную)
scrollbar1 = Scrollbar(tree, orient=VERTICAL, width=25)
scrollbar1.pack(side=RIGHT, fill=Y)
scrollbar1.config(command=tree.yview)

# Добавляем полосу прокрутки(горизонтальную)
scrollbar2 = Scrollbar(tree, orient=HORIZONTAL, width=25)
scrollbar2.pack(side=BOTTOM, fill=X)
scrollbar2.config(command=tree.xview)

# Прикрепление бегунка к визуальному окну
tree.config(yscrollcommand=scrollbar1, xscrollcommand=scrollbar2)
tree.pack(expand=True, side=LEFT, fill=BOTH)
# Запустить tkinter
# root.mainloop()

# ИМПОРТ ИЗ БД ПО СТРОКАМ
# Получаем все данные из таблицы tbl_copper_primary_sulfides, записанной в БД MGOK_1
# Данные выйдут в виде одной строки
# Устанавливаем соединение
conn = psycopg2.connect(database="MGOK_1", user="postgres", password="Leonova2001", host="localhost", port="5432")
# Задаём курсор
cursor = conn.cursor()
# Получаем все данные из таблицы tbl_copper_primary_sulfides
# Столбики от 0 до 68, где 68 - это id
cursor.execute(queries.qSelectDiff1_1)
for tbl_copper_primary_sulfides in cursor:
    print(f"{tbl_copper_primary_sulfides[0]} - {tbl_copper_primary_sulfides[1]} - {tbl_copper_primary_sulfides[2]} - "
          f"{tbl_copper_primary_sulfides[3]} - {tbl_copper_primary_sulfides[4]} - {tbl_copper_primary_sulfides[5]} - "
          f"{tbl_copper_primary_sulfides[6]} - {tbl_copper_primary_sulfides[7]} - {tbl_copper_primary_sulfides[8]} - "
          f"{tbl_copper_primary_sulfides[9]} - {tbl_copper_primary_sulfides[10]} - {tbl_copper_primary_sulfides[11]} - "
          f"{tbl_copper_primary_sulfides[12]} - {tbl_copper_primary_sulfides[13]} - {tbl_copper_primary_sulfides[14]} - "
          f"{tbl_copper_primary_sulfides[15]} - {tbl_copper_primary_sulfides[16]} - {tbl_copper_primary_sulfides[17]} - "
          f"{tbl_copper_primary_sulfides[18]} - {tbl_copper_primary_sulfides[19]} - {tbl_copper_primary_sulfides[20]} - "
          f"{tbl_copper_primary_sulfides[21]} - {tbl_copper_primary_sulfides[22]} - {tbl_copper_primary_sulfides[23]} - "
          f"{tbl_copper_primary_sulfides[24]} - {tbl_copper_primary_sulfides[25]} - {tbl_copper_primary_sulfides[26]} - "
          f"{tbl_copper_primary_sulfides[27]} - {tbl_copper_primary_sulfides[28]} - {tbl_copper_primary_sulfides[29]} - "
          f"{tbl_copper_primary_sulfides[30]} - {tbl_copper_primary_sulfides[31]} - {tbl_copper_primary_sulfides[32]} - "
          f"{tbl_copper_primary_sulfides[33]} - {tbl_copper_primary_sulfides[34]} - {tbl_copper_primary_sulfides[35]} - "
          f"{tbl_copper_primary_sulfides[36]} - {tbl_copper_primary_sulfides[37]} - {tbl_copper_primary_sulfides[38]} - "
          f"{tbl_copper_primary_sulfides[39]} - {tbl_copper_primary_sulfides[40]} - {tbl_copper_primary_sulfides[41]} - "
          f"{tbl_copper_primary_sulfides[42]} - {tbl_copper_primary_sulfides[43]} - {tbl_copper_primary_sulfides[44]} - "
          f"{tbl_copper_primary_sulfides[45]} - {tbl_copper_primary_sulfides[46]} - {tbl_copper_primary_sulfides[47]} - "
          f"{tbl_copper_primary_sulfides[48]} - {tbl_copper_primary_sulfides[49]} - {tbl_copper_primary_sulfides[50]} - "
          f"{tbl_copper_primary_sulfides[51]} - {tbl_copper_primary_sulfides[52]} - {tbl_copper_primary_sulfides[53]} - "
          f"{tbl_copper_primary_sulfides[54]} - {tbl_copper_primary_sulfides[55]} - {tbl_copper_primary_sulfides[56]} - "
          f"{tbl_copper_primary_sulfides[57]} - {tbl_copper_primary_sulfides[58]} - {tbl_copper_primary_sulfides[59]} - "
          f"{tbl_copper_primary_sulfides[60]} - {tbl_copper_primary_sulfides[61]} - {tbl_copper_primary_sulfides[62]} - "
          f"{tbl_copper_primary_sulfides[63]} - {tbl_copper_primary_sulfides[64]} - {tbl_copper_primary_sulfides[65]} - "
          f"{tbl_copper_primary_sulfides[66]}"
          )
# Закрываем курсор
cursor.close()
conn.close()
print("Соединение с PostgreSQL закрыто")

# time.sleep(5.5)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 2 ТАБЛИЦА
# ОПРЕДЕЛЯЕМ ДАННЫЕ ДЛЯ ОТОБРАЖЕНИЯ В ВИЗУАЛЕ
# Устанавливаем соединение с pgSQL
conn = psycopg2.connect(database="MGOK_1", user="postgres", password="Leonova2001", host="localhost", port="5432")
# Задаём курсор
cursor = conn.cursor()
# Получаем все данные из таблицы tbl_copper_secondary_sulfides
# Столбики от 0 до 68, где 68 - это id
# Вводим запрос в БД на выборку лучшего реагентного режима
cursor.execute(queries.qSelectAll2_1)
# Присваиваем визуальному отображению
ris_copper_secondary_sulfides = cursor.fetchall()

# Закрываем курсор
cursor.close()
conn.close()
print("Соединение с PostgreSQL закрыто")
# # Определяем столбцы
columns2 = ("proces_1l", "power_main_1l", "concentrate_basic_1l", "tails_basic_1l", "food_1cleaning",
            "tails_1cleaning_1l", "food_2cleaning", "concentrate_3cleaning", "tailings", "extraction_1l",
            "cleaning_1", "extraction_technological", "_301_1_solid", "_303_solid", "_306_solid", "_309_solid",
            "_402_solid", "_301_concentration_ph", "_303_concentration_ph", "_306_concentration_ph",
            "Hydro243_flow_volume", "Hydro243_density", "Hydro243_pressure", "Mill_244_circulation",
            "Hydro261_flow_volume", "Hydro261_density", "Circularia305", "SP4_140mn", "SP4_74mn", "SP4_45mn",
            "SP4_25mn",
            "SP4_15mn", "SP6_140mn", "SP6_74mn", "SP6_45mn", "SP6_25mn", "SP6_15mn", "filter406", "release_Cu",
            "milk_of_lime",
            "sodium_sulfide_301_1_1", "sodium_sulfide_301_1", "sodium_sulfide_303", "xanthate_301_1",
            "xanthate_301_1_2",
            "xanthate_301_1_3", "xanthate_301_1_4", "xanthate_301_1_5", "aeroflot_301_1", "aeroflot_301_1_3and4",
            "aeroflot_303_1_5and6", "mibk_301_1_1", "liquid_glass_306", "liquid_glass_220_1", "_240and301_1",
            "flocculant",
            "lump_lime", "oil_pine_301_1", "oil_pine_243", "kmc_sump_260", "kmc_sump_240", "lump_lime_602",
            "SP7", "SP11A", "SP12A", "SP13", "id")

tree = ttk.Treeview(frame2, columns=columns2, show="headings")
#
# # Определяем заголовки
tree.heading("proces_1l", text="Переработка")
tree.heading("power_main_1l", text="Пит.осн.фл.")
tree.heading("concentrate_basic_1l", text="Концентр.осн.фл.")
tree.heading("tails_basic_1l", text="Хвосты.осн.фл.")
tree.heading("food_1cleaning", text="Питание.1переч.")
tree.heading("tails_1cleaning_1l", text="Хвосты.1пер.")
tree.heading("food_2cleaning", text="Питание.2переч.")
tree.heading("concentrate_3cleaning", text="Концентрат.3переч.")
tree.heading("tailings", text="Отвальн.хвосты")
tree.heading("extraction_1l", text="Извлечение.осн.фл.")
tree.heading("cleaning_1", text="Извлечение.1переч.")
tree.heading("extraction_technological", text="Техн.извлеч.")
tree.heading("_301_1_solid", text="Содерж.тв.301.1.1")
tree.heading("_303_solid", text="Содерж.тв.303")
tree.heading("_306_solid", text="Содерж.тв.306.1")
tree.heading("_309_solid", text="Содерж.тв.309.1")
tree.heading("_402_solid", text="Содерж.тв.402")
tree.heading("_301_concentration_ph", text="pH.301.1")
tree.heading("_303_concentration_ph", text="pH.303.1")
tree.heading("_306_concentration_ph", text="pH.306")
tree.heading("Hydro243_flow_volume", text="Расх.гидро.243")
tree.heading("Hydro243_density", text="Плотн.гидро.243")
tree.heading("Hydro243_pressure", text="Давл.гидро.243")
tree.heading("Mill_244_circulation", text="Мельн.244")
tree.heading("Hydro261_flow_volume", text="Расх.гидро.261")
tree.heading("Hydro261_density", text="Плотн.гидро.261")
tree.heading("Circularia305", text="Расх.циркуляц.")
tree.heading("SP4_140mn", text="Гранул.SP4+140µm")
tree.heading("SP4_74mn", text="Гранул.SP4+74µm")
tree.heading("SP4_45mn", text="Гранул.SP4+45µm")
tree.heading("SP4_25mn", text="Гранул.SP4+25µm")
tree.heading("SP4_15mn", text="Гранул.SP4+15µm")
tree.heading("SP6_140mn", text="Гранул.SP6+140µm")
tree.heading("SP6_74mn", text="Гранул.SP6+74µm")
tree.heading("SP6_45mn", text="Гранул.SP6+45µm")
tree.heading("SP6_25mn", text="Гранул.SP6+25µm")
tree.heading("SP6_15mn", text="Гранул.SP6+15µm")
tree.heading("filter406", text="Прес.фильтр.406")
tree.heading("release_Cu", text="ВыпускCu")
tree.heading("milk_of_lime", text="Изв.молоко.240зум.) ")
tree.heading("sodium_sulfide_301_1_1", text="Серн.натрий.301.1.1")
tree.heading("sodium_sulfide_301_1", text="Серн.натрий.301.1")
tree.heading("sodium_sulfide_303", text="Серн.натрий.303.1")
tree.heading("xanthate_301_1", text="Ксантог.301.1")
tree.heading("xanthate_301_1_2", text="Ксантог.301.1.2")
tree.heading("xanthate_301_1_3", text="Ксантог.301.1.3")
tree.heading("xanthate_301_1_4", text="Ксантог.301.1.4")
tree.heading("xanthate_301_1_5", text="Ксантог.301.1.5")
tree.heading("aeroflot_301_1", text="Аэрофлот.301.1")
tree.heading("aeroflot_301_1_3and4", text="Аэрофлот.301.3-4")
tree.heading("aeroflot_303_1_5and6", text="Аэрофлот.301.5-6")
tree.heading("mibk_301_1_1", text="МИБК 301.1.1")
tree.heading("liquid_glass_306", text="Жидк.стекл.306")
tree.heading("liquid_glass_220_1", text="Жидк.стекл.220.1")
tree.heading("_240and301_1", text=" 240.через.301.1")
tree.heading("flocculant", text="Флокулянт.вода")
tree.heading("lump_lime", text="Известь.комовая")
tree.heading("oil_pine_301_1", text="Сосн.масло.301.1")
tree.heading("oil_pine_243", text="Сосн.масло.243")
tree.heading("kmc_sump_260", text="КМЦ.зумпф.260")
tree.heading("kmc_sump_240", text="КМЦ.зумпф.240")
tree.heading("lump_lime_602", text="Изв.ком.602")
tree.heading("SP7", text="SP7.концент.золото")
tree.heading("SP11A", text="SP11A.конц.ВПК")
tree.heading("SP12A", text="SP12A.пит.осн.фл.")
tree.heading("SP13", text="SP13.хв.2.пер.")
tree.heading("id", text="Номер.строки")
#
# # Выравниваем столбцы
for i in range(1, 68):
    tree.column("#" + str(i), stretch=NO, width=130)
#
for person in ris_copper_secondary_sulfides:
    tree.insert("", END, values=person)
#
# # Добавляем полосу прокрутки(вертикальную)
scrollbar2_1 = Scrollbar(tree, orient=VERTICAL, width=25)
scrollbar2_1.pack(side=RIGHT, fill=Y)
scrollbar2_1.config(command=tree.yview)
#
# # Добавляем полосу прокрутки(горизонтальную)
scrollbar2_2 = Scrollbar(tree, orient=HORIZONTAL, width=25)
scrollbar2_2.pack(side=BOTTOM, fill=X)
scrollbar2_2.config(command=tree.xview)
#
# # Прикрепление бегунка к визуальному окну
tree.config(yscrollcommand=scrollbar2_1, xscrollcommand=scrollbar2_2)
tree.pack(expand=True, side=LEFT, fill=BOTH)
# # Запустить tkinter
root.mainloop()
#
# ИМПОРТ ИЗ БД ПО СТРОКАМ
# Получаем все данные из таблицы tbl_copper_primary_sulfides, записанной в БД MGOK_1
# Данные выйдут в виде одной строки
# Устанавливаем соединение
conn = psycopg2.connect(database="MGOK_1", user="postgres", password="Leonova2001", host="localhost", port="5432")
# Задаём курсор
cursor = conn.cursor()
# Получаем все данные из таблицы tbl_copper_secondary_sulfides
# Столбики от 0 до 66, где 66 - это id
cursor.execute(queries.qSelectAll2_1)
# for tbl_copper_secondary_sulfides in cursor:
#     print(f"{tbl_copper_secondary_sulfides[0]} - {tbl_copper_secondary_sulfides[1]} - {tbl_copper_secondary_sulfides[2]} - "
#           f"{tbl_copper_secondary_sulfides[3]} - {tbl_copper_secondary_sulfides[4]} - {tbl_copper_secondary_sulfides[5]} - "
#           f"{tbl_copper_secondary_sulfides[6]} - {tbl_copper_secondary_sulfides[7]} - {tbl_copper_secondary_sulfides[8]} - "
#           f"{tbl_copper_secondary_sulfides[9]} - {tbl_copper_secondary_sulfides[10]} - {tbl_copper_secondary_sulfides[11]} - "
#           f"{tbl_copper_secondary_sulfides[12]} - {tbl_copper_secondary_sulfides[13]} - {tbl_copper_secondary_sulfides[14]} - "
#           f"{tbl_copper_secondary_sulfides[15]} - {tbl_copper_secondary_sulfides[16]} - {tbl_copper_secondary_sulfides[17]} - "
#           f"{tbl_copper_secondary_sulfides[18]} - {tbl_copper_secondary_sulfides[19]} - {tbl_copper_secondary_sulfides[20]} - "
#           f"{tbl_copper_secondary_sulfides[21]} - {tbl_copper_secondary_sulfides[22]} - {tbl_copper_secondary_sulfides[23]} - "
#           f"{tbl_copper_secondary_sulfides[24]} - {tbl_copper_secondary_sulfides[25]} - {tbl_copper_secondary_sulfides[26]} - "
#           f"{tbl_copper_secondary_sulfides[27]} - {tbl_copper_secondary_sulfides[28]} - {tbl_copper_secondary_sulfides[29]} - "
#           f"{tbl_copper_secondary_sulfides[30]} - {tbl_copper_secondary_sulfides[31]} - {tbl_copper_secondary_sulfides[32]} - "
#           f"{tbl_copper_secondary_sulfides[33]} - {tbl_copper_secondary_sulfides[34]} - {tbl_copper_secondary_sulfides[35]} - "
#           f"{tbl_copper_secondary_sulfides[36]} - {tbl_copper_secondary_sulfides[37]} - {tbl_copper_secondary_sulfides[38]} - "
#           f"{tbl_copper_secondary_sulfides[39]} - {tbl_copper_secondary_sulfides[40]} - {tbl_copper_secondary_sulfides[41]} - "
#           f"{tbl_copper_secondary_sulfides[42]} - {tbl_copper_secondary_sulfides[43]} - {tbl_copper_secondary_sulfides[44]} - "
#           f"{tbl_copper_secondary_sulfides[45]} - {tbl_copper_secondary_sulfides[46]} - {tbl_copper_secondary_sulfides[47]} - "
#           f"{tbl_copper_secondary_sulfides[48]} - {tbl_copper_secondary_sulfides[49]} - {tbl_copper_secondary_sulfides[50]} - "
#           f"{tbl_copper_secondary_sulfides[51]} - {tbl_copper_secondary_sulfides[52]} - {tbl_copper_secondary_sulfides[53]} - "
#           f"{tbl_copper_secondary_sulfides[54]} - {tbl_copper_secondary_sulfides[55]} - {tbl_copper_secondary_sulfides[56]} - "
#           f"{tbl_copper_secondary_sulfides[57]} - {tbl_copper_secondary_sulfides[58]} - {tbl_copper_secondary_sulfides[59]} - "
#           f"{tbl_copper_secondary_sulfides[60]} - {tbl_copper_secondary_sulfides[61]} - {tbl_copper_secondary_sulfides[62]} - "
#           f"{tbl_copper_secondary_sulfides[63]} - {tbl_copper_secondary_sulfides[64]} - {tbl_copper_secondary_sulfides[65]} - "
#           f"{tbl_copper_secondary_sulfides[66]}"
#           )
# Закрываем курсор
cursor.close()
conn.close()
print("Соединение с PostgreSQL закрыто")

# ВВЕДЕНИЕ ПЕРЕМЕННЫХ ДЛЯ SQL ЗАПОРОСА В БД
# Ввод запрашивается и сохраняется в переменной
# Название переменных не имеет никакого отношения к коду выше, связанному с шапкой таблицы SQL
py_sodium_sulfide_301_1_1 = input("Введите текущее значение подачи Сернистого натрия в приёмный карман 301.1.1: ")
py_sodium_sulfide_301_1 = input("Введите текущее значение подачи Сернистого натрия в приёмный карман 301.1.2: ")
text3 = input("Введите текущее значение подачи Сернистого натрия в приёмный карман 303.1: ")
text4 = input("Введите текущее значение подачи Ксантогената в приёмный карман 303.1: ")
text5 = input("Введите текущее значение подачи Ксантогената в приёмный карман 301.1.2: ")
text6 = input("Введите текущее значение подачи Ксантогената в приёмный карман 301.1.3: ")
text7 = input("Введите текущее значение подачи Ксантогената в приёмный карман 301.1.4: ")
text8 = input("Введите текущее значение подачи Ксантогената в приёмный карман 301.1.5: ")
text9 = input("Введите текущее значение подачи Аэрофлота в приёмный карман 301.1: ")
text10 = input("Введите текущее значение подачи Аэрофлота в приёмный карман 301.1.3-4: ")
text11 = input("Введите текущее значение подачи Аэрофлота в приёмный карман 301.1.5-6: ")
text12 = input("Введите текущее значение подачи МИБК в приёмный карман 301.1.1: ")
text13 = input("Введите текущее значение подачи Жидкого стекла в приёмный карман 306: ")
text14 = input("Введите текущее значение подачи Жидкого стекла в приёмный карман 220.1: ")
text15 = input("Введите текущее значение подачи 240 через желоб 301.1:")
text16 = input("Введите текущее значение подачи Флокулянта в приёмный карман 301.1.5: ")
text17 = input("Введите текущее значение подачи Извести комовой по 1 линии: ")
text18 = input("Введите текущее значение подачи Соснового масла 301.1: ")
text19 = input("Введите текущее значение подачи Соснового масла 243: ")
text20 = input("Введите текущее значение подачи КМЦ в зумпфе 260: ")
text21 = input("Введите текущее значение подачи КМЦ в зумпфе 240: ")
text22 = input("Введите текущее значение подачи Извести комовой в конвейере 602: ")

# py_sodium_sulfide_303 = text3
# py_xanthate_301_1 = text4
# py_xanthate_301_1_2 = text5
# py_xanthate_301_1_3 = text6
# py_xanthate_301_1_4 = text7
# py_xanthate_301_1_5 = text8
# py_aeroflot_301_1 = text9
# py_aeroflot_301_1_3and4 = text10
# py_aeroflot_303_1_5and6 = text11
# py_mibk_301_1_1 = text12
# py_liquid_glass_306 = text13
# py_liquid_glass_220_1 = text14
# py_240and301_1 = text15
# py_flocculant = text16
# py_lump_lime = text17
# py_oil_pine_301_1 = text18
# py_oil_pine_243 = text19
# py_kmc_sump_260 = text20
# py_kmc_sump_240 = text21
# py_lump_lime_602 = text22

print("ВЫ ВВЕЛИ: ")
# Преобразуем строку в целое число, функция float() используется вместо int(),
# для преобразования пользовательского ввода в десятичный формат.
peremennaya1 = float(py_sodium_sulfide_301_1_1)
# Выводим в консоль переменную
print("sodium_sulfide_301_1_1 = ", py_sodium_sulfide_301_1_1)
peremennaya2 = float(py_sodium_sulfide_301_1)
print("sodium_sulfide_301_1 = ", peremennaya2)

# peremennaya3 = float(text3)
# print("sodium_sulfide_303 = ", peremennaya3)
# peremennaya4 = float(text4)
# print("xanthate_301_1 = ", peremennaya4)
# peremennaya5 = float(text5)
# print("xanthate_301_1_2 = ", peremennaya5)
# peremennaya6 = float(text6)
# print("xanthate_301_1_3 = ", peremennaya6)
# peremennaya7 = float(text7)
# print("xanthate_301_1_4 = ", peremennaya7)
# peremennaya8 = float(text8)
# print("xanthate_301_1_5 = ", peremennaya8)
# peremennaya9 = float(text9)
# print("aeroflot_301_1 = ", peremennaya9)
# peremennaya10 = float(text10)
# print("aeroflot_301_1_3and4 = ", peremennaya10)
# peremennaya11 = float(text11)
# print("aeroflot_303_1_5and6 = ", peremennaya11)
# peremennaya12 = float(text12)
# print("mibk_301_1_1 = ", peremennaya12)
# peremennaya13 = float(text13)
# print("liquid_glass_306 = ", peremennaya13)
# peremennaya14 = float(text14)
# print("liquid_glass_220_1 = ", peremennaya14)
# peremennaya15 = float(text15)
# print("_240and301_1 = ", peremennaya15)
# peremennaya16 = float(text16)
# print("flocculant = ", peremennaya16)
# peremennaya17 = float(text17)
# print("lump_lime = ", peremennaya17)
# peremennaya18 = float(text18)
# print("oil_pine_301_1 = ", peremennaya18)
# peremennaya19 = float(text19)
# print("oil_pine_243 = ", peremennaya19)
# peremennaya20 = float(text20)
# print("kmc_sump_260 = ", peremennaya20)
# peremennaya21 = float(text21)
# print("kmc_sump_240 = ", peremennaya21)
# peremennaya22 = float(text22)
# print("lump_lime_602 = ", peremennaya22)

# Константы для диапазона числа
a1 = 5
a2 = 5
a3 = 5
a4 = 10
a5 = 10
a6 = 10
a7 = 10
a8 = 10
a9 = 5
a10 = 5
a11 = 5
a12 = 50
a13 = 50
a14 = 50
a15 = 50
a16 = 50
a17 = 50
a18 = 50
a19 = 50
a20 = 50
a21 = 50
a22 = 50

# Устанавливаем соединение
conn = psycopg2.connect(database="MGOK_1", user="postgres", password="Leonova2001", host="localhost", port="5432")
# Задаём курсор
cursor = conn.cursor()
# Получаем все данные из таблицы tbl_copper_secondary_sulfides
# Столбики от 0 до 66, где 66 - это id
cursor.execute(queries.qSelectDiff1_3, vars={'py_sodium_sulfide_301_1_1': py_sodium_sulfide_301_1_1, 'a1': a1})

diff = cursor.fetchall()
print("test: ", diff)

# Закрываем курсор
cursor.close()
conn.close()
print("Соединение с PostgreSQL закрыто")
