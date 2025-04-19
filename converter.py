import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
        color: #000000;
    }
    .stApp {
        background-color: #f0f2f6,#bcbcbc,#cfe2f3;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }
    .h1 {
        text-align: center;
        font-size: 36px;
        color: #000000;
    }
    .stButton>button {
        background-color: #000000;
        font-weight: bold;
        color: #ffffff;
        font-size: 25px;
        padding: 10px 20px;
        margin-top: 10px;
        border-radius: 10px;
        cursor: pointer;
        transition:0.3s;
        box-shadow: 0 10px 10px gray;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        font-weight: bold;
        box-shadow: 0 15px 15px lightblue;
        background-color: #f0f2f6;
        color: Black;
    }
    .result-box {
        font-size: 20px;
        font-family: 'Times New Roman', Times, serif;
        font-weight: bold;
        text-align: center;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 10px 10px lightblue;
    }
    .footer {
        text-align: center;
        font-weight: bold;
        font-family: 'Times New Roman', Times, serif;
        font-size: 20px;
        color: black;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# title and description:
st.markdown("<h1>🚀Unit Converter Using Python And Streamlit💡</h1>", unsafe_allow_html=True)
st.write("Easily Convert Between Units Of Length, Weight And Temperature.✨")

# sidebar menu:
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", min_value=0.0, value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilograms", "Centimeters", "Millimeters", "Miles", "Feet", "Yards", "Inches"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilograms", "Centimeters", "Millimeters", "Miles", "Feet", "Yards", "Inches"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Miligrams", "Pounds" , "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Miligrams", "Pounds" , "Ounces"])
elif Conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

#Conversion Function:
def Length_converter(value, from_unit, to_unit):
    Length_unit = {
        "Meters": 1,
        "Kilograms": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Inches": 39.3701
    }
    return (value / Length_unit[from_unit]) * Length_unit[to_unit]

def Weight_converter(value, from_unit, to_unit):
    Weight_unit = {
        "Kilograms": 1,
        "Grams": 1000,
        "Miligrams": 1000000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return (value / Weight_unit[from_unit]) * Weight_unit[to_unit]

def Temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

#Button For Conversion:
if st.button("🤖 Convert"):
    if conversion_type == "Length":
        result = Length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = Weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = Temperature_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>🔍 Created By ❤️ Dua Irfan Ahmed ❤️</div>", unsafe_allow_html=True)
