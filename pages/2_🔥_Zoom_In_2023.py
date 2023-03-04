# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit


# Layout
st.set_page_config(page_title='Zoom In 2023 -  Hollywood-Box Office',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🔥 Zoom In 2023')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Daily_2023':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Y23/Y23-Daily.csv')
    elif query == 'Weekly_2023':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Y23/Y23-Weekly.csv')
    elif query == 'daily_table':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Y23/Y23-Daily2.csv')
    return None


Daily_2023 = get_data('Daily_2023')
Weekly_2023 = get_data('Weekly_2023')
daily_table = get_data('daily_table')

df = Daily_2023
df2 = Weekly_2023
df3 = daily_table

#################################################################################################
st.write(""" ### Hollywood Box Office 2023 expectation ##  """)

st.write(""" In the year 2023, the expected value of movie production in the United States of America is \$26.7 billion.[[5]](https://www.enterpriseappstoday.com/stats/film-industry-statistics.html#:~:text=In%20the%20year%202023%2C%20the,States%20of%20America%20is%203.3%25.) As we saw in the previous section, Box office gross income in 2022 was \$7.3 billion, and gross income in 2023 has so far reached 1.06 billion in less than two months. Is this anticipation accurate? Let's dive in the daily and weekly figures for 2023 to find out.

   

  """)


st.info(""" ##### In This Zoom in 2023 Section you can find: ####

* Daily Top 10 Movie Grosss in 2023 [USD]  
* Daily Number of Movie Released 
* 10 days with Top Gross Profit [Detailed Table]
* 2023 Weekly Figures
* Top First Sold Movie each Week [Detailed Table]



""")


#################################################################################################


#####################################################

st.write(""" ## Hollywood 2023 Daily Figures  """)

st.write(""" As expected, there were significant differences between the weekend's top 10 gross and other days of the week.The first two months of 2023 saw an average daily top-ten movie gross of \$17.65 million; in comparison, the same period in 2019 saw an average daily top-ten movie gross of \$20.37 million. While "Avatar: The Way of Water" accounted for the majority of the first month's gross with \$665.88 million, "Ant-Man and the Wasp: Quantumania" created a hype in the second month weekend, and the market hit a record of \$54.71 million in one day, with "Ant-Man and the Wasp: Quantumania" accounting for \$46.5 million (85% of the day total) of this. The overall view of the 2023 daily charts revealed that the market was easily influenced by a single big production movie. And this is made much more intriguing by the knowledge that every day, more than 30 movies were released.
 """)
# Hollywood Industry total gross over course of years [USD]
fig = px.bar(df, x="Date", y="Top 10 Gross",  color="Date",
             title='Daily Top 10 Movie Grosss in 2023 [USD]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily top 10 Gross [USD]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)
with c1:
    # Hollywood Industry total gross over course of years [USD]
    fig = px.area(df, x="Date", y="Top 10 Gross",
                  title='Daily Overall Grosss Trend in 2023')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Overall Gross [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Daily Number of Release in 2023
    fig = px.line(df, x="Date", y="%± YD",
                  title='Daily Top 10 Grosss Change Rate [Yesterday]', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Change Rate')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(""" ### Daily Number of Release """)
st.write(""" The average number of daily movies released in 2019 (prior to the Covid-19 pandemic) was 54, but this figure dropped significantly to 32.4 in 2023, possibly due to an increase in the number of big production movies, as discussed in the previous section.
""")
# Hollywood Industry total gross over course of years [USD]
fig = px.area(df, x="Date", y="Releases",
              title=' Daily Number of Release in 2023')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title=' Daily Release')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#########################################################


st.write(""" ### 10 days with Top Gross Profit [Detalied Table] """)
st.write(""" Here are the top ten days with the highest gross during the first two months of 2023:
""")
st.table(df3.head(10))


##############################################################

st.write(""" ## Hollywood 2023 Weekly Figures """)
st.write(""" The release of "Ant-Man and the Wasp: Quantumania" on February 17 caused a 135% increase in the market's weekly gross change, which was more noticeable in weekly charts.This demonstrates how influential big-budget movies were on the market for the entire week.

""")
# Hollywood Industry total gross over course of years [USD]
fig = px.bar(df2, x="Dates", y="Top 10 Gross",  color="Dates",
             title='Weekly Top 10 Movie Gross in 2023 [USD]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Weekly top 10 Gross [USD]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)
with c1:
    # Hollywood Industry total gross over course of years [USD]
    fig = px.area(df2, x="Dates", y="Overall Gross",
                  title='Weekly Overall Gross Trend in 2023 [USD]')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Overall Gross [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with c2:
    # Daily Number of Release in 2023
    fig = px.line(df2, x="Dates", y="%± LW",
                  title='Weekly Overall Gross Change Rate', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Overall Gross Change Rate')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


######################################################

st.write(""" ### Weekly Number of Relaese """)

st.write("""  The weekly number of releases has steadily increased over the last two months, reaching 63 movies per week last week. 
""")

# Hollywood Industry total gross over course of years [USD]
fig = px.area(df2, x="Dates", y="Releases",
              title=' Weekly Number of Release in 2023')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title=' Weekly Release')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#########################################################


############################################################
st.write(""" ### Top First Sold Movie each Week with Detalied Table """)
st.write(""" The top-grossing movie each week, along with information from that week, is listed in the following table:

""")
st.table(df2.head(20))
##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* The average daily top-ten movie gross for the first two months of 2023 was \$17.65 million
* On February 17, "Ant-Man and the Wasp: Quantumania" brought in \$46.5 million of the \$54.71 million total
* The market was easily influenced by a single big production movie
* In 2019, there were 54 average daily movie releases, however this number fell to 32.4 in 2023
* The market's weekly gross change increased by 135% with the release of "Ant-Man and the Wasp: Quantumania" on February 17

""")
