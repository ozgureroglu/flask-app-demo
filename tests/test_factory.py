from flaskapp import create_app


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True, "DATABASE": "test.sqlite"}).testing


def test_hello(client):
    response = client.get("/hello")
    assert response.data == b"Hello, World!"
