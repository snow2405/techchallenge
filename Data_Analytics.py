import time
import numpy as np
import streamlit as st
import pandas as pd

###################################
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode

###################################

from functionforDownloadButtons import download_button

###################################

from streamlit_echarts import JsCode
from streamlit_echarts import st_echarts


####################
#VAIRABLES

color1 = "#52307c"
color2 = "#663a82"
color3 = "#7c5295"
color4 = "#b491c8"
color5 = "#bca0dc"

group1 = "Male"
group2 = "Female"
group3 = "Diverse"

feedback1 = "Highly Satisified"
feedback2 = "Satisified"
feedback3 = "Okay"
feedback4 = "Not Satisified"
feedback5 = "Highly Dissatisfied"


st.set_page_config(page_icon="🤝", page_title="include.us")

#st.markdown("<h1 style='text-align: center; size:74; color: red;'>Some title</h1>", unsafe_allow_html=True)

c20,c21,c22,c23 = st.columns([20,2,1,1])

with c21:
  st.button("Sign Out")
with c22:
  st.image(
    "https://icones.pro/wp-content/uploads/2021/03/icone-de-configuration-noire.png",
    width=35,
)
with c23:
  st.image(
    "https://cdn3.iconfinder.com/data/icons/business-avatar-1/512/11_avatar-512.png",
    width=35,
)


st.image(
    "https://i.ibb.co/q0mGSwk/logo-include.png",
    width=200,
)



st.title("Data Analytics")



st.text("")
st.text("")

baroptions = {
   
  "tooltip": {
    "trigger": "axis",
    "axisPointer": {
      "type": "shadow"
    }
  },
  "xAxis": {
    "type": "category",
    "data": [
      
        group1,
        group2,
        group3
    ]
  },
  "yAxis": {
    "type": "value"
  },
  "series": [
    {
      "data": [
        {
          "value": 22,
          "itemStyle": {
            "color": '#52307c'
          }
        },
        {
          "value": -13,
          "itemStyle": {
            "color": '#7c5295'
          }
        },
        {
          "value": -5,
          "itemStyle": {
            "color": '#bca0dc'
          }
        }
      ],

      "type": "bar",
      
    }
  ]
}

flowinglineoptions={
  "color": [
    "#52307c",
    "#7c5295",
    "#bca0dc"
  ],
  "tooltip": {
    "trigger": "axis",
    "axisPointer": {
      "type": "cross",
      "label": {
        "backgroundColor": "#6a7985"
      }
    }
  },
  "legend": {
    "data": [
      group1,
      group2,
      group3
    ]
  },
  "toolbox": {
    "feature": {
      "saveAsImage": {}
    }
  },
  "grid": {
    "left": "3%",
    "right": "4%",
    "bottom": "3%",
    "containLabel": True
  },
  "xAxis": [
    {
      "type": "category",
      "boundaryGap": False,
      "data": [
        
  
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Okt"

      ]
    }
  ],
  "yAxis": [
    {
      "type": "value"
    }
  ],
  "series": [
    {
      "name": group1,
      "type": "line",
      "stack": "Total",
      "smooth": True,
      "lineStyle": {
        "width": 0
      },
      "showSymbol": False,
      "areaStyle": {
        "opacity": 0.8
      },
      "emphasis": {
        "focus": "series"
      },
      "data": [
        2186,
       
        1433,
         1738,
        1160,
        
        1302,
        1763
      ]
    },
    {
      "name": group2,
      "type": "line",
      "stack": "Total",
      "smooth": True,
      "lineStyle": {
        "width": 0
      },
      "showSymbol": False,
      "areaStyle": {
        "opacity": 0.8
      },
      "emphasis": {
        "focus": "series"
      },
      "data": [
        658,
        512,
        826,
        1280,
        1537,
        2359
      ]
    },
    {
      "name": group3,
      "type": "line",
      "stack": "Total",
      "smooth": True,
      "lineStyle": {
        "width": 0
      },
      "showSymbol": False,
      "areaStyle": {
        "opacity": 0.8
      },
      "emphasis": {
        "focus": "series"
      },
      "data": [
        129,
        
        215,
        305,
        331,
        589,
        842
        
      ]
    }
  ]
}

pieoptionsA={
  "color": [
    color1,
    color2,
    color3,
    color4,
    color5
  ],
  "title": {
    "text": "Bottom 20% Engagement",
   
    "left": "center"
  },
  "tooltip": {
    "trigger": "item"
  },
  
  "series": [
    {
      "name": "Access From",
      "type": "pie",
      "radius": "50%",
      "data": [
        {
          "value": 1048,
          "name": feedback1
        },
        {
          "value": 735,
          "name": feedback2 
        },
        {
          "value": 580,
          "name": feedback3
        },
        {
          "value": 484,
          "name": feedback4
        },
        {
          "value": 300,
          "name": feedback5
        }
      ],
      "emphasis": {
        "itemStyle": {
          "shadowBlur": 10,
          "shadowOffsetX": 0,
          "shadowColor": "rgba(0, 0, 0, 0.5)"
        }
      }
    }
  ]
}

