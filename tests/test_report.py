import pytest

from main import SalesReport

HEADER = "ORDERNUMBER,SALES,PRODUCTLINE\n"


def write_csv(tmp_path, body: str):
    path = tmp_path / "sales.csv"
    path.write_text(HEADER + body)
    return path


@pytest.fixture
def report(tmp_path):
    # Order 1 = 150, order 2 = 200; Cars = 300, Ships = 50
    return SalesReport(write_csv(tmp_path, "1,100,Cars\n1,50,Ships\n2,200,Cars\n"))


def test_total_sales(report):
    assert report.total_sales() == pytest.approx(350)


def test_average_order(report):
    assert report.avg_order_value() == pytest.approx(175)   # 350 / 2 orders


def test_top_product(report):
    assert report.top_product_line() == "Cars"


def test_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        SalesReport(tmp_path / "nope.csv")


def test_empty_file_raises(tmp_path):
    path = tmp_path / "empty.csv"
    path.write_text("")
    with pytest.raises(ValueError, match="no data rows"):
        SalesReport(path)


def test_header_only_raises(tmp_path):
    with pytest.raises(ValueError, match="no data rows"):
        SalesReport(write_csv(tmp_path, ""))


def test_bad_number_row_is_skipped(tmp_path, capsys):
    path = write_csv(tmp_path, "1,100,Cars\n2,abc,Ships\n")
    report = SalesReport(path)
    assert report.total_sales() == pytest.approx(100)
    assert "skipped 1 row" in capsys.readouterr().err