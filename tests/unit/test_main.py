# # ============ Imports =========== #

# import pytest
# from pathlib import Path
# import tempfile
# import shutil
# from unittest.mock import patch
# from main import create_directory, is_valid_url, generate_qr_code, setup_logging

# # ============ Tests =========== #

# def test_is_valid_url_with_valid_url():
#     """Test if valid URL returns True"""
#     assert is_valid_url("https://github.com/CxLos/CxLos_Docker_Assignment") == True

# def test_is_valid_url_with_invalid_url():
#     """Test if url returns False"""
#     assert is_valid_url("/CxLos/CxLos_Docker_Assignment ") == False

# def test_is_valid_url_logs_error_for_invalid_url():
#     """Test that logging.error is called for invalid URL"""
#     url = "invalid_url.cm"
#     result = is_valid_url(url)
#     assert result == False

# def test_create_directory():
#     """Test that directory is created successfully"""
#     with tempfile.TemporaryDirectory() as tmpdir:
#         test_path = Path(tmpdir) / "test_folder"
#         create_directory(test_path)
#         assert test_path.exists()
#         assert test_path.is_dir()

# def test_generate_qr_code_valid_url():
#     """Test if qr codees successfully generate with valid url"""
#     with tempfile.TemporaryDirectory() as tmpdir:
#         test_path = Path(tmpdir) / "test_qr.png"
#         generate_qr_code("https://github.com", test_path, "red", "blue")
#         assert test_path.exists()
#         assert test_path.suffix == ".png"

# def test_generate_qr_code_with_invalid_url():
#     """Test that qr code is not generated with invalid url"""
#     with tempfile.TemporaryDirectory() as tmpdir:
#         test_path = Path(tmpdir) / "test_qr.png"
#         generate_qr_code("htps:/githu.cm", test_path, "green", "yellow")
#         assert not test_path.exists()

# # =========== Exception Handling Tests =========== #

# def test_fail_to_create_directory():
#     """Test that exception handler is triggered when directory creation fails"""

#     with patch('main.Path.mkdir') as mock_mkdir:
#         mock_mkdir.side_effect = Exception("Failed to create directory")

#         with patch('main.logging.error') as mock_log:
            
#             with pytest.raises(SystemExit) as exit_info:
#                 path = Path('invalide/directory')
#                 create_directory(path)
            
#             assert exit_info.value.code == 1
#             mock_log.assert_called_once()

# def test_generate_qr_code_handles_exception():
#     """Test that exception handler is triggered when QR generation fails"""

#     with patch('main.qrcode.QRCode') as mock_qr:
#         mock_qr.side_effect = Exception("Simulated QR generation error") 
        
#         with tempfile.TemporaryDirectory() as tmpdir:
#             test_path = Path(tmpdir) / "test_qr.png"
#             with patch('main.logging.error') as mock_log:
#                 generate_qr_code("https://github.com", test_path)
#                 mock_log.assert_called_once()
#             assert not test_path.exists()