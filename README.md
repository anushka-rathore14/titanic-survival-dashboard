<div align="center">

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=35&pause=1000&color=00D9FF&center=true&vCenter=true&multiline=true&width=900&height=100&lines=%F0%9F%9A%A2+Titanic+Survival+Explorer;Interactive+Machine+Learning+Dashboard" alt="Typing SVG" /></a>

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:00d9ff&height=200&section=header&text=Titanic%20Explorer&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Interactive%20Data%20Science%20Dashboard%20%7C%20Live%20on%20Streamlit&descSize=18&descAlignY=55&descColor=58a6ff" width="100%"/>

<br/>

![GitHub last commit](https://img.shields.io/github/last-commit/anushka-rathore14/titanic-survival-dashboard?style=for-the-badge&color=00d9ff&labelColor=0d1117)
![GitHub repo size](https://img.shields.io/github/repo-size/anushka-rathore14/titanic-survival-dashboard?style=for-the-badge&color=7c3aed&labelColor=0d1117)
[![GitHub stars](https://img.shields.io/github/stars/anushka-rathore14/titanic-survival-dashboard?style=for-the-badge&color=36BCF7)](https://github.com/anushka-rathore14/titanic-survival-dashboard/stargazers)
[![Open in Streamlit](https://img.shields.io/badge/Open%20in-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://titanic-survival-dashboard-egxranycqvjpuvhte8lymr.streamlit.app/.streamlit.app/)
</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🚢 About This Project

> *A complete Machine Learning project analyzing the Titanic disaster, brought to life through an interactive web dashboard using Streamlit and Plotly.*

This project demonstrates a full data science workflow. It takes the raw historical Titanic dataset, processes it through data engineering (handling missing values, binning ages, extracting titles), trains a predictive Random Forest model, and visualizes the insights dynamically through a live Streamlit UI.

<div align="center">

| 🎯 Goal | 📊 Dataset | 🏆 Model | 📈 Accuracy |
|:--------|:-----------|:------------------|:-----------------|
| Explore Survival Odds | 891 passengers | Random Forest Classifier | **81.0%** |

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🗺️ System Architecture

The application follows a clean, interactive approach. The data cleaning and modeling phase was executed in a Jupyter environment, and the final extracted insights are served via a dynamic frontend.

    Raw Kaggle CSV --> Data Cleaning (Pandas) --> Random Forest Model Insights --> Streamlit & Plotly Integration --> Interactive UI

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 📈 Insights and Dashboards

The dashboard translates raw model accuracy into a compelling visual story, allowing users to filter by passenger class and gender to uncover:
* **Demographic Survival Rates:** Visualizing the stark contrast in survival between 1st, 2nd, and 3rd class passengers.
* **Gender Breakdown:** Highlighting the impact of the "women and children first" protocol.
* **Feature Importances:** A breakdown showing exactly which variables (Sex, Pclass, Fare) the Random Forest algorithm weighed most heavily to make its predictions.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 💻 Tech Stack and Tools

<div align="center">

<p>
  <img src="https://skillicons.dev/icons?i=python,vscode,git,github&theme=dark" height="50"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
</p>
<p>
  <img src="https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=google-colab&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit%20Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />

</p>

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🚀 Getting Started

### 🌐 The Cloud Way (Recommended)
You do not need to install anything to interact with the dashboard.
👉 <a href="https://titanic-survival-dashboard-egxranycqvjpuvhte8lymr.streamlit.app/" target="_blank" rel="noopener noreferrer">Titanic Survival Explorer</a>

### ▶️ Run Locally

```bash
# 1. Clone the repository
git clone [https://github.com/YOUR-USERNAME/titanic-survival-dashboard.git](https://github.com/YOUR-USERNAME/titanic-survival-dashboard.git)
cd titanic-survival-dashboard

# 2. Install the required dependencies:
pip install -r requirements.txt

# 3. Run the dashboard locally:
streamlit run app.py
```
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

📊 Dataset Overview
The dashboard utilizes the famous Kaggle Titanic - Machine Learning from Disaster
training dataset, consisting of 891 passenger records with their known survival outcomes. 

**Key Features Include:**
- **Categorical/Grouped**: `Sex`, `Embarked`, `Age_bin`, `Fare_bin`, `Deck`
- **Numerical**: `Pclass`, `SibSp`, `Parch`,`Family_Size`,`Is_Alone`

**Citation**
Will Cukierski. <a href="https://kaggle.com/competitions/titanic">Titanic - Machine Learning from Disaster, 2012. Kaggle.</a>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🤝 Contributing & Support

Contributions, issues, and feature requests are welcome! 

1. 🍴 Fork the Project
2. 🌿 Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your Changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to the Branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

**If you found this project helpful for learning Machine Learning, please give it a ⭐!**

<div align="center">

<!-- Animated Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:00d9ff&height=120&section=footer" width="100%"/>

<br/>

<b>Made with ❤️ by <a href="https://github.com/anushka-rathore14">Anushka Rathore</a></b>

<br/><br/>

<img src="https://forthebadge.com/images/badges/built-with-love.svg" />
<img src="https://forthebadge.com/images/badges/made-with-python.svg" />
<img src="https://forthebadge.com/images/badges/open-source.svg" />

</div>


