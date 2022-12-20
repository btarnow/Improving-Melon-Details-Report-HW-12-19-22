"""Print out all the melons in our inventory."""


from melons import melons

def print_all_melons(melons):
    for melon_name, attributes in melons.items():
        print(melon_name.upper())
    
        for attribute, value in attributes.items():
            print(f"{attribute}: {value}")

        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()

print_all_melons(melons)



##BELOW IS THE ORIGINAL PROVIDED CODE THAT WE NEED TO UPDATE TO IMPROVE PER HW DIRECTIONS:
##########################################################################################
# def print_melon(dictionary):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(name.uppper())
#     print(f"price: {")
#     print(f"seedless: ")
#     print(f'{name}s {have_or_have_not} seeds and are ${price}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])
