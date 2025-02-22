"""
This is the test file for the kvell_extraction package.
"""

from pathlib import Path
import pytest
from kvell_extraction import (
    PDFExtracter,
    PDFExtracterError,
    DocExtracter,
    ExcelExtracter,
    PresentationExtracter,
)


def test_basic_functionality():
    """
    Test the basic functionality of the extracters.
    """
    extracter = PDFExtracter()

    # Test PDF file
    pdf_path = "tests/test_files/sample.pdf"
    result_pdf = extracter(pdf_path)
    print("\nPDF Result:", result_pdf)
    assert isinstance(result_pdf, list)
    assert all(
        len(item) == 3 for item in result_pdf
    )  # Each item should have [page_num, text, confidence]

    # Test image file
    img_path = "tests/test_files/sample.png"
    result_img = extracter(img_path)
    print("\nImage Result:", result_img)
    assert isinstance(result_img, list)
    assert len(result_img) == 1  # Image should return single result
    assert result_img[0][0] == "0"  # Page number should be 0
    assert isinstance(result_img[0][1], str)  # Text content
    assert result_img[0][2] == "1.0"  # Confidence


def test_error_handling():
    """
    Test the error handling of the extracters.
    """
    extracter = PDFExtracter()

    # Test non-existent file
    with pytest.raises(PDFExtracterError):
        extracter("nonexistent.pdf")

    # Test unsupported file type
    with pytest.raises(PDFExtracterError):
        extracter("tests/test_files/sample.txt")


def test_doc_extraction():
    """
    Test the DOC extraction functionality.
    """
    extracter = DocExtracter()

    # Test DOC file
    doc_path = "tests/test_files/sample.docx"
    result_doc = extracter(doc_path)
    print("\nDOC Result:", result_doc)
    assert isinstance(result_doc, list)
    assert len(result_doc) == 1  # Doc should return single result
    assert result_doc[0][0] == "0"  # Page number should be 0
    assert isinstance(result_doc[0][1], str)  # Text content
    assert result_doc[0][2] == "1.0"  # Confidence

    # Test error handling
    with pytest.raises(PDFExtracterError):
        extracter("tests/test_files/nonexistent.docx")

    with pytest.raises(PDFExtracterError):
        extracter("tests/test_files/sample.txt")


def test_excel_extraction():
    """
    Test the Excel extraction functionality.
    """
    extracter = ExcelExtracter()

    # Test Excel file
    excel_path = "tests/test_files/sample.xlsx"
    result_excel = extracter(excel_path)
    print("\nExcel Result:", result_excel)
    assert isinstance(result_excel, list)
    assert len(result_excel) == 1  # Excel should return single result
    assert result_excel[0][0] == "0"  # Page number should be 0
    assert isinstance(result_excel[0][1], str)  # Text content
    assert result_excel[0][2] == "1.0"  # Confidence

    # Test error handling
    with pytest.raises(PDFExtracterError):
        extracter("tests/test_files/nonexistent.xlsx")

    with pytest.raises(PDFExtracterError):
        extracter("tests/test_files/sample.txt")


def test_presentation_extraction():
    """
    Test the PowerPoint extraction functionality.
    """
    extracter = PresentationExtracter()

    # Test PowerPoint file
    ppt_path = "tests/test_files/sample.pptx"
    result_ppt = extracter(ppt_path)
    print("\nPowerPoint Result:", result_ppt)
    assert isinstance(result_ppt, list)
    assert all(
        len(item) == 3 for item in result_ppt
    )  # Each item should have [slide_num, text, confidence]
    for item in result_ppt:
        assert isinstance(item[0], str)  # Slide number
        assert isinstance(item[1], str)  # Text content
        assert item[2] == "1.0"  # Confidence

    # Test error handling
    with pytest.raises(PDFExtracterError):
        extracter("tests/test_files/nonexistent.pptx")

    with pytest.raises(PDFExtracterError):
        extracter("tests/test_files/sample.txt")


if __name__ == "__main__":
    # Simple manual test without pytest
    extracter = PDFExtracter()

    # Create test directory and files if they don't exist
    test_dir = Path("tests/test_files")
    test_dir.mkdir(parents=True, exist_ok=True)

    # Test with a sample PDF
    pdf_path = test_dir / "sample.pdf"
    if not pdf_path.exists():
        print(f"Please place a test PDF file at: {pdf_path}")
    else:
        print("\nTesting PDF extraction:")
        result = extracter(str(pdf_path))
        print(f"PDF Result: {result}")

    # Test with a sample image
    img_path = test_dir / "sample.png"
    if not img_path.exists():
        print(f"Please place a test image file at: {img_path}")
    else:
        print("\nTesting image extraction:")
        result = extracter(str(img_path))
        print(f"Image Result: {result}")
