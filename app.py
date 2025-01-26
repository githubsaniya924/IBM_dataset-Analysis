import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache_data
def load_data():
    # Hardcoded file path (adjust as necessary)
    url = "D:\Dataset-Employee Attrition and performance/IBMEmployee_data.csv"  # Replace with your file path
    data = pd.read_csv(url)
    return data


def home_page():
    st.markdown(
    """
    <h2 style="text-align: center; color: #0077B5;">Unveiling IBM Employee Dynamics: A Comprehensive Study on Attrition, Performance, and Job Satisfaction</h2>
    """,
    unsafe_allow_html=True
)
    st.image("D:\Dataset-Employee Attrition and performance\ibm_img.webp", caption="IBM and Employees", use_container_width=True,)

    st.markdown(
        """
        <h2>Introduction</h2>
        <p>IBM Employee Attrition Analysis has been analyzed in multiple ways with different outlooks 
        and different replications of the dataset. IBM (International Business Machines), founded since 1911, 
        is a global hybrid cloud & AI, and consulting expertise. IBM has helped more than 175 countries gain competitive edge
         within their industries, and more than 4,000 government and corporate companies rely on IBM’s service. As a company that
          has been around for over 100 years to remain competitive and innovate within their industries the company must maintain their 
          edge through the quality and performance of their employees.</p>
        """,  unsafe_allow_html=True
    )
    st.markdown(
        """
        <h2>Business Problem</h2>
        <p>Attrition, the voluntary and involuntary departure of employees from an organization, can have sustainable effects on the
         company’s performances, productivity, and overall workforce stability. As one of the leading players in the technology 
         industry, IBM faces the challenger of understanding and mitigating attrition to sustain its competitive edge and ensure the 
         long-term success of its business.</p>
        """,  unsafe_allow_html=True
    )
    st.markdown(
        """
        <h2>Motivation</h2>
        <p>The workforce is becoming older and more dynamic. As the age increases the demand for healthcare increase. 
        The number of millennials and Gen Z comprising the workforce is increasing. Millennials want a more flexible workplace and 
        experience higher job satisfaction based on the work they perform. Gen Z more like baby boomers and are looking to secure
        quality benefits along with workplace flexibility. The results showed evidence that participating in a wellness program will
        increase an employee’s extrinsic and intrinsic job satisfaction levels. Leaders should use a wellness program as a tool to 
        improve both employee health and job satisfaction.

        The purpose of IBM HR Attrition Analysis is to offer actionable insights, empowering IBM’s HR department and management 
        to make well-informed decisions and to utilize impactful retention tactics. Through identifying the factors affecting 
        attrition and enacting precise interventions, IBM can decrease attrition rates, increase employee satisfaction, promoting
         an optimal workforce that aligns with the company goal and innovation.</p>
        """,  unsafe_allow_html=True
    )
    

    st.markdown(
    """
    <style>
    .fab-container {
        display: flex;
        justify-content: center; /* Centers the icons horizontally */
        align-items: center; /* Centers the icons vertically within their container */
        gap: 20px; /* Space between icons */
        position: sticky; /* Ensures the icons stay in place */
        bottom: 20px; /* Distance from the bottom of the page */
        left: 0;
        right: 0;
        z-index: 9999; /* Keeps the icons on top of other elements */
    }
    .fab {
        background-color: #007BFF; /* Blue button */
        color: white;
        border: none;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        text-align: center;
        line-height: 60px;
        font-size: 24px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        cursor: pointer;
        transition: transform 0.2s, background-color 0.2s;
        text-decoration: none; /* Prevents underline */
    }
    .fab:hover {
        background-color: #0056b3;
        transform: scale(1.1); /* Enlarge slightly on hover */
    }
    .fab-call {
        background-color: #28A745; /* Green button */
    }
    .fab-call:hover {
        background-color: #1e7e34;
    }
    .fab-linkedin {
        background-color: #0077B5; /* LinkedIn blue */
    }
    .fab-linkedin:hover {
        background-color: #005582;
    }
    </style>

    <div class="fab-container">
        <!-- Email Button -->
        <a href="https://mail.google.com/mail/?view=cm&fs=1&to=saniyamachado2344@gmail.com" target="_blank">
            <div class="fab">📧</div>
        </a>
        <!-- Call Button -->
        <a href="tel:+1234567890" target="_blank">
            <div class="fab fab-call">📞</div>
        </a>
        <!-- LinkedIn Button -->
        <a href="https://www.linkedin.com/in/saniyamachado/" target="_blank">
            <div class="fab fab-linkedin">🔗</div>
        </a>
    </div>
    """, unsafe_allow_html=True
    )
