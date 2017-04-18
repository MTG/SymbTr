# -*- coding: utf-8 -*-
from symbtrdataextractor.reader.mu2 import Mu2Reader
from fileoperations.fileoperations import get_filenames_in_dir
import csv


def test_mu2_header():
    col_names = {2: u'Pay', 3: u'Payda', 4: u'Legato%', 5: u'Bas',
                 6: u'Çek', 7: u'Söz-1', 8: u'Söz-2'}

    num_columns = 10
    all_read_correctly = True
    all_headers_valid = True
    all_header_rows_valid = True
    all_num_columns_correct = True

    [mu2filepaths, mu2folders, mu2names] = get_mu2_filenames()

    for mf, mn in zip(mu2filepaths, mu2names):
        try:
            mu2_header, header_row, is_header_valid = Mu2Reader.read_header(
                mf, symbtr_name=mn)

            if not is_header_valid:
                all_headers_valid = False

            if not len(header_row) == num_columns:
                all_num_columns_correct = False
                print mn + ': Number of columns is different than 10!'

            for ii in range(0, len(col_names) + 3):
                if ii in [0, 1]:
                    try:
                        int(header_row[ii])
                    except ValueError:  # not int
                        all_header_rows_valid = False
                        print('{0:s}: {1:s}th column in the header row should '
                              'have been an integer!'.format(mn, str(ii)))
                elif ii == len(col_names) + 2:
                    try:
                        float(header_row[ii])
                    except ValueError:  # not float
                        all_header_rows_valid = False
                        print('{0:s}: {1:s}th column in the header row should '
                              'have been a float!'.format(mn, str(ii)))
                else:
                    if not header_row[ii] == col_names[ii]:
                        all_header_rows_valid = False
                        print(u'%s: %dth column in the header row should have '
                              u'been named "%s" instead of "%s"'
                              % (mn, ii, col_names[ii], header_row[ii]))

        except UnicodeEncodeError:
            all_read_correctly = False
            print(mn + ' unicode read error')

    assert all_read_correctly, 'Unicode errors'
    assert all_header_rows_valid, 'Invalid header rows'
    assert all_num_columns_correct, 'Incorrect number of columns'
    assert all_headers_valid, 'Invalid header values'

def test_mu2_num_cols():
    num_columns = 10

    [mu2filepaths, mu2folders, mu2names] = get_mu2_filenames()
    all_num_columns_correct = True

    for mf, mn in zip(mu2filepaths, mu2names):
        with open(mf, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            for ii, row in enumerate(reader):
                if not len(row) == num_columns:
                    print '{}: Row {:d} has {:d} columns'.format(
                        mn, ii, len(row))
                    all_num_columns_correct = False

    assert all_num_columns_correct, 'Incorrect number of columns'

def get_mu2_filenames():
    symbtr_mu2_folder = './mu2/'
    return get_filenames_in_dir(symbtr_mu2_folder, keyword='*.mu2')
