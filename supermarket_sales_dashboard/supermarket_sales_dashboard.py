import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px


# ========================================
# Initialisation de l'application
# ========================================

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


# =========================================
# Chargement des données
# =========================================

df = pd.read_csv("supermarket_sales_dashboard/supermarket_sales.csv")


# =========================================
# Nettoyage et transformation des données
# =========================================

# Colonnes en français
colonnes = {
    "Invoice ID": "ID Facture",
    "Branch": "Succursale",
    "City": "Ville",
    "Customer type": "Type de client",
    "Gender": "Genre",
    "Product line": "Ligne de produit",
    "Unit price": "Prix unitaire",
    "Quantity": "Quantité",
    "Tax 5%": "Taxe 5%",
    "Total": "Montant total",
    "Date": "Date",
    "Time": "Heure",
    "Payment": "Paiement",
    "cogs": "Coût des marchandises vendues",
    "gross margin percentage": "Pourcentage de marge brute",
    "gross income": "Revenu brut",
    "Rating": "Note",
}
df.rename(columns=colonnes, inplace=True)

# Modalités en français

client = {"Member": "Membre", "Normal": "Normal"}

genre = {"Female": "Femme", "Male": "Homme"}

produit = {
    "Health and beauty": "Santé et beauté",
    "Electronic accessories": "Accessoires électroniques",
    "Home and lifestyle": "Maison et style de vie",
    "Sports and travel": "Sport et voyage",
    "Food and beverages": "Alimentation et boissons",
    "Fashion accessories": "Accessoires de mode",
}

paiement = {
    "Ewallet": "Portefeuille électronique",
    "Cash": "Espèces",
    "Credit card": "Carte de crédit",
}

df["Type de client"] = df["Type de client"].map(client)
df["Genre"] = df["Genre"].map(genre)
df["Ligne de produit"] = df["Ligne de produit"].map(produit)
df["Paiement"] = df["Paiement"].map(paiement)


# Convertir la colonne "Date" en datetime

df["Date"] = pd.to_datetime(df["Date"])


# =========================================
# Implémentation des fonctions
# =========================================

# Affichage


def format_decimal(x):
    return f"{x:,.2f}".replace(",", " ").replace(".", ",")


def format_entier(x):
    return f"{x:,}".replace(",", " ").replace(".", ",")


# Indicateurs


def afficher_montant_total_achats(data):
    montant_total_achats = f"{format_decimal(data['Montant total'].sum())} USD"
    return montant_total_achats


def afficher_nombre_total_achats(data):
    nombre_total_achats = f"{format_entier(data['ID Facture'].nunique())}"
    return nombre_total_achats


# Graphiques


## Histogramme
def histogramme_montants_totaux_achats(data):
    data["Ville_Genre"] = data["Ville"] + " - " + data["Genre"]
    data = data.sort_values(by="Ville_Genre")

    couleurs = ["blue", "lightblue", "red", "pink", "orange", "yellow"]

    fig = px.histogram(
        data_frame=data,
        x="Montant total",
        color="Ville_Genre",
        labels={
            "Montant Total": "Montant total des achats (USD)",
            "Ville_Genre": "Ville - Genre",
        },
        nbins=30,
        color_discrete_sequence=couleurs,
    )

    # Titre
    fig.update_layout(
        title=dict(
            text="<b>Répartition des montants totaux des achats</b><br>"
            "<b>par genre et par ville</b><br><br>",
            font=dict(
                size=21.5,
                color="black",
            ),
            x=0.5,
            xanchor="center",
            y=0.95,
        ),
        yaxis_title="Nombre total d'achats (facture)",
        xaxis=dict(
            showgrid=True,
            nticks=10,
        ),
        yaxis=dict(
            showgrid=True,
            nticks=10,
        ),
        legend=dict(
            x=1.05,
            y=0.5,
            xanchor="left",
            yanchor="middle",
            font=dict(color="black", size=13),
        ),
        margin=dict(t=70, b=5, l=5, r=5),
    )

    return fig


## Diagramme circulaire
def diagramme_categorie_produit(data):
    # Calcul des pourcentages
    df = data.groupby("Ligne de produit").size().reset_index(name="Nombre")
    df["Pourcentage"] = df["Nombre"] / df["Nombre"].sum()

    # Pourcentages en gras
    df["Texte"] = df["Pourcentage"].apply(
        lambda x: f"<b>{format_decimal(x * 100)} %</b>"
    )

    # Graphique
    fig = px.pie(
        df,
        names="Ligne de produit",
        values="Nombre",
        color="Ligne de produit",
        category_orders={"Ligne de produit": sorted(df["Ligne de produit"].unique())},
    )

    # Texte à l'intérieur du graphique
    fig.update_traces(
        text=df["Texte"],
        textinfo="text",
        textposition="inside",
        textfont=dict(color="black", size=13),
    )

    # Titre
    fig.update_layout(
        title=dict(
            text="<b>Répartition des catégories de produit</b>",
            font=dict(
                size=21.5,
                color="black",
            ),
            x=0.5,
            xanchor="center",
            y=0.95,
        ),
        legend=dict(
            title_text="Catégorie",
            x=1.05,
            y=0.5,
            xanchor="left",
            yanchor="middle",
            font=dict(color="black", size=13),
        ),
        margin=dict(t=70, b=5, l=5, r=5),
    )

    return fig


