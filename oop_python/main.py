from data import load,save
import utils

data = load()
data = utils.add_person(data,"asahina",20,"asahina@gmail.com","tokyo")
utils.display_neatly(data)
utils.display_sorted_by_age(data)
