from symbtrdataextractor.dataextractor import DataExtractor
from fileoperations.fileoperations import get_filenames_in_dir


def test_txt_data():
    extractor = SymbTrDataExtractor(print_warnings=False)
    [txtfilepaths, txtfolders, txtnames] = get_txt_filenames()

    is_all_txt_data_valid = True
    for tf, tn in zip(txtfilepaths, txtnames):
        try:
            txtdata, is_txt_data_valid = extractor.extract(tf)
            is_all_txt_data_valid = is_txt_data_valid \
                if is_all_txt_data_valid else False
        except (RuntimeError, ValueError, KeyError, TypeError):
            print "Unspecified error in " + tn
            is_all_txt_data_valid = False

    assert is_all_txt_data_valid


def get_txt_filenames():
    symbtr_txt_folder = './txt/'
    return get_filenames_in_dir(symbtr_txt_folder, keyword='*.txt')
