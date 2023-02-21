# Запросы к БД

# ТАБЛИЦА 1
qSelectAll1_1 = """
SELECT * FROM tbl_copper_primary_sulfides;
"""

# qSelectDiff1_1 = """
# SELECT * FROM tbl_copper_primary_sulfides
# WHERE cleaning_1+extraction_1l-tailings >= 180
# ORDER BY cleaning_1+extraction_1l-tailings DESC LIMIT 3;
# """

qSelectDiff1_1 = "SELECT * FROM tbl_copper_primary_sulfides WHERE cleaning_1+extraction_1l-tailings >= 180 ORDER BY cleaning_1+extraction_1l-tailings DESC LIMIT 3;"

qSelectDiff1_2 = """
SELECT * FROM tbl_copper_primary_sulfides
WHERE milk_of_lime>=2500 and milk_of_lime<=2700 and "sodium_sulfide_301.1.1" >=400 
and "sodium_sulfide_301.1.1"<=500
ORDER BY extraction_1l DESC LIMIT 1;
# -- DESC LIMIT 1
# -- извлечение в приоритете, вместо чисел переменные на основе текущего реагентного режима
# -- реагентный решим выравнивается в течение 30-60 минут
"""

qSelectDiff1_3 = """
SELECT * FROM tbl_copper_primary_sulfides
WHERE "sodium_sulfide_301.1.1" >= %(py_sodium_sulfide_301_1_1)s - %(a1)s AND "sodium_sulfide_301.1.1" <= %(py_sodium_sulfide_301_1_1)s + %(a1)s
ORDER BY extraction_1l DESC LIMIT 1;
"""

qSelectDiff1_4 = """
SELECT * FROM tbl_copper_primary_sulfides;
"""

# ТАБЛИЦА 2
qSelectAll2_1 = """
SELECT * FROM tbl_copper_secondary_sulfides;
"""