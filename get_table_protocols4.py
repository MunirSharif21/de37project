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
    # now do extra processing on scores
    df_scores0 = split_up_column(df_scores0, "tech_self_score", "score")
    df_scores0 = df_scores0.rename(columns={"tech_self_score": "language_name"})
    # swap columns
    columns_titles = ["applicant_id", "language_name", "score"]
    df_scores0 = df_scores0.reindex(columns=columns_titles)
    # normalise language names
    df_scores0, df_lang0 = normalise(df_scores0, ["language_name"], deletion=False,
                                     new_id=True, index="language_name")
    # normalise strengths table
    df_stren0 = split_up_column(df_stren0, "strengths", "val", not_list=False, single_index=True)
    df_stren0, df_stren_names = normalise(df_stren0, ["strengths"], deletion=False,
                                          new_id=True, index="strengths")
    df_stren_names = df_stren_names.drop(columns="id")
    df_stren0 = df_stren0.reset_index()
    df_stren0 = df_stren0.drop(columns="index")

    # normalise weaknesses table
    df_weak0 = split_up_column(df_weak0, "weaknesses", "val", not_list=False, single_index=True)
    df_weak0, df_weak_names = normalise(df_weak0, ["weaknesses"], deletion=False,
                                        new_id=True, index="weaknesses")
    df_weak_names = df_weak_names.drop(columns="id")
    df_weak0 = df_weak0.reset_index()
    df_weak0 = df_weak0.drop(columns="index")

    # print(df_stren0[:20], df_stren_names[:20], sep="\n")
    # print(df_weak0[:20], df_weak_names[:20], sep="\n")
    # df_weak0 = split_up_column(df_weak0, "weaknesses")
    return df_cand0, df_scores0, df_stren0, df_weak0, df_lang0, df_stren_names, df_weak_names


def candidates_location(df_cand0):
    # print(df_cand0[:10])
    df_cand0, df_locations = normalise(df_cand0, ["Location"], deletion=False,
                                       new_id=True, index="Location")
    return df_cand0, df_locations


def get_tables_1():
    df_app, df_add = applicants_address()
    df_app, df_rec = applicants_recruiter(df_app)
    df_app = delete_column(df_app, "month")

    # extra post normalisation cleaning
    df_rec = df_rec.rename(columns={"invited_by": "name"})
    df_rec = split_name_into_2(df_rec, "name")
    return df_app, df_add, df_rec


def get_tables_2():
    df_json = clean_json()
    df_json, df_scores, df_stren, df_weak, df_lang, df_stren_names, df_weak_names = candidates_scores_strengths(df_json)

    return df_json, df_scores, df_stren, df_weak, df_lang, df_stren_names, df_weak_names


def get_tables_3():
    df_candidates = clean_candidates()
    df_candidates, df_locations = candidates_location(df_candidates)
    # print(df_locations)

    return df_candidates, df_locations


def get_tables_4(force_refresh=False):
    df_academy = clean_academy(force_refresh)
    df_academy = df_academy.drop(columns=["first_name", "last_names", "date_on_file"])
    # print(df_academy)
    # df_academy, df_behaviours = normalise(df_academy, ["behaviour"], deletion=False,
    #                                       new_id=True, index="behaviour")
    return df_academy

# MAIN

