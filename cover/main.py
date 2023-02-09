import streamlit as st
st.title('Marcel Map')

import streamlit.components.v1 as com
com.html("""

<link href="main.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
 <div> 
   <h1> Map App <h1/>
   <hr>
 <div/>
 <table class"table">
  <th scope="col"> hello <tr/>
  <th scope="col"> test <td/>
 <table/>
 



""")
# folium
import folium

from streamlit_folium import st_folium


m = folium.Map(location=[-7.782140, 110.385221], zoom_start=16)
folium.Marker(
    [-7.782140, 110.385221], popup="Yogyakarta", tooltip="Yogyakarta"
).add_to(m)


st_data = st_folium(m, width=725)
# end folium

