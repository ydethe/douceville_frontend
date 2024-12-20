from math import log
import typing as T

import plotly.graph_objects as go

import requests


def render_map(
    token: str,
    latitude_deg: float,
    longitude_deg: float,
    dist_s: float,
    year: int,
    nature: T.List[str],
    secteur: T.List[str],
    stat_min: int,
    transp: str = "driving-car",
) -> go.Figure:
    headers = {"Authorization": f"Bearer {token}"}

    params = dict(lat=latitude_deg, lon=longitude_deg, dist=dist_s, transp=transp)
    res = requests.get(
        "https://douceville.johncloud.fr/api/v1/isochrone", params=params, headers=headers
    )
    isochrone = res.json()

    isochrone["geometry"]
    query = dict(iso=isochrone, stat_min=stat_min, year=year, secteur=secteur, nature=nature)
    res = requests.post(
        "https://douceville.johncloud.fr/api/v1/etablissements", json=query, headers=headers
    )
    etablissements = res.json()

    geom = isochrone["geometry"]
    lon, lat = zip(*geom)

    fig = go.Figure()

    # Isochrone
    fig.add_traces(go.Scattermap(fill="toself", lon=lon, lat=lat, marker={"size": 0}))

    # Etablissements
    lon = [e["position"]["coordinates"][0] for e in etablissements]
    lat = [e["position"]["coordinates"][1] for e in etablissements]
    nom = [e["nom"] for e in etablissements]
    fig.add_traces(
        go.Scattermap(
            lat=lat,
            lon=lon,
            mode="markers",
            marker=go.scattermap.Marker(size=14),
            text=nom,
        )
    )

    x1 = min(*lon)
    x2 = max(*lon)
    y1 = min(*lat)
    y2 = max(*lat)
    max_bound = max(abs(x1 - x2), abs(y1 - y2)) * 111
    zoom = 13.5 - log(max_bound)
    fig.update_layout(
        map={
            "style": "open-street-map",
            "center": {"lon": longitude_deg, "lat": latitude_deg},
            "zoom": zoom,
        },
        showlegend=False,
    )
    fig.update_geos(fitbounds="locations")

    return fig
