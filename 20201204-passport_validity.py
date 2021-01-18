# --- Day 4: Passport Processing ---
# You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.
#
# It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.
#
# Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.
#
# The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:
#
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
# Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.
#
# Here is an example batch file containing four passports:
#
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
#
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
#
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm
#
# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).
#
# The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.
#
# The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.
#
# According to the above rules, your improved system would report 2 valid passports.
#
# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
#
# Your puzzle answer was 200.
#
# --- Part Two ---
# The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!
#
# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:
#
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
# Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:
#
# byr valid:   2002
# byr invalid: 2003
#
# hgt valid:   60in
# hgt valid:   190cm
# hgt invalid: 190in
# hgt invalid: 190
#
# hcl valid:   #123abc
# hcl invalid: #123abz
# hcl invalid: 123abc
#
# ecl valid:   brn
# ecl invalid: wat
#
# pid valid:   000000001
# pid invalid: 0123456789
# Here are some invalid passports:
#
# eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
#
# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946
#
# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
#
# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007
# Here are some valid passports:
#
# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f
#
# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
#
# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022
#
# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
# Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
#
# Your puzzle answer was 116.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


import re


def check_validity(passport, part):
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    if part == 1:
        if required_keys <= passport.keys():
            return True
    elif part == 2:
        #print("passport.keys(): ", passport.keys())
        #print("required_keys: ", required_keys)
        if not all(k in passport.keys() for k in required_keys):
            return False

        four_digit_regex_pattern = '^\d{4}$'

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        byr = regex_min_max_value_check(four_digit_regex_pattern, passport.get('byr'), 1920, 2002)
        #print("byr: ", byr)

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        iyr = regex_min_max_value_check(four_digit_regex_pattern, passport.get('iyr'), 2010, 2020)
        #print("iyr: ", iyr)

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        eyr = regex_min_max_value_check(four_digit_regex_pattern, passport.get('eyr'), 2020, 2030)
        #print("eyr: ", eyr)

        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        hgt_regex_pattern = '^(?:1[5-8][0-9]cm)|(?:19[0-3]cm)|(?:59in)|(?:6[0-9]in)|(?:7[0-6]in)$'
        if re.match(hgt_regex_pattern, passport.get('hgt')):
            hgt = True
        else:
            hgt = False
        #print("hgt: ", hgt)

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        hcl_regex_pattern = '^#[0-9a-f]{6}$'
        if re.match(hcl_regex_pattern, passport.get('hcl')):
            hcl = True
        else:
            hcl = False
        #print("hcl: ", hcl)

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        ecl_valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if passport.get('ecl') in ecl_valid:
            ecl = True
        else:
            ecl = False
        #print("ecl: ", ecl)

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        pid_regex_pattern = '^[0-9]{9}$'
        if re.match(pid_regex_pattern, passport.get('pid')):
            pid = True
        else:
            pid = False
        #print("pid: ", pid)

        # cid (Country ID) - ignored, missing or not.
        return byr and iyr and eyr and hgt and hcl and ecl and pid


def regex_min_max_value_check(regex, value, min, max):
    # Alternative:
    # if re.match(regex, value) and int(value) in range(min-1, max-1):
    if re.match(regex, value) and min <= int(value) <= max:
        return True
    else:
        return False


if __name__ == '__main__':

    files = ['20201204-example.txt', '20201204-input.txt']

    for file_name in files:
        print("\n" + file_name)
        with open(file_name) as f:
            lines = f.readlines()

        len_rows = len(lines)

        part_passport_list = []

        for part in range(1, 3):
            #print("part: ", part)
            passport_dict = {}
            passport_list = []
            row_count = 0
            while row_count < len_rows:
                #print("lines[row_count]: ", lines[row_count])
                row_content = lines[row_count].strip()
                #print("row_content: ", row_content)
                for i in row_content.split():
                    key = i.split(':')[0]
                    value = i.split(':')[1]
                    passport_dict[key] = value

                    #print("key: ", key)
                    #print("value: ", value)
                    #print("passport_dict: ", passport_dict)

                if row_content == "":
                    passport_dict['is_valid'] = check_validity(passport_dict, part)
                    passport_list.append(passport_dict)
                    passport_dict = {}

                    #print("passport_list: ", passport_list)
                    #print("passport_dict: ", passport_dict)

                #print("row_count: ", row_count)
                row_count += 1

            part_passport_list.append(passport_list)

        for part_count in range(len(part_passport_list)):
            valid_pp_count = 0
            for j in part_passport_list[part_count]:
                if j.get('is_valid'):
                    valid_pp_count += 1
            print("Part {} - valid_pp_count: {}".format(part_count+1, valid_pp_count))
