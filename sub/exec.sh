#!/bin/bash
OUTPUT=$(ps aux |grep "python")
string='sub-elec110'

if [[ $OUTPUT =~ $string ]]; then
      echo "run"
else
      echo "Test Start!"
      /usr/local/bin/python /sub/app/sub-elec110.py &
      /usr/local/bin/python /sub/app/sub-elec220.py &
      /usr/local/bin/python /sub/app/sub-plug1-1.py &
      /usr/local/bin/python /sub/app/sub-plug1-2.py &
      /usr/local/bin/python /sub/app/sub-plug1-3.py &
      /usr/local/bin/python /sub/app/sub-plug3-1.py &
      /usr/local/bin/python /sub/app/sub-plug3-2.py &
      /usr/local/bin/python /sub/app/sub-plug3-3.py &
fi

exit 0
