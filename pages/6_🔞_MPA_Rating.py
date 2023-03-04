# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='MPA Rating - Hollywood-Box Office',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🔞 MPA Rating')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'G_Rating':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/MPA_Rating/G_MPAA_Rating.csv')
    elif query == 'PG_Rating':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/MPA_Rating/PG_MPAA_Rating.csv')
    elif query == 'PG_13_Rating':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/MPA_Rating/PG_13_MPAA_Rating.csv')
    elif query == 'R_Rating':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/MPA_Rating/R_MPAA_Rating.csv')
    elif query == 'share_of_t':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/MPA_Rating/Share_Total.csv')
    return None


G_Rating = get_data('G_Rating')
PG_Rating = get_data('PG_Rating')
PG_13_Rating = get_data('PG_13_Rating')
R_Rating = get_data('R_Rating')
share_of_t = get_data('share_of_t')


df = G_Rating.head(10)
df2 = PG_Rating.head(10)
df3 = PG_13_Rating.head(10)
df4 = R_Rating.head(10)
df5 = share_of_t

#################################################################################################
st.write(""" ### MPA Rating Concept ##  """)

st.write("""
The Motion Picture Association film rating system is used in the United States and its territories to rate a motion picture's suitability for certain audiences based on its content. The system and the ratings applied to individual motion pictures are the responsibility of the Motion Picture Association (MPA). Introduced in 1968, following the Hays Code of the classical Hollywood cinema era, the MPA rating system is one of various motion picture rating systems that are used to help parents decide what films are appropriate for their children. It is administered by the Classification & Ratings Administration (CARA), an independent division of the MPA. The MPA film ratings are as follows: 
* G – (General Audiences) All ages admitted. Nothing that would offend parents for viewing by children
* PG – (Parental Guidance Suggested) Some material may not be suitable for children. Parents urged to give "parental guidance"  
* PG-13 – (Parents Strongly Cautioned) Some material may be inappropriate for children under 13, Parents are urged to be cautious    
* R – (Restricted) Under 17 requires accompanying parent or adult guardian. Contains some adult material   
* NC-17 – (Adults Only) No one 17 and under admitted. Clearly adult. Children are not admitted  [[8]](https://en.wikipedia.org/wiki/Motion_Picture_Association_film_rating_system)    

In this dashboard, we do not include NC-17 rating as a separate rating and blend this rating with R rating as one category.
  """)


st.info(""" ##### In This MPA Rating Section you can find: ####

* G Rating Share of Total Gross with Top 10 Movies
* PG Rating Share of Total Gross with Top 10 Movies
* PG-13 Rating Share of Total Gross with Top 10 Movies  
* R Rating Share of Total Gross with Top 10 Movies  





""")


#################################################################################################

st.write(""" ## G Rating top 10 Life time Gross [USD]
""")

st.write(""" Ten percent of Hollywood's total box office receipts come from G-rated movies, and "Toy Story 4", with an overall rank of 28, comes in first. These two metrics demonstrated that G-rated movies are not always the most profitable movies overall.

""")
c1, c2 = st.columns(2)
with c1:
    # Top new contracts based on weekly transactions
    fig = px.bar(df.sort_values(["Lifetime Gross", "Title"], ascending=[
        True, False]), x="Title", y="Lifetime Gross", color="Title", title='Top 10 G Rate Movie Based on Life Time Gross [USD]')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Life Time Gross [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:

    fig = px.pie(df5, values="Total Gross", names="MPA Rate",
                 title='Share G Rating Movie of Total Gross', hole=0.4)
    fig.update_layout(legend_title='USDC Amount', legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.table(df)

#####################################################
st.write(""" ## PG Rating top 10 Life time Gross [USD]
""")
st.write(""" With a 13th-place overall , "Incredibles 2" tops the list of PG-rated films, which account for 28% of all Hollywood box office receipts. There are no recent PG-rated films in the top 10.

""")
c1, c2 = st.columns(2)
with c1:
    # Top new contracts based on weekly transactions
    fig = px.bar(df2.sort_values(["Lifetime Gross", "Title"], ascending=[
        True, False]), x="Title", y="Lifetime Gross", color="Title", title='Top 10 PG Rate Movie Based on Life Time Gross [USD]')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Life Time Gross [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:

    fig = px.pie(df5, values="Total Gross", names="MPA Rate",
                 title='Share PG Rating Movie of Total Gross', hole=0.4)
    fig.update_layout(legend_title='USDC Amount', legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.table(df2)


######################################################
st.write(""" ## PG-13 Rating top 10 Life time Gross [USD]
""")
st.write(""" What is really interesting here is that all 10 of the overall top-ranked movies are PG-13-rated. and there were mostly created in recent years, except "Avatar" and "Titanic". This demonstrates that in recent years, children under the age of 13 have not been targeted in the same way that teenagers have. 

""")
c1, c2 = st.columns(2)
with c1:
    # Top new contracts based on weekly transactions
    fig = px.bar(df3.sort_values(["Lifetime Gross", "Title"], ascending=[
        True, False]), x="Title", y="Lifetime Gross", color="Title", title='Top 10 PG-13 Rate Movie Based on Life Time Gross [USD]')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Life Time Gross [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    fig = px.pie(df5, values="Total Gross", names="MPA Rate",
                 title='Share PG-13 Rating Movie of Total Gross', hole=0.4)
    fig.update_layout(legend_title='USDC Amount', legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.table(df3)

##########################################################
st.write(""" ## R Rating top 10 Life time Gross [USD]
""")
st.write(""" R-rated movies are responsible for 20% of total gross, and "Joker," produced in 2019, was the most recent successful one.
""")
c1, c2 = st.columns(2)
with c1:
    # Top new contracts based on weekly transactions
    fig = px.bar(df4.sort_values(["Lifetime Gross", "Title"], ascending=[
        True, False]), x="Title", y="Lifetime Gross", color="Title", title='Top 10 R Rate Movie Based on Life Time Gross [USD]')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Life Time Gross [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    fig = px.pie(df5, values="Total Gross", names="MPA Rate",
                 title='Share R Rating Movie of Total Gross', hole=0.4)
    fig.update_layout(legend_title='USDC Amount', legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.table(df4)


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* G-rated movies bring in 10% of all box office earnings in Hollywood and are the least successful
* The top 10 films on the overall rank list are all PG-13 movies.
* The most profitable group at the box office is PG-13 films, which brought in 41% of all sales
* While the volume of bridge transactions was significantly influenced  
* R-rated films account for 20% of global box office and have not had a blockbuster in the past three years

""")