def dataOverview_page():
    st.markdown("""
<h2>Data Overview</h2>
<p>The dataset contains 50,000 observations and 35 variables. It is related to HR analytics and focuses on employee attrition. Data reduction was conducted, reducing the number of variables to 27 by removing variables that lacked descriptions or did not provide meaningful insights. The final dataset includes relevant variables for analysis.</p>

<div>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">Age</summary>
    <p>Age of the employee (integer values).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">Attrition</summary>
    <p>Whether the employee left the company (Yes/No).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">BusinessTravel</summary>
    <p>Frequency of business travel (Travel_Rarely, Travel_Frequently, Non-Travel).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">DailyRate</summary>
    <p>Daily income rate (integer values).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">Department</summary>
    <p>Department where the employee works (Sales, Research & Development, Human Resources).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">DistanceFromHome</summary>
    <p>Distance between home and workplace (integer values).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">Education</summary>
    <p>Education level (1: Below College, 2: College, 3: Bachelor, 4: Master, 5: Doctor).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">EnvironmentSatisfaction</summary>
    <p>Satisfaction with the work environment (1: Low, 2: Medium, 3: High, 4: Very High).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">Gender</summary>
    <p>Gender of the employee (Male/Female).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">JobInvolvement</summary>
    <p>Level of job involvement (1: Low, 2: Medium, 3: High, 4: Very High).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">JobLevel</summary>
    <p>Level of the job in the company (integer values).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">JobRole</summary>
    <p>Role of the employee (e.g., Sales Executive, Research Scientist, Manager).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">JobSatisfaction</summary>
    <p>Satisfaction with the job (1: Low, 2: Medium, 3: High, 4: Very High).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">MaritalStatus</summary>
    <p>Marital status (Single, Married, Divorced).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">NumCompaniesWorked</summary>
    <p>Number of companies the employee has worked at (integer values).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">OverTime</summary>
    <p>Whether the employee works overtime (Yes/No).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">PercentSalaryHike</summary>
    <p>Percentage increase in salary (integer values).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">PerformanceRating</summary>
    <p>Employee performance rating (1: Low, 2: Good, 3: Excellent, 4: Outstanding).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">RelationshipSatisfaction</summary>
    <p>Satisfaction with relationships at work (1: Low, 2: Medium, 3: High, 4: Very High).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">StockOptionLevel</summary>
    <p>Level of stock options granted (0: None, 1: Low, 2: Medium, 3: High).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">TotalWorkingYears</summary>
    <p>Total years of work experience (integer values).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">TrainingTimesLastYear</summary>
    <p>Number of training sessions attended last year (integer values).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">WorkLifeBalance</summary>
    <p>Work-life balance rating (1: Bad, 2: Good, 3: Better, 4: Best).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">YearsAtCompany</summary>
    <p>Number of years the employee has worked at the company (integer values).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">YearsInCurrentRole</summary>
    <p>Number of years in the current role (integer values).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">YearsSinceLastPromotion</summary>
    <p>Number of years since the last promotion (integer values).</p>
  </details>
  <details>
    <summary style="font-size: 1.2em; cursor: pointer;">YearsWithCurrManager</summary>
    <p>Number of years with the current manager (integer values).</p>
  </details>
</div>
""", unsafe_allow_html=True)

# Function for visualizations


