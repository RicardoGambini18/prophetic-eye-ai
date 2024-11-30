import random


def get_random_items(input_list: list, number_of_items=1):
  if (len(input_list) == 0 or number_of_items <= 0):
    return None

  final_number_of_items = number_of_items

  if number_of_items >= len(input_list):
    final_number_of_items = len(input_list)

  if (len(input_list) == 1 and final_number_of_items == 1):
    return input_list[0]

  if (final_number_of_items == 1):
    return input_list[random.randint(0, len(input_list) - 1)]

  if (final_number_of_items == len(input_list)):
    return input_list

  return random.sample(input_list, final_number_of_items)
