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



st.set_page_config(page_icon="🤝", page_title="Include.us")

#st.markdown("<h1 style='text-align: center; size:74; color: red;'>Some title</h1>", unsafe_allow_html=True)

st.image(
    "https://i.ibb.co/q0mGSwk/logo-include.png",
    width=200,
)


col1, col2, col3, col4 = st.columns(4)

with col1:
 st.title("Include.us")

with col4:
  st.image(
      "https://i.ibb.co/NYTfP1d/Screenshot-2022-10-11-004740.png",
      width=100,
  )

#st.text ("Your current inclusion score is 83, up 4% from last week!")
st.markdown("<p style='text-align: left; '>Your current inclusion score is 83, up 4% from last week!</p>", unsafe_allow_html=True)

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
      
        "06.10.2022",
        "07.10.2022",
        "08.10.2022",
        "09.10.2022",
        "Monday",
        "Tuesday"
    ]
  },
  "yAxis": {
    "type": "value"
  },
  "series": [
    {
      "data": [
        {
          "value": 91,
          "itemStyle": {
            "color": '#0000ff'
          }
        },
        {
          "value": 79,
          "itemStyle": {
            "color": '#0044ff'
          }
        },
        {
          "value": 67,
          "itemStyle": {
            "color": '#0066ff'
          }
        },
        {
          "value": 92,
          "itemStyle": {
            "color": '#3388ff'
          }
        },
        {
         "value": 86,
          "itemStyle": {
            "color": '#55aaff'
          }
        },
        {
          "value": 97,
          "itemStyle": {
            "color": '#77ccff'
          }
        }
      ],

      "type": "bar",
      
    }
  ]
}

flowinglineoptions={
  "color": [
    "#0066ff",
    "#00DDFF",
    "#37A2FF",
    "#FF0087",
    "#FFBF00"
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
      "Male",
      "Female",
      "Diverse"
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
      "name": "Male",
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
      "name": "Female",
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
      "name": "Diverse",
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
  "title": {
    "text": "A",
    "subtext": "Fake Data",
    "left": "center"
  },
  "tooltip": {
    "trigger": "item"
  },
  "legend": {
    "orient": "vertical",
    "left": "left"
  },
  "series": [
    {
      "name": "Access From",
      "type": "pie",
      "radius": "50%",
      "data": [
        {
          "value": 1048,
          "name": "Search Engine"
        },
        {
          "value": 735,
          "name": "Direct"
        },
        {
          "value": 580,
          "name": "Email"
        },
        {
          "value": 484,
          "name": "Union Ads"
        },
        {
          "value": 300,
          "name": "Video Ads"
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
  "title": {
    "text": "B",
    "subtext": "Fake Data",
    "left": "center"
  },
  "tooltip": {
    "trigger": "item"
  },
  "legend": {
    "orient": "vertical",
    "left": "left"
  },
  "series": [
    {
      "name": "Access From",
      "type": "pie",
      "radius": "50%",
      "data": [
        {
          "value": 1048,
          "name": "Search Engine"
        },
        {
          "value": 735,
          "name": "Direct"
        },
        {
          "value": 580,
          "name": "Email"
        },
        {
          "value": 484,
          "name": "Union Ads"
        },
        {
          "value": 300,
          "name": "Video Ads"
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
  "title": {
    "text": "Referer of a Website",
    "subtext": "Fake Data",
    "left": "center"
  },
  "tooltip": {
    "trigger": "item"
  },
  "legend": {
    "orient": "vertical",
    "left": "left"
  },
  "series": [
    {
      "name": "Access From",
      "type": "pie",
      "radius": "50%",
      "data": [
        {
          "value": 1048,
          "name": "Search Engine"
        },
        {
          "value": 735,
          "name": "Direct"
        },
        {
          "value": 580,
          "name": "Email"
        },
        {
          "value": 484,
          "name": "Union Ads"
        },
        {
          "value": 300,
          "name": "Video Ads"
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

st.subheader('Divergent from Average Inclusion')
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["Male", "Female", "Diverse"])

st.bar_chart(chart_data)

st.text("")
st.text("")

st.subheader('Diversity score over the last days')
st_echarts(baroptions)

st.text("")
st.text("")

st.subheader('Inclusion minutes over the last 6 months')
st_echarts(flowinglineoptions)

st.text("")
st.text("")


colA, colB, colC = st.columns(3)

st_echarts(pieoptionsA)
st_echarts(pieoptionsB)
st_echarts(pieoptionsC)

"""
with colA:
  st_echarts(pieoptionsA)
with colB:
  st_echarts(pieoptionsB)
with colC:
  st_echarts(pieoptionsC)
"""
