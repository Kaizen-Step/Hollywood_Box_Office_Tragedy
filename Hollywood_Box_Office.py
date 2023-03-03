# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title=' Hollywood Box Office',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' Hollywood Box Office Tragedy 🎬')
st.text(" \n")
# Content
c1, c2, c3 = st.columns(3)


with c3:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/metricsstackedwhite.png'), width=250)
with c1:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/t6.png'), width=300)


st.write("""
### Hollywood Movie Indsustry ###
The cinema of the United States, consisting mainly of major film studios (also known metonymously as Hollywood) along with some independent film, has had a large effect on the global film industry since the early 20th century. The dominant style of American cinema is classical Hollywood cinema, which developed from 1913 to 1969 and is still typical of most films made there to this day. While Frenchmen Auguste and Louis Lumière are generally credited with the birth of modern cinema, American cinema soon came to be a dominant force in the emerging industry. As of 2017, it produced the third-largest number of films of any national cinema, after India and China, with more than 600 English-language films released on average every year. While the national cinemas of the United Kingdom, Canada, Australia, and New Zealand also produce films in the same language, they are not part of the Hollywood system. Because of this, Hollywood has also been considered a transnational cinema, and has produced multiple language versions of some titles, often in Spanish or French. Contemporary Hollywood often outsources production to Canada, Australia, and New Zealand.
Hollywood is considered to be the oldest film industry, in the sense of being the place where the earliest film studios and production companies emerged. It is the birthplace of various genres of cinema—among them comedy, drama, action, the musical, romance, horror, science fiction, and the war epic—and has set the example for other national film industries.[[1]](https://en.wikipedia.org/wiki/Cinema_of_the_United_States#Hollywood)

### Box Office ###
A box office or ticket office is a place where tickets are sold to the public for admission to an event. By extension, the term is frequently used, especially in the context of the film industry, as a metonym for the amount of business a particular production, such as a film or theatre show, receives. The term is also used to refer to a ticket office at an arena or a stadium.    
Box office business can be measured in the terms of the number of tickets sold or the amount of money raised by ticket sales (revenue). The projection and analysis of these earnings is greatly important for the creative industries and often a source of interest for fans.[[2]](https://en.wikipedia.org/wiki/Box_office#cite_note-1)

### Box Office Mojo by IMDb ###
The top online box office reporting and analysis service, Box Office Mojo by IMDbPro, keeps track of domestic and international box office receipts. Professionals in the entertainment industry, journalists, researchers, financiers, data analyst and movie enthusiasts worldwide can use Box Office Mojo by IMDbPro as a resource. It offers thorough box office information for more than 60 nations and territories. Movie Office Mojo by IMDbPro contains domestic box office grosses for every day, every week, every weekend, every month, every year, every season, and every holiday. IMDbPro also offers a list of all-time rankings and a release schedule for forthcoming films.

""")


st.write("""
## Methodology ##  

Hollywood's box office revenues in North America have significantly decreased in 2020 as a result of the coronavirus epidemic closing cinemas and studios delaying the release of numerous new films. Moreover, some social scientists think that movies ,as a form of entertainment, are no longer the main topic of our cultural conversation.
Off-chain This week, Bounty wants a thorough examination of the box office using Hollywood statistics. We search the Internet for a suitable data collection to examine the Hollywood box office over time using current data. Kaggle offers various data sets for this idea. We used two separate Kaggle data sets that were taken from various views on the Box Office Mojo website. For our investigation of Hollywood box office following the COVID-19 epidemic, we acquired this information and created our own data sets.
After collecting and purifying the data, we started looking at the Hollywood box office since 2000 to get perspective and look for long-term trends. We then narrowed our attention to the Hollywood gross avenue following the COVID-19 outbreak to look for impact and remedies for this disaster. then look for a studio- and genre-specific cultural and economic analysis of Hollywood box office. After all, we want to provide a summary of how Hollywood has evolved and should change in order to improve its marketing strategy. Following this section, we shared Kaggle data sets containing IMDB Box Office Mojo scraped data. 

""")
st.text(" \n")
st.write("""   
#### Sources ####  """)
st.write("""    1.https://en.wikipedia.org/wiki/Cinema_of_the_United_States#Hollywood   
        2.https://en.wikipedia.org/wiki/Box_office#cite_note-1)  
        3.https://help.imdb.com/article/imdbpro/industry-research/box-office-mojo-by-imdbpro-faq/GCWTV4MQKGWRAUAP?ref_=mojo_ftr_help#  
              """)
st.text(" \n")
c1, c2 = st.columns(2)
with c1:
    st.info(
        '**Twitter:  [Ludwig.1989](https://flipsidecrypto.xyz/)**', icon="🦉")
    st.info(
        '**Data Set (1):  [IMDB Box office Mojo (Kaggle)](https://www.kaggle.com/code/jonbown/box-office-mojo-web-scraping-with-python)**', icon="🧠")

with c2:
    st.info(
        '**Project Github:  [Hollywood Box Office](https://github.com/Kaizen-Step/The_Whales_of_Near)**', icon="💻")
    st.info(
        '**Data Set (2):  [IMDB Box office Mojo (Kaggle)](https://www.kaggle.com/datasets/thedevastator/hollywood-movies-domestic-lifetime-gross-and-ran?resource=download)**', icon="🧠")
