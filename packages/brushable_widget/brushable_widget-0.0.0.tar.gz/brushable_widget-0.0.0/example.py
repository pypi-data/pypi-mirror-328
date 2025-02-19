import marimo

__generated_with = "0.11.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from svg import SVG, Circle
    import random
    return Circle, SVG, mo, random


@app.cell
def _(random):
    datapoints = []
    for _i in range(20):
        datapoints.append({
            'x': random.randint(20,180),
            'y': random.randint(20,180),
            'z': random.randint(20,180),
            'id': _i
        })
    return (datapoints,)


@app.cell
def _(Circle, datapoints):
    circles = []
    for datapoint in datapoints:
        circles.append(Circle(
            cx=datapoint['x'],
            cy=datapoint['y'],
            r=10,
            fill="steelblue",
            fill_opacity=0.5,
            stroke_width=1,
            stroke="white",
            class_="jfsi2 brushable",
            id=datapoint['id']
        ))
    return circles, datapoint


@app.cell
def _(SVG, circles):
    svg = SVG(
        class_="notebook",
        width=200,
        height=200,
        elements=[circles]
    )
    return (svg,)


@app.cell
def _():
    import brushable_widget
    return (brushable_widget,)


@app.cell
def _(brushable_widget, mo, svg):
    x = mo.ui.anywidget(brushable_widget.BrushableWidget(svg=svg.as_str(), selected_ids = []))
    return (x,)


@app.cell
def _(x):
    x
    return


@app.cell
def _(x):
    x.selected_ids
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
