# Cell 1: Setup
import streamlit as st
from openai import OpenAI


# Load the images
hourly_wage_trends = Image.open('/Users/lokeshwaripotluri/Desktop/Task1.png')
comparison_of_weekly_wages = Image.open('/Users/lokeshwaripotluri/Desktop/Task2.png')
top_5_occupations = Image.open('/Users/lokeshwaripotluri/Desktop/Task3.1.png')
top3 = Image.open('/Users/lokeshwaripotluri/Desktop/Task3.2.png')
bottom3 = Image.open('/Users/lokeshwaripotluri/Desktop/Task3.3.png')

#AI responses
response_message_Task1 = """In analyzing Canadian wage data, several key aspects emerge. Firstly, when examining overall wage trends over time, it is evident that there has been a gradual increase in wages, albeit with fluctuations influenced by economic
factors and policy changes. The data shows that wages have generally risen in line with economic growth, but certain periods of recession or policy shifts have impacted the rate of increase.
Understanding these trends can provide insights into the broader economic landscape and the impact of government interventions on wage levels."""

response_message_Task2 = """Secondly, a significant issue highlighted in the data is the gender wage difference, showcasing the persistent gap in pay equity between men and women across various sectors.
Despite efforts to address this issue, the data reveals that women continue to earn less than their male counterparts, indicating a systemic problem that requires further attention. By delving into the
specifics of these disparities, it becomes clear that gender inequality remains a pressing concern in the Canadian labor market."""

response_message_Task3 = """Lastly, an exploration of employment types uncovers disparities in earnings, particularly in how financial stability affects hourly rates. The data suggests that certain
employment types, such as part-time or contract work, often result in lower wages compared to full-time positions. This disparity highlights the importance of financial security in determining wage levels,
with implications for workers' overall well-being and quality of life. By examining these employment-related factors, a deeper understanding of the complexities of wage disparities in Canada can be gained,
shedding light on the challenges faced by different segments of the workforce"""

st.title("Data Journalism: Canadian Wage Analysis")

st.header("Introduction")
st.write("In this report, we analyze the Canadian wage data with a focus on three key aspects.")

st.header("Analysis")
st.write(response_message_Task1)

st.image(hourly_wage_trends)

st.write(response_message_Task2)

st.image(comparison_of_weekly_wages)

st.write(response_message_Task3)

st.image(top_5_occupations)

st.image(top3)

st.image(bottom3)
