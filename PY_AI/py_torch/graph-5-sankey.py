import plotly.graph_objects as go

df["Source_Label"] = encoder.inverse_transform(df["Source"])
df["Target_Label"] = encoder.inverse_transform(df["Target"])

fig = go.Figure(go.Sankey(
    node = dict(label=df["Source_Label"].append(df["Target_Label"]).unique()),
    link=dict(source=df["Source"], target=df["Target"], value=df["Value"])))

fig.show()
