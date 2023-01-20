import hello


def test_hello_name():
    assert "bob" in hello.hello_name("bob")
    assert "bob" not in hello.hello_name("not")
