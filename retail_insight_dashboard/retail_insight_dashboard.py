# Import des bibliothèques essentielles
import numpy as np
import pandas as pd
from calendar import month_abbr, month_name

# Import de Dash et de ses composants
import dash
from dash import Dash, dcc, html, dash_table, Input, Output, callback
import dash_bootstrap_components as dbc

# Import de Plotly pour la visualisation
import plotly.express as px
import plotly.graph_objects as go


# ========================================
# Initialisation de l'application
# ========================================

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


# =========================================
# Chargement des données
# =========================================

df = pd.read_csv(
    "retail_insight_dashboard/omnichannel_retail_line_items.csv", index_col=0
)


# =========================================
# Sélection des colonnes
# =========================================

df = df[
    [
        "CustomerID",
        "Gender",
        "Location",
        "Product_Category",
        "Quantity",
        "Avg_Price",
        "Transaction_Date",
        "Month",
        "Discount_pct",
    ]
]

colonnes = [
    "Date",
    "Gender",
    "Location",
    "Product_Category",
    "Quantity",
    "Avg_Price",
    "Discount_pct",
]


# =========================================
# Nettoyage et transformation des données
# =========================================

df["CustomerID"] = df["CustomerID"].fillna(0).astype(int)
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])

df["Total_price"] = (
    df["Quantity"] * df["Avg_Price"] * (1 - (df["Discount_pct"] / 100)).round(3)
)

df["Date"] = df["Transaction_Date"].dt.date


# =========================================
# Implémentation des fonctions
# =========================================


def calculer_chiffre_affaire(data):
    return data["Total_price"].sum()


def frequence_meilleure_vente(data, top=10, ascending=False):
    resultat = (
        pd.crosstab(
            [data["Gender"], data["Product_Category"]],
            "Total vente",
            values=data["Total_price"],
            aggfunc=lambda x: len(x),
            rownames=["Sexe", "Categorie du produit"],
            colnames=[""],
        )
        .reset_index()
        .groupby(["Sexe"], as_index=False, group_keys=True)
        .apply(
            lambda x: x.sort_values("Total vente", ascending=ascending).iloc[:top, :]
        )
        .reset_index(drop=True)
        .set_index(["Sexe", "Categorie du produit"])
    )

    return resultat


def indicateur_du_mois(data, current_month=12, freq=True, abbr=False):
    previous_month = current_month - 1 if current_month > 1 else 12
    if freq:
        resultat = data["Month"][
            (data["Month"] == current_month) | (data["Month"] == previous_month)
        ].value_counts()
        # sort by index
        resultat = resultat.sort_index()
        resultat.index = [
            (month_abbr[i] if abbr else month_name[i]) for i in resultat.index
        ]
        return resultat
    else:
        resultat = (
            data[(data["Month"] == current_month) | (data["Month"] == previous_month)]
            .groupby("Month")
            .apply(calculer_chiffre_affaire)
        )
        resultat.index = [
            (month_abbr[i] if abbr else month_name[i]) for i in resultat.index
        ]
        return resultat


def barplot_top_10_ventes(data):
    df_plot = frequence_meilleure_vente(data, ascending=True)
    graph = px.bar(
        df_plot,
        x="Total vente",
        y=df_plot.index.get_level_values(1),
        color=df_plot.index.get_level_values(0),
        barmode="group",
        title="Frequence des 10 meilleures ventes",
        labels={"x": "Fréquence", "y": "Categorie du produit", "color": "Sexe"},
    ).update_layout(margin=dict(t=60))
    return graph


# Evolution chiffre d'affaire
def plot_evolution_chiffre_affaire(data):
    df_plot = data.groupby(pd.Grouper(key="Transaction_Date", freq="W")).apply(
        calculer_chiffre_affaire
    )[:-1]
    chiffre_evolution = px.line(
        x=df_plot.index,
        y=df_plot,
        title="Evolution du chiffre d'affaire par semaine",
        labels={"x": "Semaine", "y": "Chiffre d'affaire"},
    ).update_layout(
        margin=dict(t=40, b=0),
    )
    return chiffre_evolution


## Chiffre d'affaire du mois
def plot_chiffre_affaire_mois(data):
    df_plot = indicateur_du_mois(data, freq=False)
    indicateur = go.Figure(
        go.Indicator(
            mode="number+delta",
            value=df_plot[1],
            delta={"reference": df_plot[0]},
            domain={"row": 0, "column": 1},
            title=f"{df_plot.index[1]}",
        )
    ).update_layout(margin=dict(l=0, r=0, t=30, b=0))
    return indicateur


# Ventes du mois
def plot_vente_mois(data, abbr=False):
    df_plot = indicateur_du_mois(data, freq=True, abbr=abbr)
    indicateur = go.Figure(
        go.Indicator(
            mode="number+delta",
            value=df_plot[1],
            delta={"reference": df_plot[0]},
            domain={"row": 0, "column": 1},
            title=f"{df_plot.index[1]}",
        )
    ).update_layout(margin=dict(l=0, r=0, t=30, b=0))
    return indicateur


