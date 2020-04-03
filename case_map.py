import pandas as pd
import plotly.express as px
from urllib.request import urlopen
import json

def  build_map_df(
    case_file_path
):
    zip_geojson = json.loads(open("data/ca_zips.json", 'r').read())
    c_df = pd.read_csv(case_file_path, sep = '\t')
    c_df["zip"] = c_df.astype(str)
    #c_df = c_df.set_index("zip")

    fig = px.choropleth(
        c_df,
        geojson=zip_geojson,
        locations = 'zip',
        featureidkey = 'properties.ZCTA5CE10',
        color = 'count'
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig

if __name__ == "__main__":
    fig = build_map_df("data/zipcode_case_counts/through040102020_updated04022020_updated0800.txt")
    fig.show()
