# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='WorldWide - Hollywood-Box Office',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🌎 WorldWide Box Office ')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'worldwide_Total_Gross':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/All%20time/Worldwide.csv')
    elif query == 'Worldwide_Foreign':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/All%20time/Worldwide2.csv')
    elif query == 'worldwide_foreign_percent':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/All%20time/Worldwide3.csv')
    return None


worldwide_Total_Gross = get_data('worldwide_Total_Gross')
Worldwide_Foreign = get_data('Worldwide_Foreign')
worldwide_foreign_percent = get_data('PG_13_Rating')


df = worldwide_Total_Gross
df2 = Worldwide_Foreign


#################################################################################################
st.write(""" ### Domestic and Worldwide Box Office ##  """)

st.write(""" The term "Domestic" in this Dashboard refers to gross box office receipts from North America (the U.S. and Canada), while the term "Foreign" refers to the rest of the world. and the sum of these two phrases is "Worldwide".
  """)


st.info(""" ##### In This Worldwide Section you can find: ####

* Top 10 Best Foreign Seller
* Top 10 Worldwide Best Seller



""")


#################################################################################################

st.write(""" ## Top 10 Best Foreign Seller
""")

st.write(""" With a 2.13 billion foreign lifetime gross, Avatar led all Hollywood productions. The figure shows that 73% of Avatar's overall global box office earnings came from overseas. Furious 7 got the largest overseas share with 76% of the total.
""")
# Top new contracts based on weekly transactions
fig = px.bar(df2.head(10), x="Title", y="Foreign Lifetime Gross",
             color="Title", title='Top 10 Best Foreign Seller')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Foreign Lifetime Gross[USD]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.table(df2.head(10))


#####################################################

st.write(""" ## Top 10 Worldwide Best Seller """)

st.write(""" Foreign sales account for over 70% of all successful movie revenue. Recent films have had a fair amount of success abroad.
 """)
# Top new contracts based on weekly transactions
fig = px.bar(df.head(10), x="Title", y="Worldwide Lifetime Gross",
             color="Title", title='Top 10 G Rate Movie Based on Life Time Gross [USD]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Worldwide Lifetime Gross[USD]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.table(df.head(10))


st.text(" \n")

st.info(""" #### Summary: ####


* Avatar led all Hollywood productions with a lifetime foreign gross of 2.13 billion dollars
* Furious 7 got the largest overseas share with 76% of the total
* Around 70% of successful movie revenues come from foreign sales.
* Recent movies have seen some success overseas more than before

""")