# Table des ventes
table_des_ventes = dash_table.DataTable(
    id="table-ventes",
    editable=False,
    filter_action="native",
    sort_action="native",
    page_action="native",
    page_current=0,
    page_size=10,
    columns=[{"id": c, "name": c.replace("_", " ").title()} for c in colonnes],
    style_cell={
        "font-size": "1.2vw",
        "font-family": "Arial",
        "fontWeight": "bold",
    },
)


# =========================================
# Structure de l'application
# =========================================

app.layout = dbc.Container(
    [
        # ligne 1
        dbc.Row(
            [
                # ligne 1 colonne 1
                dbc.Col(
                    html.H3("ECAP Store"),
                    md=6,
                    style={
                        "height": "7vh",
                        "display": "flex",
                        "alignItems": "center",
                    },
                ),
                # ligne 1 colonne 2
                dbc.Col(
                    [
                        dcc.Dropdown(
                            id="filtre-location",
                            options=[{"label": "Toutes les zones", "value": "all"}]
                            + [
                                {"label": loc, "value": loc}
                                for loc in sorted(df["Location"].dropna().unique())
                            ],
                            multi=True,
                            value=None,
                            placeholder="Choisissez des zones",
                            style={
                                "width": "80%",
                                "font-size": "16px",
                            },
                        )
                    ],
                    md=6,
                    style={
                        "height": "7vh",
                        "display": "flex",
                        "alignItems": "center",
                        "justifyContent": "center",
                    },
                ),
            ],
            style={"backgroundColor": "#bad7e4"},
        ),
        # ligne 2
        dbc.Row(
            [
                # ligne 2 colonne 1
                dbc.Col(
                    [
                        # ligne 2 colonne 1 ligne 1
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Graph(
                                        id="chiffre-affaires",
                                        style={
                                            "width": "80%",
                                            "height": "80%",
                                        },
                                        config={"responsive": True},
                                    ),
                                    style={
                                        "width": "50%",
                                        "height": "23vh",
                                        "display": "flex",
                                        "alignItems": "center",
                                        "justifyContent": "center",
                                    },
                                ),
                                dbc.Col(
                                    dcc.Graph(
                                        id="vente-mois",
                                        style={
                                            "width": "80%",
                                            "height": "80%",
                                        },
                                        config={"responsive": True},
                                    ),
                                    style={
                                        "width": "50%",
                                        "height": "23vh",
                                        "display": "flex",
                                        "alignItems": "center",
                                        "justifyContent": "center",
                                    },
                                ),
                            ]
                        ),
                        # ligne 2 colonne 1 ligne 2
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Graph(
                                        id="barplot-vente",
                                        style={
                                            "width": "110%",
                                            "height": "100%",
                                        },
                                        config={"responsive": True},
                                    ),
                                    style={
                                        "height": "70vh",
                                    },
                                )
                            ]
                        ),
                    ],
                    md=5,
                ),
                # ligne 2 colonne 2
                dbc.Col(
                    [
                        # ligne 2 colonne 2 ligne 1
                        dbc.Row(
                            [
                                dbc.Col(
                                    dcc.Graph(
                                        id="evolution-ca",
                                        style={
                                            "width": "120%",
                                            "height": "90%",
                                        },
                                        config={"responsive": True},
                                    ),
                                    style={
                                        "height": "47vh",
                                        "display": "flex",
                                        "alignItems": "center",
                                    },
                                )
                            ]
                        ),
                        # ligne 2 colonne 2 ligne 2
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H5(
                                            "Table des 100 dernières ventes",
                                            style={"paddingLeft": "3vw"},
                                        ),
                                        table_des_ventes,
                                    ],
                                    style={
                                        "height": "46vh",
                                    },
                                )
                            ]
                        ),
                    ],
                    md=7,
                ),
            ]
        ),
    ],
    fluid=True,
)


# =========================================
# Callbacks pour les éléments interactifs
# =========================================


@callback(
    [
        Output("chiffre-affaires", "figure"),
        Output("vente-mois", "figure"),
        Output("barplot-vente", "figure"),
        Output("evolution-ca", "figure"),
        Output("table-ventes", "data"),
    ],
    Input("filtre-location", "value"),
)
def update_graphs(locations):

    df_filtre = df.copy()

    if locations:
        df_filtre = df_filtre[df_filtre["Location"].isin(locations)]

    chiffre_affaires = plot_chiffre_affaire_mois(df_filtre)
    vente_mois = plot_vente_mois(df_filtre)
    barplot_vente = barplot_top_10_ventes(df_filtre)
    evolution_ca = plot_evolution_chiffre_affaire(df_filtre)
    table_ventes = (
        df_filtre[colonnes]
        .sort_values(by="Date", ascending=False)
        .head(100)
        .to_dict("records")
    )

    return (chiffre_affaires, vente_mois, barplot_vente, evolution_ca, table_ventes)


if __name__ == "__main__":
    app.run(debug=True, port=8100, jupyter_mode="external")
