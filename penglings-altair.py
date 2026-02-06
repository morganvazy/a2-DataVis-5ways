
import altair as alt
import pandas as pd

df = pd.read_csv("penglings.csv")
#https://altair-viz.github.io/gallery/scatter_tooltips.html
#https://altair-viz.github.io/user_guide/customization.html
#https://altair-viz.github.io/user_guide/generated/channels/altair.Size.html
#resource for making a scatterplot

chart = alt.Chart(df).mark_circle().encode(
    alt.X("flipper_length_mm").scale(zero=False).title("Flipper length (mm)"),
    alt.Y("body_mass_g").scale(zero=False).title("Body mass (g)"),
    color = alt.Color("species", scale=alt.Scale(
        domain = ["Adelie", "Chinstrap", "Gentoo"],
        range = ["#FA9702","#B802FA","#018A75"]
    )),
    size=alt.Size("bill_length_mm", scale=alt.Scale(range=[0,200])),
    tooltip = ["flipper_length_mm", "body_mass_g", "species", "bill_length_mm"]
).interactive()

chart.save("penglings_altair.html")