## Graphique en ligne
def evolution_montant_total_achats(data):

    # Colonne semaine
    data["Semaine"] = data["Date"].dt.isocalendar().week

    # Colonne année
    data["Annee"] = data["Date"].dt.isocalendar().year

    # Groupement par Annee, Semaine et Ville
    df = (
        data.sort_values(by=["Annee", "Semaine", "Ville"])
        .groupby(["Annee", "Semaine", "Ville"])["Montant total"]
        .sum()
        .reset_index()
    )

    # Colonne pour la semaine de l'année
    df["Semaine_annee"] = (
        "S" + df["Semaine"].astype(str) + "-" + df["Annee"].astype(str)
    )

    # Tracer l'évolution des achats par semaine et par ville
    fig = px.line(
        df,
        x="Semaine_annee",
        y="Montant total",
        color="Ville",
        labels={
            "Montant total": "Montant total des achats (USD)",
            "Semaine_annee": "Semaine",
        },
    )

    # Titre
    fig.update_layout(
        title=dict(
            text="<b>Évolution du montant total des achats par semaine et par ville</b>",
            font=dict(
                size=21.5,
                color="black",
            ),
            x=0.5,
            xanchor="center",
            y=0.95,
        ),
        legend=dict(
            x=1.05,
            y=0.5,
            xanchor="left",
            yanchor="middle",
            font=dict(color="black", size=14),
        ),
        margin=dict(t=70, b=5, l=5, r=5),
    )

    return fig


# =========================================
# Options pour les filtres
# =========================================

options_genre = [{"label": "Tous les genres", "value": "all"}] + [
    {"label": g, "value": g} for g in sorted(df["Genre"].dropna().unique())
]

options_ville = [{"label": "Toutes les villes", "value": "all"}] + [
    {"label": v, "value": v} for v in sorted(df["Ville"].dropna().unique())
]


# =========================================
# Interface utilisateur
# =========================================

