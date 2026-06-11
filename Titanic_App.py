import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page layout to wide
st.set_page_config(page_title="Titanic Survival Explorer", layout="wide")

#  Load the Data
@st.cache_data
def load_data():
    df = pd.read_csv('titanic_train_clean_dataset.csv')
    # Quick cleanup for the dashboard
    df['Survived_Label'] = df['Survived'].map({1: 'Survived', 0: 'Deceased'})
    df['Pclass_Label'] = df['Pclass'].map({1: '1st Class', 2: '2nd Class', 3: '3rd Class'})
    return df

df = load_data()

# Dashboard Header
st.title("🚢 Titanic Survival Explorer")
st.markdown("Explore passenger survival statistics and model insights from the Titanic disaster.")
st.divider()

# Sidebar Controls 
st.sidebar.header("Filter Passengers")
selected_class = st.sidebar.multiselect(
    "Passenger Class", 
    options=['1st Class', '2nd Class', '3rd Class'], 
    default=['1st Class', '2nd Class', '3rd Class']
)

selected_sex = st.sidebar.multiselect(
    "Sex", 
    options=df['Sex'].unique(), 
    default=df['Sex'].unique()
)

# Apply Filters
filtered_df = df[
    (df['Pclass_Label'].isin(selected_class)) & 
    (df['Sex'].isin(selected_sex))
]

# Top Row: KPI Metrics
kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    st.metric("Total Passengers", len(filtered_df))
with kpi2:
    survival_rate = filtered_df['Survived'].mean() * 100
    st.metric("Overall Survival Rate", f"{survival_rate:.1f}%")
with kpi3:
    # Assuming 'Is_Alone' is 1 for alone and 0 for with family
    solo_travelers = filtered_df['Is_Alone'].sum()
    st.metric("Solo Travelers", solo_travelers)

st.divider()

# Visualizations (2x2 Grid)
col1, col2 = st.columns(2)

with col1:
    # Chart 1: Survival Rate by Passenger Class
    st.subheader("Survival Rate by Class")
    class_survival = filtered_df.groupby('Pclass_Label')['Survived'].mean().reset_index()
    fig1 = px.bar(class_survival, x='Pclass_Label', y='Survived', 
                  labels={'Survived': 'Survival Rate', 'Pclass_Label': 'Class'},
                  color='Pclass_Label', text_auto='.1%')
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    # Chart 2: Gender Breakdown of Survivors
    st.subheader("Survivors by Gender")
    survivors_only = filtered_df[filtered_df['Survived'] == 1]
    fig2 = px.pie(survivors_only, names='Sex', hole=0.4, 
                  color='Sex', color_discrete_map={'male':'blue', 'female':'pink'})
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    # Chart 3: Survival by Age Group
    st.subheader("Survival Status by Age")
    fig3 = px.histogram(filtered_df, x="Age_bin", color="Survived_Label", 
                        nbins=30, barmode="group",
                        color_discrete_map={'Survived': 'green', 'Deceased': 'red'})
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    # Chart 4: Mock Feature Importances (Hardcoded based on your RF model)
    st.subheader("Model Feature Importances")
    feature_data = pd.DataFrame({
        'Feature': ['Sex/Title', 'Pclass', 'Fare', 'Age', 'Family_Size', 'Embarked'],
        'Importance': [0.35, 0.20, 0.18, 0.15, 0.08, 0.04]
    }).sort_values('Importance', ascending=True)
    
    fig4 = px.bar(feature_data, x='Importance', y='Feature', orientation='h',
                  color='Importance', color_continuous_scale='Blues')
    st.plotly_chart(fig4, use_container_width=True)