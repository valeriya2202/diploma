# Запросы к БД

# ТАБЛИЦА 1
qSelectAll1_1 = """
SELECT * FROM tbl_copper_primary_sulfides;
"""

qSelectDiff1_1 = """
SELECT * FROM tbl_copper_primary_sulfides
WHERE cleaning_1+extraction_1l-tailings >= 180
ORDER BY cleaning_1+extraction_1l-tailings DESC LIMIT 3;
"""

qSelectDiff1_2 = """
SELECT * FROM tbl_copper_primary_sulfides
WHERE milk_of_lime>=2500 and milk_of_lime<=2700 and "sodium_sulfide_301.1.1" >=400 
and "sodium_sulfide_301.1.1"<=500
ORDER BY extraction_1l DESC LIMIT 1;
"""

qSelectDiff1_3 = """
SELECT * FROM tbl_copper_primary_sulfides
WHERE "sodium_sulfide_301.1.1" >= %(py_sodium_sulfide_301_1_1)s - %(a1)s
AND "sodium_sulfide_301.1.1" <= %(py_sodium_sulfide_301_1_1)s + %(a1)s

AND "sodium_sulfide_301.1" >= %(py_sodium_sulfide_301_1)s - %(a2)s
AND "sodium_sulfide_301.1" <= %(py_sodium_sulfide_301_1)s + %(a2)s

AND "sodium_sulfide_303" >= %(py_sodium_sulfide_303)s - %(a3)s
AND "sodium_sulfide_303" <= %(py_sodium_sulfide_303)s + %(a3)s

AND "xanthate_301.1" >= %(py_xanthate_301_1)s - %(a3)s
AND "xanthate_301.1" <= %(py_xanthate_301_1)s + %(a3)s

AND "xanthate_301.1.2" >= %(py_xanthate_301_1_2)s - %(a3)s
AND "xanthate_301.1.2" <= %(py_xanthate_301_1_2)s + %(a3)s

AND "xanthate_301.1.3" >= %(py_xanthate_301_1_3)s - %(a3)s
AND "xanthate_301.1.3" <= %(py_xanthate_301_1_3)s + %(a3)s

AND "xanthate_301.1.4" >= %(py_xanthate_301_1_4)s - %(a3)s
AND "xanthate_301.1.4" <= %(py_xanthate_301_1_4)s + %(a3)s

AND "xanthate_301.1.5" >= %(py_xanthate_301_1_5)s - %(a3)s
AND "xanthate_301.1.5" <= %(py_xanthate_301_1_5)s + %(a3)s

AND "aeroflot_301.1" >= %(py_aeroflot_301_1)s - %(a3)s
AND "aeroflot_301.1" <= %(py_aeroflot_301_1)s + %(a3)s

AND "aeroflot_301.1.3-4" >= %(py_aeroflot_301_1_3and4)s - %(a3)s
AND "aeroflot_301.1.3-4" <= %(py_aeroflot_301_1_3and4)s + %(a3)s

AND "aeroflot_303.1.5-6" >= %(py_aeroflot_303_1_5and6)s - %(a3)s
AND "aeroflot_303.1.5-6" <= %(py_aeroflot_303_1_5and6)s + %(a3)s

AND "mibk_301.1.1" >= %(py_mibk_301_1_1)s - %(a3)s
AND "mibk_301.1.1" <= %(py_mibk_301_1_1)s + %(a3)s

AND "liquid_glass_306" >= %(py_liquid_glass_306)s - %(a3)s
AND "liquid_glass_306" <= %(py_liquid_glass_306)s + %(a3)s

AND "liquid_glass_220.1" >= %(py_liquid_glass_220_1)s - %(a3)s
AND "liquid_glass_220.1" <= %(py_liquid_glass_220_1)s + %(a3)s

AND "240and301_1" >= %(py_240and301_1)s - %(a3)s
AND "240and301_1" <= %(py_240and301_1)s + %(a3)s

AND "flocculant" >= %(py_flocculant)s - %(a3)s
AND "flocculant" <= %(py_flocculant)s + %(a3)s

AND "lump_lime" >= %(py_lump_lime)s - %(a3)s
AND "lump_lime" <= %(py_lump_lime)s + %(a3)s

AND "oil_pine_301.1" >= %(py_oil_pine_301_1)s - %(a3)s
AND "oil_pine_301.1" <= %(py_oil_pine_301_1)s + %(a3)s

AND "oil_pine_243" >= %(py_oil_pine_243)s - %(a3)s
AND "oil_pine_243" <= %(py_oil_pine_243)s + %(a3)s

AND "kmc_sump_260" >= %(py_kmc_sump_260)s - %(a3)s
AND "kmc_sump_260" <= %(py_kmc_sump_260)s + %(a3)s

AND "kmc_sump_240" >= %(py_kmc_sump_240)s - %(a3)s
AND "kmc_sump_240" <= %(py_kmc_sump_240)s + %(a3)s

AND "lump_lime_602" >= %(py_lump_lime_602)s - %(a3)s
AND "lump_lime_602" <= %(py_lump_lime_602)s + %(a3)s

ORDER BY extraction_1l DESC LIMIT 1;
"""

qSelectDiff1_4 = """
SELECT * FROM tbl_copper_primary_sulfides;
"""

# ТАБЛИЦА 2
qSelectAll2_1 = """
SELECT * FROM tbl_copper_secondary_sulfides;
"""

# ТАБЛИЦА 3
qSelectAll3_1 = """
SELECT * FROM tbl_copper_water_soluble;
"""

# ТАБЛИЦА 4
qSelectAll4_1 = """
SELECT * FROM tbl_copper_oxidized;
"""

# ТАБЛИЦА 5
qSelectAll5_1 = """
SELECT * FROM tbl_copper_total;
"""