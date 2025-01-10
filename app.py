import streamlit as st
import matplotlib.pyplot as plt

# Define emission factors for 30+ countries (sample data, can be updated with real data)
EMISSION_FACTORS = {
    "India": {"Transportation": 0.14, "Electricity": 0.82, "Diet": 1.25, "Waste": 0.1},
    "United States": {"Transportation": 0.41, "Electricity": 0.45, "Diet": 1.77, "Waste": 0.18},
    "China": {"Transportation": 0.12, "Electricity": 0.57, "Diet": 1.02, "Waste": 0.13},
    "Germany": {"Transportation": 0.21, "Electricity": 0.35, "Diet": 1.57, "Waste": 0.16},
    "Canada": {"Transportation": 0.30, "Electricity": 0.15, "Diet": 1.58, "Waste": 0.16},
    "Australia": {"Transportation": 0.36, "Electricity": 0.92, "Diet": 1.49, "Waste": 0.18},
    "United Kingdom": {"Transportation": 0.25, "Electricity": 0.21, "Diet": 1.50, "Waste": 0.14},
    "Brazil": {"Transportation": 0.13, "Electricity": 0.10, "Diet": 1.08, "Waste": 0.09},
    "France": {"Transportation": 0.22, "Electricity": 0.06, "Diet": 1.45, "Waste": 0.12},
    "Italy": {"Transportation": 0.25, "Electricity": 0.35, "Diet": 1.53, "Waste": 0.14},
    "Spain": {"Transportation": 0.23, "Electricity": 0.33, "Diet": 1.60, "Waste": 0.15},
    "Japan": {"Transportation": 0.28, "Electricity": 0.45, "Diet": 1.55, "Waste": 0.13},
    "South Korea": {"Transportation": 0.30, "Electricity": 0.38, "Diet": 1.60, "Waste": 0.14},
    "Mexico": {"Transportation": 0.17, "Electricity": 0.28, "Diet": 1.10, "Waste": 0.12},
    "Russia": {"Transportation": 0.35, "Electricity": 0.49, "Diet": 1.65, "Waste": 0.17},
    "Turkey": {"Transportation": 0.22, "Electricity": 0.37, "Diet": 1.50, "Waste": 0.14},
    "Saudi Arabia": {"Transportation": 0.35, "Electricity": 0.93, "Diet": 1.80, "Waste": 0.20},
    "South Africa": {"Transportation": 0.24, "Electricity": 0.95, "Diet": 1.30, "Waste": 0.18},
    "Argentina": {"Transportation": 0.14, "Electricity": 0.09, "Diet": 1.10, "Waste": 0.10},
    "Egypt": {"Transportation": 0.18, "Electricity": 0.53, "Diet": 1.20, "Waste": 0.13},
    "Indonesia": {"Transportation": 0.13, "Electricity": 0.44, "Diet": 1.05, "Waste": 0.11},
    "Nigeria": {"Transportation": 0.15, "Electricity": 0.37, "Diet": 1.00, "Waste": 0.09},
    "Vietnam": {"Transportation": 0.12, "Electricity": 0.49, "Diet": 1.10, "Waste": 0.10},
    "Thailand": {"Transportation": 0.15, "Electricity": 0.43, "Diet": 1.20, "Waste": 0.12},
    "Pakistan": {"Transportation": 0.13, "Electricity": 0.46, "Diet": 1.10, "Waste": 0.10},
    "Bangladesh": {"Transportation": 0.11, "Electricity": 0.50, "Diet": 1.00, "Waste": 0.08},
    "Chile": {"Transportation": 0.22, "Electricity": 0.21, "Diet": 1.40, "Waste": 0.13},
    "Peru": {"Transportation": 0.17, "Electricity": 0.30, "Diet": 1.10, "Waste": 0.10},
    "Poland": {"Transportation": 0.28, "Electricity": 0.65, "Diet": 1.60, "Waste": 0.15},
    "Ukraine": {"Transportation": 0.32, "Electricity": 0.53, "Diet": 1.65, "Waste": 0.16},
    "Romania": {"Transportation": 0.24, "Electricity": 0.45, "Diet": 1.50, "Waste": 0.14},
    "Sweden": {"Transportation": 0.20, "Electricity": 0.04, "Diet": 1.40, "Waste": 0.11},
}

# Set wide layout and page title
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")

# App title
st.title("🌍 Personal Carbon Calculator App ⚠️")

# Sidebar for country selection and input fields
st.sidebar.header("Input your data")

country = st.sidebar.selectbox("Select your country", list(EMISSION_FACTORS.keys()))

# Inputs for daily commute distance, electricity consumption, waste, and meals
distance = st.sidebar.slider("🚗 Daily commute distance (in km)", 0.0, 100.0, 10.0)
electricity = st.sidebar.slider("💡 Monthly electricity consumption (in kWh)", 0.0, 1000.0, 200.0)
waste = st.sidebar.slider("🗑️ Waste generated per week (in kg)", 0.0, 100.0, 5.0)
meals = st.sidebar.number_input("🍽️ Meals per day", min_value=0, max_value=10, value=3)

# Normalize inputs
distance_yearly = distance * 365
electricity_yearly = electricity * 12
meals_yearly = meals * 365
waste_yearly = waste * 52

# Emission calculations
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance_yearly / 1000
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity_yearly / 1000
diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals_yearly / 1000
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste_yearly / 1000

# Total emissions
total_emissions = transportation_emissions + electricity_emissions + diet_emissions + waste_emissions

# Display results when the button is clicked
if st.button("Calculate CO2 Emissions"):

    # Show carbon emissions by category
    st.header("Results")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚗 Transportation: {transportation_emissions:.2f} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emissions:.2f} tonnes CO2 per year")
        st.info(f"🍽️ Diet: {diet_emissions:.2f} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {waste_emissions:.2f} tonnes CO2 per year")

    with col2:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions:.2f} tonnes CO2 per year")
        st.warning(f"💡 Your carbon footprint in {country} may vary based on various factors such as lifestyle, energy mix, and transportation choices.")

    # Graphical breakdown of emissions
    st.subheader("Emissions Breakdown")

    categories = ["Transportation", "Electricity", "Diet", "Waste"]
    emissions = [transportation_emissions, electricity_emissions, diet_emissions, waste_emissions]

    fig, ax = plt.subplots()
    ax.pie(emissions, labels=categories, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

    # Educational Section
    st.subheader("Learn More About Carbon Emissions")
    st.write("""
    Your carbon footprint is a reflection of your daily activities and consumption choices. By understanding the impact of your actions, you can make informed decisions to reduce your carbon footprint. 
    Small lifestyle changes such as driving less, using energy-efficient appliances, eating less meat, and recycling more can significantly reduce your environmental impact.

    ## Global Averages:
    - The average global carbon footprint per person is roughly **4.7 tonnes** of CO2 per year.
    - High-income countries like the United States have much higher footprints (about **16.6 tonnes** per person), while low-income countries like India have significantly lower footprints (around **1.9 tonnes** per person).
    """)

# Footer for extra information
st.markdown("""
---
### 🌟 Developed By 🌟

- **Bhavleen Kaur**  
- **Mehak Sharma**  
- **Faizan Hamid**  
- **Sadhna Rao**  
- **Prajjwal Gupta**  

Source: Data from various environmental agencies and studies.
""")
