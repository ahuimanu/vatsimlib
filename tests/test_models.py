from datetime import datetime
import pytest

from ..models.models import VatsimGeneral

def test_datetime_from_iso_timestamp():
	# arrange
	t = VatsimGeneral('1',						# version
        			  '1',						# reload
        			  '00000',					# update
        			  '2021-04-27T18:39:55',	# timestamp
					  1,						# connected clients
					  1, 						# unique clients
    )
	# act
	dt = t.get_datetime()
	print(dt.timetz.__repr__)

	# assert
	assert dt == datetime.fromisoformat('2021-04-27T18:39:55')