app.layout = dbc.Container(
    [
        # Titre
        dbc.Row(
            [
                html.H1(
                    "Tableau de bord des ventes",
                    style={
                        "display": "flex",
                        "alignItems": "center",
                        "justifyContent": "center",
                        "color": "white",
                        "fontWeight": "bold",
                    },
                ),
            ],
            style={
                "height": "10vh",
                "backgroundColor": "#001F3F",
            },
        ),
        # Filtres
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Label(
                                    "Genre :",
                                    style={
                                        "fontSize": "2.4vh",
                                        "paddingLeft": "9vw",
                                        "color": "white",
                                        "fontWeight": "bold",
                                        "marginBottom": "1vw",
                                    },
                                ),
                                dcc.Dropdown(
                                    id="filtre-genre",
                                    options=options_genre,
                                    multi=True,
                                    value=None,
                                    placeholder="Sélectionnez le genre",
                                    style={
                                        "width": "30vw",
                                        "font-size": "2.2vh",
                                        "margin": "auto",
                                        "marginBottom": "1vw",
                                    },
                                ),
                            ]
                        )
                    ],
                    style={
                        "height": "17vh",
                        "display": "flex",
                        "flexDirection": "column",
                        "justifyContent": "center",
                        "backgroundColor": "#003366",
                    },
                    md=6,
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Label(
                                    "Ville(s) :",
                                    style={
                                        "fontSize": "2.4vh",
                                        "paddingLeft": "9vw",
                                        "color": "white",
                                        "fontWeight": "bold",
                                        "marginBottom": "1vw",
                                    },
                                ),
                                dcc.Dropdown(
                                    id="filtre-ville",
                                    options=options_ville,
                                    multi=True,
                                    value=None,
                                    placeholder="Sélectionnez la ou les villes",
                                    style={
                                        "width": "30vw",
                                        "font-size": "2.2vh",
                                        "margin": "auto",
                                        "marginBottom": "1vw",
                                    },
                                ),
                            ]
                        ),
                    ],
                    style={
                        "height": "17vh",
                        "display": "flex",
                        "flexDirection": "column",
                        "justifyContent": "center",
                        "backgroundColor": "#003366",
                    },
                    md=6,
                ),
            ]
        ),
        # Indicateurs
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5(
                                    "Montant total des achats ($)",
                                    style={
                                        "font-weight": "bold",
                                        "text-align": "center",
                                        "font-size": "3.5vh",
                                    },
                                ),
                                html.H2(
                                    id="montant-total-achats",
                                    style={
                                        "font-weight": "bold",
                                        "text-align": "center",
                                        "font-size": "5.5vh",
                                    },
                                ),
                            ]
                        ),
                        outline=True,
                        style={
                            "width": "32vw",
                            "height": "18vh",
                            "borderRadius": "1.5vw",
                            "border": "0.4vw solid #001F3F",
                            "margin": "auto",
                            "text-align": "center",
                        },
                    ),
                    style={
                        "height": "25vh",
                        "display": "flex",
                        "alignItems": "center",
                        "justifyContent": "center",
                        "backgroundColor": "#004080",
                    },
                    md=6,
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5(
                                    "Nombre total d'achats",
                                    style={
                                        "font-weight": "bold",
                                        "text-align": "center",
                                        "font-size": "3.5vh",
                                    },
                                ),
                                html.H2(
                                    id="nombre-total-achats",
                                    style={
                                        "font-weight": "bold",
                                        "text-align": "center",
                                        "font-size": "5.5vh",
                                    },
                                ),
                            ]
                        ),
                        outline=True,
                        style={
                            "width": "32vw",
                            "height": "18vh",
                            "borderRadius": "1.5vw",
                            "border": "0.4vw solid #001F3F",
                            "margin": "auto",
                            "text-align": "center",
                        },
                    ),
                    style={
                        "height": "25vh",
                        "display": "flex",
                        "alignItems": "center",
                        "justifyContent": "center",
                        "backgroundColor": "#004080",
                    },
                    md=6,
                ),
            ]
        ),
        # Graphiques
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            dcc.Graph(
                                id="hist-montants-totaux-achats",
                                style={
                                    "width": "96%",
                                    "height": "96%",
                                },
                                config={"responsive": True},
                            ),
                        ],
                        style={
                            "width": "47.5vw",
                            "height": "70vh",
                            "display": "flex",
                            "justifyContent": "center",
                            "borderRadius": "1.5vw",
                            "backgroundColor": "white",
                            "border": "0.4vw solid #001F3F",
                        },
                    ),
                    style={
                        "height": "70vh",
                        "display": "flex",
                        "justifyContent": "center",
                        "backgroundColor": "#004080",
                    },
                    md=6,
                ),
                dbc.Col(
                    html.Div(
                        [
                            dcc.Graph(
                                id="diag-categorie-produit",
                                style={
                                    "width": "96%",
                                    "height": "96%",
                                },
                                config={"responsive": True},
                            ),
                        ],
                        style={
                            "width": "47.5vw",
                            "height": "70vh",
                            "display": "flex",
                            "justifyContent": "center",
                            "borderRadius": "1.5vw",
                            "backgroundColor": "white",
                            "border": "0.4vw solid #001F3F",
                        },
                    ),
                    style={
                        "height": "70vh",
                        "display": "flex",
                        "justifyContent": "center",
                        "backgroundColor": "#004080",
                    },
                    md=6,
                ),
            ]
        ),
        dbc.Row(
            [
                html.Div(
                    [
                        dcc.Graph(
                            id="evol-montant-total-achats",
                            style={
                                "width": "96%",
                                "height": "96%",
                            },
                            config={"responsive": True},
                        ),
                    ],
                    style={
                        "width": "96.75vw",
                        "height": "70vh",
                        "display": "flex",
                        "alignItems": "center",
                        "justifyContent": "center",
                        "borderRadius": "1.5vw",
                        "backgroundColor": "white",
                        "border": "0.4vw solid #001F3F",
                    },
                ),
            ],
            style={
                "height": "77vh",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
                "backgroundColor": "#004080",
            },
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    "Projet réalisé dans le cadre du cours de Python-Dash, Master 1 ECAP (2024-2025), par Florian CROCHET sous la direction de M. Abdoul Razac SANE.",
                    style={
                        "textAlign": "center",
                        "fontStyle": "italic",
                        "fontSize": "14px",
                        "color": "white",
                    },
                ),
                style={
                    "height": "7vh",
                    "backgroundColor": "#004080",
                },
            )
        ),
    ],
    fluid=True,
)


# =========================================
# Callbacks pour les éléments interactifs
# =========================================


@callback(
    [
        Output("montant-total-achats", "children"),
        Output("nombre-total-achats", "children"),
        Output("hist-montants-totaux-achats", "figure"),
        Output("diag-categorie-produit", "figure"),
        Output("evol-montant-total-achats", "figure"),
    ],
    [
        Input("filtre-genre", "value"),
        Input("filtre-ville", "value"),
    ],
)
def update_dashboard(genre, ville):

    df_filtre = df.copy()

    if genre and genre != ["all"]:
        df_filtre = df_filtre[df_filtre["Genre"].isin(genre)]

    if ville and ville != ["all"]:
        df_filtre = df_filtre[df_filtre["Ville"].isin(ville)]

    # Indicateurs

    indic_montant_total_achats = afficher_montant_total_achats(df_filtre)

    indic_nombre_total_achats = afficher_nombre_total_achats(df_filtre)

    # Graphiques

    hist_montants_totaux_achats = histogramme_montants_totaux_achats(df_filtre)

    diag_categorie_produit = diagramme_categorie_produit(df_filtre)

    evol_montant_total_achats = evolution_montant_total_achats(df_filtre)

    return (
        indic_montant_total_achats,
        indic_nombre_total_achats,
        hist_montants_totaux_achats,
        diag_categorie_produit,
        evol_montant_total_achats,
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000, jupyter_mode="external")