def basic_analysis(df):
    # Display the entire dataset with checkbox option
    if st.checkbox('Show entire dataset'):
        st.write(df)

    # Filter data by Age
    min_age, max_age = int(df['Age'].min()), int(df['Age'].max())
    age_range = st.slider(
        "Select Age Range",
        min_age,
        max_age,
        (min_age, max_age),
        label_visibility="collapsed",  # Hide redundant label
    )

    # Filter data based on age range
    filtered_data = df[(df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])]

    # Age distribution graph
    st.subheader("Age Distribution")
    st.write("This histogram shows the distribution of employee ages within the selected age range, allowing for the identification of age clusters.")
    plt.figure(figsize=(5, 3))  # Reduced size
    sns.histplot(filtered_data['Age'], kde=True, color='skyblue', bins=20)
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title(f'Age Distribution for Ages {age_range[0]} to {age_range[1]}')
    st.pyplot(plt)

    # Attrition by gender graph
    st.subheader("Attrition by Gender")
    st.write("This bar plot shows the count of employees who have left the company ('Attrition = Yes') by gender, helping identify gender-specific attrition patterns.")
    gender_attrition = filtered_data[filtered_data['Attrition'] == 'Yes']['Gender'].value_counts()

    plt.figure(figsize=(5, 3))  # Reduced size
    sns.barplot(x=gender_attrition.index, y=gender_attrition.values, palette='pastel')
    plt.xlabel('Gender')
    plt.ylabel('Number of Attrition Cases')
    plt.title(f'Attrition by Gender (Ages {age_range[0]}-{age_range[1]})')
    st.pyplot(plt)

    # Calculate attrition percentage
    total_employees = filtered_data.shape[0]
    attrition_count = filtered_data['Attrition'].value_counts().get('Yes', 0)
    attrition_percentage = (attrition_count / total_employees) * 100 if total_employees > 0 else 0

    # Display the attrition percentage in a card
    st.markdown(
        """
        <h4 style="color:red;">Attrition Percentage</h4>
        """, unsafe_allow_html=True
    )

    # Custom card style for attrition percentage
    attrition_card_html = f"""
    <div style="
        background-color: #f0f8ff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        font-size: 24px;
        color: #333;
        font-weight: bold;
        width: 250px;
        margin: 0 auto;
        ">
        <p style="font-size: 16px;">Attrition Percentage</p>
        <h2>{attrition_percentage:.2f}%</h2>
    </div>
    """
    # Display the card
    st.markdown(attrition_card_html, unsafe_allow_html=True)

    # Department-wise Attrition
    st.markdown("### Department-wise Attrition")
    st.write("This bar plot illustrates the percentage of attrition by department, showing which departments are experiencing higher employee turnover.")
    dept_attrition = filtered_data.groupby("Department")["Attrition"].value_counts(normalize=True).unstack()
    if "Yes" in dept_attrition.columns:
        dept_attrition["Yes"] *= 100
        fig2, ax2 = plt.subplots(figsize=(5, 3))  # Reduced size
        dept_attrition["Yes"].sort_values().plot(kind="barh", color="teal", ax=ax2)
        ax2.set_title("Percentage of Attrition by Department")
        ax2.set_xlabel("Attrition (%)")
        ax2.set_ylabel("Department")
        st.pyplot(fig2)
    else:
        st.info("No attrition data available for the selected filters.")

    # Analyze years at the company
    st.markdown("### Years at Company vs Attrition")
    st.write("This box plot compares the number of years employees have been at the company to their attrition status, helping identify if tenure impacts attrition.")
    plt.figure(figsize=(5, 3))  # Reduced size
    sns.boxplot(x='Attrition', y='YearsAtCompany', data=filtered_data, palette="Set2")
    plt.title('Years at Company vs Attrition')
    plt.xlabel('Attrition')
    plt.ylabel('Years at Company')
    st.pyplot(plt)

    df = df.dropna(subset=['TrainingTimesLastYear', 'PerformanceRating'])
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='TrainingTimesLastYear', y='PerformanceRating', s=100, color='blue')

    # Adding labels and title
    plt.title('Training Hours vs Employee Performance', fontsize=16)
    plt.xlabel('Number of Training Hours', fontsize=12)
    plt.ylabel('Performance Rating', fontsize=12)

    # Display the plot
    plt.tight_layout()
    st.pyplot(plt)



    st.markdown("### WorkLifeBalance Distribution by Attrition (Pie Chart)")
    st.write("This pie chart shows the distribution of work-life balance levels for employees who stayed and those who left.")

    # Plotting pie charts for each attrition group with reduced chart size
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))  # Smaller size
    filtered_data[filtered_data['Attrition'] == 'Yes']['WorkLifeBalance'].value_counts(normalize=True).plot.pie(ax=ax1, autopct='%1.1f%%', colormap='viridis', title="Attrition: Yes")
    filtered_data[filtered_data['Attrition'] == 'No']['WorkLifeBalance'].value_counts(normalize=True).plot.pie(ax=ax2, autopct='%1.1f%%', colormap='viridis', title="Attrition: No")

    plt.tight_layout()
    st.pyplot(fig)
  


# Load the dataset
df = load_data()

# Sidebar for navigation
st.sidebar.title("Nav")
options = st.sidebar.radio("Go to", ["Home", "Data Overview", "Analysis"])

if options == "Analysis":
    analysis_options = st.sidebar.selectbox("Select Analysis Option", ["Basic Analysis", "Hypothesis Testing", "Predective Analysis"])

# Navigation logic
if options == "Home":
    home_page()
elif options == "Data Overview":
    dataOverview_page()
elif options == "Analysis":
    st.title("Analysis")
    if analysis_options == "Basic Analysis":
        basic_analysis(df)
    elif analysis_options == "Hypothesis Testing":
        st.write("Hypothesis Testing")
    elif analysis_options == "Predective Analysis":
        st.write("Predective Analysis")
