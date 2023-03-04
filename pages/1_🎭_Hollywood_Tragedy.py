# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title=' Domestic Yearly - Hollywood-Box Office',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🎭 Hollywood In Years')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Domestic_Yearly':
        return pd.read_json('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Domestic-Yearly.csv')
    elif query == 'table':
        return pd.read_json('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Domestic-Yearly2.csv')
    return None


Domestic_Yearly = get_data('Domestic_Yearly')
table = get_data('table')


df = Domestic_Yearly
df2 = table

#################################################################################################
st.write(""" ### Gross Box Office Revenue Concept ##  """)

st.write("""
 The revenue generated from ticket sales (receipts), including any taxes and other levies, is referred to as the gross box office.[[4]](http://uis.unesco.org/en/glossary-term/gross-box-office)  The information on grosses exclusively applies to theatrical receipts in this dashboard; it does not include DVD/Blu-ray sales or digital platform income. The distinction between net and gross box office revenue is substantial. While the money collected from the total sale of movie tickets is included in the gross box office collection, the term "net" refers to the gross box office collection less government deductions such as entertainment tax, service tax, etc. In this dashboard, we discussed the Hollywood movie industry's gross profit.    

  """)


st.info(""" ##### In This Hollywood Tragedy Section you can find: ####

* Hollywood Yearly Gorss Revenue [USD]
* Hollywood Yearly Gross Change Rate
* Number of Movie Released in Hollywood each Year  
* Average Gross per Release   
* Each year, the top-selling movie [detailed table]



""")


#################################################################################################


#####################################################
st.write(""" ## Hollywood Industry Yearly Gross Revenue """)

st.write("""  From \$7.47 billion in 2000 to \$11.36 billion in 2019, Hollywood has seen a steady rise in its overall revenue. As a result of the COVID-19 pandemic, which closed all of the world's teather doors, this trend came to an abrupt end in 2020 with a drop to 2.11B. Since December 2020, when vaccination became available, this figure has steadily increased, reaching nearly 4.5 billion in 2021 (a more than 112% increase). This upward trend persisted into 2022, but not by enough to surpass the high of 11.3B in 2019.

 """)
# Hollywood Industry total gross over course of years [USD]
fig = px.bar(df.tail(24), x="Year", y="Total Gross", color="Year",
             title='Hollywood Industry Yearly Gross since 2000 [USD]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Industry Yearly Gross [USD]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)

with c1:
    # Hollywood Industry total gross over course of years [USD]
    fig = px.area(df.tail(24), x="Year", y="Total Gross",
                  title='Hollywood Industry Total gross Trend')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Industry Total Gross [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    # Hollywood Industry Gross Yearly change Rate[USD]
    fig = px.line(df.tail(24), x="Year", y="%± LY",
                  title='Hollywood Industry Yearly Gross change Rate', log_y=False)
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Change Rate')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##############################################################
st.text(" \n")
st.write(""" ### Number of Movie Released in Hollywood each Year """)
st.write(""" The number of movies released has increased steadily since 2000, reaching a record high of 993 movies in a single year in 2018. This number decreased slightly to 910 in 2019. It's interesting to note that in 2020, the number of movies released decreased by 44% while the total gross revenue fell by 82%. This figure remained relatively stable in 2021 and 2022, accounting for nearly half of the 2019 figure. 
""")
# Number of Yearly Releases
fig = px.area(df.tail(24), x="Year", y="Releases",
              title='Number of Movie Released each Year ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Yearly Releases')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
######################################################

st.write(""" ### Average Gross per Release Since 2000 """)

st.write(""" This metric displays the average annual sales of each individual project, which is primarily correlated with the number of big production movies produced in a given year. As you can see, the average gross revenue for each movie increased from $12 million in 2019 to $14.84 million in 2022.
""")
# Average gross per Release over time [USD]
fig = px.bar(df.tail(24), x="Year", y="Average", color="Year",
             title='Average gross per Release over time [USD]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Average Gross per Released [USD]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


############################################################
st.write(""" ## Each year, the top-selling movie [detailed table]  """)
st.write(""" The following table lists the top-selling movie each year, with the details that we discussed earlier:
""")
st.table(df2.head(24))
##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* As a result of the COVID-19 pandemic, the Hollywood annual gross dropped from \$11.36 billion in 2019 to \$2.11 billion in 2020
* Annual gross has steadily increased, reaching nearly \$7.36 billion in 2022—a more than 112% increase in a single year.
* Since 2000, the number of movies released has continuously risen, with 2018 seeing a record-breaking 993 movies released in a single year
* The total gross fell by 82% in 2020 while the number of movies released fell by 44%.
* Each movie's average gross revenue rose from \$12 million in 2019 to \$14.84 million in 2022.

""")
