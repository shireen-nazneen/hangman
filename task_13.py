
from os import link, read, replace
import os
# from re import split
# from typing import Text, runtime_checkable
from bs4 import BeautifulSoup
import requests
import json
from requests import models
from task_1 import (wrting_file ,readingfile,scrape_top_list)
import random
from task_12  import cast
from os import write


movie_name="Dangal"
link_1="https://www.imdb.com/title/tt5074352/"
file="tt5074352"+".text"
   
def scrape_movie_details_with_cast(link_1,movie_name,file):
    print(file)
    # file="/home/shireen/Desktop/webscarping/all_file/"+"tt5074352"+".text"
    # print(file)
    # ipc-metadata-list-item__content-container
    print(os.path.exists(file))
    if (os.path.exists(file)):
        f=open(file,"r")
        # f.read(f)
        print(f)
        url_page_soup=BeautifulSoup(f,"html.parser")
        # print(url_page_soup,"----------------")
        find_div_dir=url_page_soup.find_all("div",class_="ipc-metadata-list-item__content-container")
        find_div_dir=url_page_soup.select("")
        print(find_div_dir)
        find_director=find_div_dir.find_all("a")
        director_list=[d.get_text() for d in find_director]
        find_summury_div=url_page_soup.find("div",class_="Hero__ContentContainer-kvkd64-10 eaUohq")
        find_span_p=find_summury_div.find("p")
        find_span_summary=find_span_p.find("span",class_="GenresAndPlot__TextContainerBreakpointL-cum89p-3 bgIqtV").text
        find_genre_div=url_page_soup.select("li[data-testid='storyline-genres']")
        for li_genre in find_genre_div:
            genre=li_genre.find_all("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")
            find_genre_list=[d.get_text() for d in genre]
        find_ul_runtime=url_page_soup.find("ul",class_="ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt")
        find_li_runtime=find_ul_runtime.find_all("li",class_="ipc-inline-list__item")
        i=0
        if len(find_li_runtime)==3:
            while i<len(find_li_runtime):
                if i==2:
                    find_runtime=find_li_runtime[i].text
                    i+=1
                    break
                i+=1
                continue
        else:
            find_runtime=find_li_runtime[1].text
        runtime=int(find_runtime[0])*60
        if "min" in find_runtime:
            min=find_runtime[3:]
            s=" "
            for i in min:
                if i=="m" or i=="i" or i=="n":
                    continue
                else:
                    s+=i
            runtime=runtime+int(s)
        else:
            runtime=runtime   
        find_img_div=url_page_soup.select("div[data-testid='hero-media__poster']")
        for div in find_img_div:
            img_url=div.find("a",class_="ipc-lockup-overlay ipc-focusable")["href"]
        find_div_lan=url_page_soup.select("div[data-testid='title-details-section']")
        for k in find_div_lan:
            find_all_li=k.select("li[data-testid='title-details-languages']")
            for li_lan in find_all_li:
                element=li_lan.find_all("li",class_="ipc-inline-list__item")
                languge_list=[d.get_text() for d in element]
        find_li_countury=url_page_soup.select("li[data-testid='title-details-origin']")  
        for li_country in find_li_countury:
            element2=li_country.find_all("li",class_="ipc-inline-list__item")
            list_country=[d.get_text() for d in element2]
        cast_actor=cast(link_1,file)
        # print(cast_actor)
        # print(movie_name,find_span_summary,"^^^^^^^^^^^^^^^^^^")
        dic2={"name":movie_name,"bio":find_span_summary, "director":director_list,"languge": languge_list,"country":list_country,"genre":find_genre_list,"runtime": runtime,"posterurl":"https://www.imdb.com"+img_url,"cast":cast_actor}
        writing_file=wrting_file("movie_details_cast.json",dic2)
        # print(dic2,"*******************")
        return dic2
    else:
        print("NNNNNNNNNNNNNNNNNNNNNNN")
# print(scrape_movie_details(link_1,movie_name,file))

movie=scrape_top_list()
list_movie=[]
for list in movie:
    url=list["url"]
    link=url[27:]
    id=""
    for i in link:
        if "/"!=i:
            id+=i
        else:
            break
    list_movie.append(id)
def get_movie_list_details():
    count=1
    list_movie_details=[]
    for j in movie:
        for id in list_movie:
            link_1=(j["url"])
            file="/home/shireen/Desktop/webscarping/all_file/"+id+".text"
            making_list_details=scrape_movie_details_with_cast(link_1,j["movie"],file)
            # print(making_list_details,"--------------------------")
            list_movie_details.append(making_list_details)
            print(count)
            count+=1
    file=wrting_file("movie_details_with_cast.json",list_movie_details)
    return list_movie_details
print(get_movie_list_details())


