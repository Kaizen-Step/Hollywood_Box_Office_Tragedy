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


with c1:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/Avatar.jpg'))
with c2:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/fury.jpg'))
with c3:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/joker3.jpg'))


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

Hollywood's box office revenues in North America have significantly decreased in 2020 as a result of the coronavirus epidemic closing cinemas and studios delaying the release of numerous new films. In addition to this, social scientists believe that movies ,as a form of entertainment, are no longer the main topic of our cultural conversation.  
Although the issues are considered a catastrophe for the Hollywood industry, the story is far from over. We searched the internet for an appropriate data gathering technique to evaluate the Hollywood box office history using current data in order to better comprehend the problem and look for causes and solutions. For this concept, Kaggle offers a number of data sets, although some of them are outdated and others are poorly arranged. Several perspectives on the Box Office Mojo website were used on two distinct Kaggle data sets. We collected this data for our research into Hollywood box office after the COVID-19 outbreak, developed our own data sets based on IMDB box office mojo categorization, then updated the material that was lacking from the IMDB box office mojo website.
After collecting and purifying the data, we started looking at the Hollywood box office since 2000 to get perspective and look for long-term trends. We then narrowed our attention to the Hollywood gross avenue following the COVID-19 outbreak to look for impact and remedies for this disaster.then examine the market's leading studios and genres, as well as the cultural and economic effects they have. The final sections examine MPA ratings and overseas gross sales. At conclusion, we made an effort to summarize how Hollywood has changed and it might change in order to improve its marketing strategy and turn this tragedy into a happy ending drama. Following this, we shared Kaggle data sets with IMDB Box Office Mojo scraped data(from May 1973 to February 2023).
""")


st.text(" \n")
st.write("""   
#### Sources ####  """)
st.write("""    1.https://en.wikipedia.org/wiki/Cinema_of_the_United_States#Hollywood   
        2.https://en.wikipedia.org/wiki/Box_office#cite_note-1   
        3.https://www.boxofficemojo.com/
            """)


st.text(" \n")
c1, c2 = st.columns(2)
with c1:
    st.info(
        '**Twitter:  [Ludwig.1989](https://flipsidecrypto.xyz/)**', icon="🕊️")
    st.info(
        '**Data Set (1):  [IMDB Box office Mojo (Kaggle)](https://www.kaggle.com/code/jonbown/box-office-mojo-web-scraping-with-python)**', icon="🧠")

with c2:
    st.info(
        '**Project Github:  [Hollywood Box Office](https://github.com/Kaizen-Step/Hollywood_Box_Office_Tragedy)**', icon="💻")
    st.info(
        '**Data Set (2):  [IMDB Box office Mojo (Kaggle)](https://www.kaggle.com/datasets/thedevastator/hollywood-movies-domestic-lifetime-gross-and-ran?resource=download)**', icon="🧠")
