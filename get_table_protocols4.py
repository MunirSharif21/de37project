from cleaning_table_protocols3 import *
from normalisation_functions import *


"""
This file takes a clean table and hence applies normalisation
to it
"""


def applicants_address():
    df_app0 = clean_applicants()
    # extract address into a new table and attach applicant id to it
    df_app0, df_add0 = normalise(df_app0, ["city", "address", "postcode"],
                                 deletion=True, old_id=True, index="applicant_id")
    return df_app0, df_add0


def applicants_recruiter(df_app0):
    # extract recruiters into a new normalised table
    df_app0, df_rec0 = normalise(df_app0, ["invited_by"], deletion=False,
                                 new_id=True, index="invited_by")
    return df_app0, df_rec0


def candidates_scores_strengths(df_cand0):
    df_cand0, df_scores0 = normalise(df_cand0, ["tech_self_score"], deletion=True,
                                     old_id=True, index="applicant_id")
    df_cand0, df_stren0 = normalise(df_cand0, ["strengths"], deletion=True,
                                    old_id=True, index="applicant_id")
    df_cand0, df_weak0 = normalise(df_cand0, ["weaknesses"], deletion=True,
                                   old_id=True, index="applicant_id")
    # df_scores0 = split_up_column(df_scores0, "tech_self_score")
    # df_stren0 = split_up_column(df_stren0, "strengths")
    # df_weak0 = split_up_column(df_weak0, "weaknesses")
    return df_cand0, df_scores0, df_stren0, df_weak0


def candidates_academy(df_cand0):
    # print(df_cand0[:10])
    df_cand0, df_locations = normalise(df_cand0, ["Location"], deletion=True,
                                       new_id=True, index="Location")
    return df_cand0, df_locations


def get_tables_1():
    df_app, df_add = applicants_address()
    df_app, df_rec = applicants_recruiter(df_app)

    # print(df_app, df_rec, sep="\n")
    # lim = 7
    # print("Candidate Table")
    # print(df_json[:lim])
    # print("Tech Scores Table")
    # print(df_scores[:lim])
    # print("Strengths Table")
    # print(df_stren[:lim])
    # print("Weaknesses Table")
    # print(df_weak[:lim])
    return df_app, df_add, df_rec


def get_tables_2():
    df_json = clean_json()
    df_json, df_scores, df_stren, df_weak = candidates_scores_strengths(df_json)

    return df_json, df_scores, df_stren, df_weak


def get_tables_3():
    df_candidates = clean_candidates()
    df_candidates, df_locations = candidates_academy(df_candidates)
    # print(df_locations)

    return df_candidates, df_locations


def get_tables_4(force_refresh=False):
    df_academy = clean_academy(force_refresh)

    return df_academy

# MAIN

