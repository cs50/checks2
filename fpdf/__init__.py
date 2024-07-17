import check50


@check50.check()
def test_range_level_1():
    """Print fpdf version"""

    # With random.seed(0) in testing.py, 6 + 6 is expected output from randint and randrange with range of 0–9
    check50.run("pip3 freeze | grep fpdf").stdin(level, prompt=False).stdout(
        "Debugging", "Debugging", regex=True
    )
