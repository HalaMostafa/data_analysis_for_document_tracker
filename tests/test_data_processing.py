import pytest
import logging
from data_processing import dataProcessing


# Create and configure logger
logging.basicConfig(filename="display.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()


def test_getData():
    test = dataProcessing()
    status = test.getData(file_path ="issuu_cw2.json", display = logger)
    assert status=="File Uploaded Successfuly"
