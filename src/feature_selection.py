from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif, f_regression
import source_reader as src


def main_feat(listname, yy):
    data, annot =  read_data(listname)
    k_value = len(data[0])/2

    if yy == 0:
        new_data = SelectKBest(f_classif, k = k_value)
    elif yy == 1:
        new_data = SelectKBest(chi2, k = k_value)
    else:
        tech = f_regression
        new_data = SelectKBest(f_regression, k = k_value)


    new_data.fit_transform(data, annot)
    selected_feat = new_data.get_support()
    new_selected = convert_elem(selected_feat)

    return new_selected


def convert_elem(selected):
    new_elem = []
    for line in selected:
        if line:
            new_elem.append(1)
        else:
            new_elem.append(0)

    return new_elem

def read_data(listname):
    data = []
    annot = []

    for name in listname:
        temp_feat, annot_name = read_seq(name)
        data.extend(temp_feat)
        annot.extend(annot_name)

    return data, annot

def read_seq(name):
    path = src.combined_path(name)
    annot = []
    instance = []
    with open(path) as obj:
        for line in obj:
            raw_splitted = line.split()
            f_split = [float(i) for i in raw_splitted]
            instance.append(f_split[: len(f_split)-1])
            annot.append(f_split[len(f_split)-1])

    return instance,annot
