import eves
import combined_features as cf
import source_reader as src
import csv
import feature_selection as fs
import main_detection as md

def main():
    flag = True
    result = []
    #calculate all features
    for yy in range(3):

        elem_feat = [1] * 81

        #read list name
        list_name = read_name()

        #do feature extraction combined features from different placements
        prec_val, rec_val, f_score_val, temp_ct, temp_wt, temp_tt, tot_tt, place = md.main_detection(list_name, elem_feat)
        if flag:
            result.append([prec_val, rec_val, f_score_val, temp_ct, temp_wt, temp_tt, tot_tt, place])
            flag = False

        #do several feature selection techniques & get the new sub-features

        new_feat = fs.main_feat(list_name, yy)

        #re-calculate features together with the time for each placements
        prec_val_fin, rec_val_fin, f_score_fin, temp_ct_fin, temp_wt_fin, temp_tt_fin, tot_tt_fin, place_fin = md.main_detection(list_name, new_feat)
        result.append([prec_val_fin, rec_val_fin, f_score_fin, temp_ct_fin, temp_wt_fin, temp_tt_fin, tot_tt_fin, place_fin])
    #write result

    write_final_result(result)


def write_final_result(array):
    path = src.read_temp_fscore()
    out_file = open(path, "w")
    csv_writer = csv.writer(out_file, delimiter='\t')
    for line in array:
        csv_writer.writerow(line)
    out_file.close()




def read_seq(name, position):
    path = src.raw_source(name,position)
    x = []
    y = []
    z = []
    annot = []
    with open(path) as obj:
        for line in obj:
            raw_splitted = line.split()
            f_split = [float(i) for i in raw_splitted]
            x.append(f_split[0])
            y.append(f_split[1])
            z.append(f_split[2])
            annot.append(f_split[3])

    return x,y,z,annot

def read_name():
    name_list = []
    path = src.listname_path()

    with open(path) as obj_name:
        for line in obj_name:
            raw = line.split()
            name = raw[0]
            name_list.append(name)

    return name_list


if __name__ == '__main__':
    main()
