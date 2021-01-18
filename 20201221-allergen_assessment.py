# --- Day 21: Allergen Assessment ---
# You reach the train's last stop and the closest you can get to your vacation island without getting wet. There aren't even any boats here, but nothing can stop you now: you build a raft. You just need a few days' worth of food for your journey.
#
# You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are listed in a language you do understand. You should be able to use this information to determine which ingredient contains which allergen and work out which foods are safe to take with you on your trip.
#
# You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that food's ingredients list followed by some or all of the allergens the food contains.
#
# Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. Allergens aren't always marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list), the ingredient that contains each listed allergen will be somewhere in the corresponding ingredients list. However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present: maybe they forgot to label it, or maybe it was labeled in a language you don't know.
#
# For example, consider the following list of foods:
#
# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)
# The first food in the list has four ingredients (written in a language you don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food might contain other allergens, a few allergens the food definitely contains are listed afterward: dairy and fish.
#
# The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your list. In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. Counting the number of times any of these ingredients appear in any ingredients list produces 5: they all appear once each except sbzzf, which appears twice.
#
# Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of those ingredients appear?
#
# Your puzzle answer was 2461.
#
# --- Part Two ---
# Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient contains which allergen.
#
# In the above example:
#
# mxmxvkd contains dairy.
# sqjhc contains fish.
# fvjkl contains soy.
# Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical dangerous ingredient list. (There should not be any spaces in your canonical dangerous ingredient list.) In the above example, this would be mxmxvkd,sqjhc,fvjkl.
#
# Time to stock your raft with supplies. What is your canonical dangerous ingredient list?
#
# Your puzzle answer was ltbj,nrfmm,pvhcsn,jxbnb,chpdjkf,jtqt,zzkq,jqnhd.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


from pprint import pprint


if __name__ == '__main__':

    files = ['20201221-example.txt', '20201221-input.txt']

    for file_name in files:
        print("\n****************************\n" + file_name)
        with open(file_name) as f:
            foods = f.readlines()

        ingredients_with_allergens = set()
        food_list = []

        all_ingredients = []
        all_allergens = []

        for i in range(len(foods)):
            food = foods[i].strip()
            allergens = set(food[food.find('(') + 1:-1].replace('contains', '').replace(' ', '').split(','))
            ingredients = set(food[:food.find('(')].split())
            #print("allergens: ", allergens)
            #print("ingredients: ", ingredients)
            all_ingredients += list(ingredients)
            all_allergens += list(allergens)
            food_list.append({'i': ingredients, 'a': allergens})

        #print("food_list:")
        #pprint(food_list)

        all_ingredients = set(all_ingredients)
        all_allergens = set(all_allergens)

        #print("all_ingredients ({}):".format(len(all_ingredients)))
        #pprint(all_ingredients)

        #print("all_allergens ({}):".format(len(all_allergens)))
        #pprint(all_allergens)

        allergens_only_mapped_to_single_food = []

        # Iterate food list
        for fi in range(len(food_list)):
            # Get allergens of food fi
            ai = food_list[fi].get('a')
            # Get ingredients of food fi
            ii = food_list[fi].get('i')
            # Intersection match count
            ai_intersection_match_count = 0
            ai_intersection_not_match_count = 0
            # Get food fj for comparison with fi
            for fj in range(len(food_list)):
                if fi != fj:
                    # Get allergens of food fj
                    aj = food_list[fj].get('a')
                    # Get ingredients of food fj
                    ij = food_list[fj].get('i')
                    # If food fi and food fj contain allergen
                    if ai.intersection(aj):
                        #print("Intersection of {} and {} allergens: {}".format(fi, fj, ai.intersection(aj)))
                        ai_intersection_match_count += 1
                        if ii.intersection(ij):
                            #print("Intersection of {} and {} ingredients: {}".format(fi, fj, ii.intersection(ij)))
                            for iwa in ii.intersection(ij):
                                ingredients_with_allergens.add(iwa)
                    else:
                        ai_intersection_not_match_count += 1
            # Allergen is only mapped to a single food since there was no intersection of allergens with other foods
            if ai_intersection_match_count == 0 and ai_intersection_not_match_count == len(food_list) -1:
                # Now check intersection of ingredients
                for fj in range(len(food_list)):
                    # Get ingredients of food fj
                    ij = food_list[fj].get('i')
                    if fi != fj:
                        if ii.intersection(ij):
                            #print("Intersection of {} and {} ingredients: {}".format(fi, fj, ii.intersection(ij)))
                            for iwa in ii.intersection(ij):
                                ingredients_with_allergens.add(iwa)

        #print("ingredients_with_allergens:")
        #pprint(ingredients_with_allergens)

        ingredients_without_allergens = [i for f in food_list for i in f.get('i') if i not in ingredients_with_allergens]
        #print("ingredients_without_allergens:")
        #pprint(ingredients_without_allergens)

        allergen_ingredient_dict = {}

        ingredients_with_allergens = set()
        for a in all_allergens:
            ingredient_sets = []
            for f in food_list:
                if a in f.get('a'):
                    ingredient_sets.append(f.get('i'))
            if len(ingredient_sets) > 1:
                ingredients_with_allergens.update(ingredient_sets[0].intersection(*ingredient_sets[1:]))
                intersection = ingredient_sets[0].intersection(*ingredient_sets[1:])
            else:
                ingredients_with_allergens.update(ingredient_sets[0])
                intersection = ingredient_sets[0]

            allergen_ingredient_dict[a] = intersection

        print("allergen_ingredient_dict:")
        pprint(allergen_ingredient_dict)

        ingredients_without_allergens_set = all_ingredients - ingredients_with_allergens

        print("ingredients_without_allergens_set: ", ingredients_without_allergens_set)
        print("len(ingredients_without_allergens_set): ", len(ingredients_without_allergens_set))

        print("ingredients_with_allergens: ", ingredients_with_allergens)
        print("len(ingredients_with_allergens): ", len(ingredients_with_allergens))

        ingredients_without_allergens = [i for f in food_list for i in f.get('i') if i in ingredients_without_allergens_set]
        #print("ingredients_without_allergens:")
        #pprint(ingredients_without_allergens)

        part_one = {}
        for i in ingredients_without_allergens:
            part_one[i] = part_one.get(i, 0) + 1

        print("Part One: ", sum(part_one.values()))

        mapped = 0
        while mapped < len(allergen_ingredient_dict):
            for ki, vi in allergen_ingredient_dict.items():
                if len(vi) == 1:
                    mapped += 1
                    for kj, vj in allergen_ingredient_dict.items():
                        if kj == ki:
                            continue
                        if vi.intersection(vj):
                            vj -= vi

        print(allergen_ingredient_dict)

        p2_str_list = ""
        for k in sorted(allergen_ingredient_dict.keys()):
            p2_str_list += str(allergen_ingredient_dict.get(k)).replace("{'", "").replace("'}","") + ","

        print("Part Two: ", p2_str_list[:-1])
