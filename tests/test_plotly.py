from rxconfig import config
from douceville_frontend.douceville_frontend import create_access_token
from douceville_frontend.map_render import render_map


def test_map():
    username = "yann@johncloud.fr"
    password = "a,4Tosh!"

    token = create_access_token(config.SUPABASE_URL, config.SUPABASE_KEY, username, password)

    fig = render_map(
        token,
        latitude_deg=43.604419,
        longitude_deg=1.443379,
        dist_s=600,
        year=2020,
        nature=[],
        secteur=[],
        stat_min=0,
    )

    fig.show()


if __name__ == "__main__":
    test_map()