pieoptionsB={
    "color": [
    color1,
    color2,
    color3,
    color4,
    color5
  ],
  "title": {
    "text":"All Groups",
 
    "left": "center"
  },
  "tooltip": {
    "trigger": "item"
  },
  
  "series": [
    {
      "name": "Access From",
      "type": "pie",
      "radius": "50%",
      "data": [
        {
          "value": 1448,
          "name": feedback1
        },
        {
          "value": 635,
          "name": feedback2 
        },
        {
          "value": 480,
          "name": feedback3
        },
        {
          "value": 384,
          "name": feedback4
        },
        {
          "value": 200,
          "name": feedback5
        }
      ],
      "emphasis": {
        "itemStyle": {
          "shadowBlur": 10,
          "shadowOffsetX": 0,
          "shadowColor": "rgba(0, 0, 0, 0.5)"
        }
      }
    }
  ]
}

pieoptionsC={
  "color": [
    color1,
    color2,
    color3,
    color4,
    color5
  ],
  "title": {
    "text": "Bottom 20% Engagement",
   
    "left": "center"
  },
  "tooltip": {
    "trigger": "item"
  },
  
  "series": [
    {
      "name": "Access From",
      "type": "pie",
      "radius": "50%",
      "data": [
        {
          "value": 248,
          "name": feedback1
        },
        {
          "value": 435,
          "name": feedback2 
        },
        {
          "value": 680,
          "name": feedback3
        },
        {
          "value": 784,
          "name": feedback4
        },
        {
          "value": 900,
          "name": feedback5
        }
      ],
      "emphasis": {
        "itemStyle": {
          "shadowBlur": 10,
          "shadowOffsetX": 0,
          "shadowColor": "rgba(0, 0, 0, 0.5)"
        }
      }
    }
  ]
}

####################################
##MAIN
####################################

with st.sidebar:
  # ~ Harvard Buisness Review
    st.title("Include.us")
    st.subheader("Quote of the Day")
    st.markdown("<p style='text-align: left; '>'Inclusive companies are 1.7 times more likely to be innovation leaders and inclusive teams make better business decisions twice as fast.'  </p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; '>~ Harvard Buisness Review </p>", unsafe_allow_html=True)

   # st.text("Hey there, you are currently only using the demo version of Include.us. Contact our sales tean to start being inclusive today!")
   # st.markdown("<p style='text-align: left; '>Hey there, you are currently only using the demo version of Include.us. Contact our sales tean to start being inclusive today!</p>", unsafe_allow_html=True)
   

    st.subheader("Resources")
    st.markdown("<p style='text-align: left; '>It's time to Include.us! Find out more with the resources below or contact us directly.</p>", unsafe_allow_html=True)
    resultSocial = st.button("Find out how we create positive Impact")
    resultProduct = st.button("Pricing")
    resultMedia = st.button("Social Media")
    resultContact = st.button("Upgrade Now & Go Inclusive!")

 
#st.subheader('Divergent from Average Inclusion')
#chart_data = pd.DataFrame(
#    np.random.randn(3, 3),
#    columns=["Male", "Female", "Diverse"])

#st.bar_chart(chart_data)

c27,c28,c29,c30, c31 = st.columns([1,3, 1, 6,1])
with c28:
 
  st.subheader('Inclusion Index')
  st.markdown("<p style='text-align: left; '>Your weekly inclusion index is 83, up 4% from last week!</p>", unsafe_allow_html=True)
  st.image(
      "https://i.ibb.co/Xjm04v6/Screenshot-2022-10-11-004740.png",
      width=300,
  )
 # st.markdown("<p style='text-align: left; '>Your current inclusion score is 83, up 4% from last week!</p>", unsafe_allow_html=True)


with c30:
  


  st.subheader('Speech Engagement Deviation in %')
  st_echarts(baroptions)

st.title("")


st.subheader('Talking time over the last 6 months [h]')
c32,c33,c34 = st.columns([1,8,1])

with c33:
  
  st_echarts(flowinglineoptions)

  st.text(" ")
  st.text(" ")
  st.text(" ")
  st.text(" ")

st.subheader('Meeting Feedback Grouped by Engagement')

colX, colY, colZ= st.columns(3)

with colX:
  st_echarts(pieoptionsA)
with colY:
  st_echarts(pieoptionsB)
with colZ:
  st_echarts(pieoptionsC)



  
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")


  
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")

st.text("Demo Version Only")

st.text("© Copyright include.us Inc. 2022, all rights reserved")