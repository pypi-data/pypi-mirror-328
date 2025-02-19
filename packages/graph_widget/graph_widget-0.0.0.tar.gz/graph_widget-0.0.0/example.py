import marimo

__generated_with = "0.11.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import marimo as mo
    return mo, pd


@app.cell
def _():
    import graph_widget
    return (graph_widget,)


@app.cell
def _():
    import json
    import requests

    url = "https://raw.githubusercontent.com/observablehq/sample-datasets/refs/heads/main/miserables.json"
    response = requests.get(url)
    data = response.json()
    return data, json, requests, response, url


@app.cell
def _(mo):
    repulsion_slider = mo.ui.slider(
        start=-200, stop=10000, step=10, value=1, debounce=False, label="Repulsion"
    )
    node_scale_slider = mo.ui.slider(
        start=1, stop=500, step=1, value=20, debounce=True, label="Node scale"
    )
    return node_scale_slider, repulsion_slider


@app.cell
def _(data, graph_widget, mo, node_scale_slider, repulsion_slider):
    data_graph = mo.ui.anywidget(
        graph_widget.ForceGraphWidget(
            data=data,
            repulsion=repulsion_slider.value,
            node_scale=node_scale_slider.value
        )
    )
    return (data_graph,)


@app.cell
def _(data_graph, mo, node_scale_slider, repulsion_slider):
    plot = mo.hstack([ data_graph,
                mo.vstack([
                    repulsion_slider,
                    node_scale_slider])])
    return (plot,)


@app.cell
def _(plot):
    plot
    return


@app.cell
def _(data_graph):
    selected = data_graph.selected_ids
    return (selected,)


@app.cell
def _(selected):
    selected
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
