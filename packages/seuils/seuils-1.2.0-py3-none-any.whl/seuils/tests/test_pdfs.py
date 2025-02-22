import requests

from seuils.usure import local_liens, local_pdf, source


def test_remote():
    for x in local_liens():
        response = requests.get(f"{source}/assets/pdf/{x}.pdf")
        assert response.status_code == 200


def test_local():
    for x in local_liens():
        assert local_pdf(x) is not False
