from datetime import date
import os
import pandas as pd
from ..utils import get_urls

def parse_pipeline(base : str, project : str, scrape_dir : str) -> pd.DataFrame:

    """ 
    Parse pages from an excel list downloaded from TED 

    params:
    base: directory where results should be placed in subdirectories
    project: name of the project (such as AT, for namings)
    chunksize: how many pages should be scraped (1500 default bc TED refuses to load pages after a while) 

    returns:
    segmented_df: dataframe with parsed results from pages
    remaining_links_to_scrape: those links which were not done due to the chunksize limitation
    """
    scrape_dates = [date.today().strftime('%d_%m_%Y')]                           

    output_dir = base + project + "/parsed raw pages"

    parse_notices_from_pages(raw_directory = scrape_dir, 
                        output_dir = output_dir,
                        scrape_dates = scrape_dates, 
                        project = project)

    path = prepare_notice_dir2(notice_dir = output_dir)
    sectioned_df = get_sections_from_notices(folder = path, dq_for_each_file = False) 

    ###################################################################################################################
    ### Unclear if this is reliable across countries
    non_roman_suspicion = sectioned_df.apply(lambda x: "6.1.  \n \n \n Result" in x.loc["Results_long"], axis = 1)
    df_non_roman = sectioned_df.loc[non_roman_suspicion[non_roman_suspicion == True].index, :] 
    df_roman = sectioned_df.loc[non_roman_suspicion[non_roman_suspicion == False].index, :] 
    ###################################################################################################################

    output_dir2 = base + project + "/parsed tables/"
    path = prepare_notice_dir2(notice_dir = output_dir2)

    parsed_nr = full_non_roman_parser(df_non_roman, path, project)
    parsed_r = parse_romans_wrapper(df_roman, path, project)

    combined_df = combine_key_cols(parsed_nr, parsed_r)
    segmented_df = do_simple_segmentation(combined_df)

    

    output_dir3 = output_dir2 + "combined_segmented/"
    final_path = prepare_notice_dir2(notice_dir = output_dir3)

    orig_dir = os.getcwd()
    os.chdir(output_dir2)
    if "combined_segmented" not in os.listdir():
        os.mkdir("combined_segmented")
    os.chdir(orig_dir)

    segmented_df.to_csv(final_path + "TED_{}_{}.csv".format("full", project, date.today().strftime('%d_%m_%Y')), encoding = "utf-8")

    return segmented_df

def full_pipeline(excel_path : str, base : str, project : str, chunksize : int = 1500) -> pd.DataFrame:

    """ 
    Scrape and parse pages from an excel list downloaded from TED 

    params:
    excel_path: the path to the file, including the name
    base: directory where results should be placed in subdirectories
    project: name of the project (such as AT, for namings)
    chunksize: how many pages should be scraped (1500 default bc TED refuses to load pages after a while) 

    returns:
    segmented_df: dataframe with parsed results from pages
    remaining_links_to_scrape: those links which were not done due to the chunksize limitation
    """

    full_url_list = get_urls(excel_path)

    prepare_notice_dir(notice_dir = base, project = project)

    scrape_dir = base + project + "/unparsed raw pages"

    # scraping not fully finished if chunksize is lower than table size
    remaining_links_to_scrape = scrape(full_url_list, scrape_dir, headless = True, chunksize = chunksize)                            

    parse_pipeline(base = base,
                   project = project,
                   scrape_dir = scrape_dir)

    return segmented_df, remaining_links_to_scrape

if __name__ == "__main__":
    excel_path = "C:/Users/OSBPAKSI/Downloads/ROU_TED_14-01-2025.xlsx"
    base = "C:/Users/OSBPAKSI/Carl Zeiss AG/Data & Analytics AT CH SEE - Data Projects/01_Projects/Tender Analysis/01_Data/projects/"
    project = "Test Project 3"
    
    segmented_df, _ = full_pipeline(excel_path=excel_path,
                                    base = base,
                                    project = project, 
                                    chunksize = 5)
